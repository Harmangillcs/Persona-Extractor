import requests
import praw
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="persona-extractor"
)

def fetch_user_content(username, limit=100):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for submission in user.submissions.new(limit=limit):
        posts.append(f"Title: {submission.title}\nText: {submission.selftext}")
    for comment in user.comments.new(limit=limit):
        comments.append(comment.body)

    return posts, comments

def build_prompt(posts, comments):
    combined_text = "\n\n".join(posts + comments)
    prompt = f"""
Extract a detailed user persona based on the following Reddit posts and comments. 
The persona should include: personality, hobbies, goals, frustrations, writing style, and demographic clues. 
Cite the text you are using for each attribute.

Text:
"""{combined_text}"""
"""
    return prompt

def generate_persona(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert persona profiler."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

def save_persona(output, username):
    output_path = f"persona_output/{username}.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Reddit username (without /u/)")
    args = parser.parse_args()

    posts, comments = fetch_user_content(args.username)
    prompt = build_prompt(posts, comments)
    persona = generate_persona(prompt)
    save_persona(persona, args.username)

if __name__ == "__main__":
    main()
