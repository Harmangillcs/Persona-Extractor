from getpass import getpass
import os

from reddit_scraper import initialize_reddit, fetch_user_data
from persona_generator import (
    create_chunks,
    create_vectorstore,
    load_llm_model,
    build_prompt,
    generate_persona
)

def main():
    client_id = getpass("Enter your Reddit client_id: ")
    client_secret = getpass("Enter your Reddit client_secret: ")

    reddit = initialize_reddit(client_id, client_secret)

    username = "kojied"  
    combined_text = fetch_user_data(username, reddit)

    llm = load_llm_model()
    prompt = build_prompt()

    persona = generate_persona(combined_text, llm, prompt)

    with open("persona_output.txt", "w", encoding="utf-8") as f:
        f.write(persona)

    print("Saved to persona_output.txt")

if __name__ == "__main__":
    main()
