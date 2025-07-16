import praw

def initialize_reddit(client_id, client_secret):
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="persona-extractor-script by u/SwimmingIndividual61"
    )

def fetch_user_data(username, reddit, limit=100):
    user = reddit.redditor(username)
    data = []

    for comment in user.comments.new(limit=limit):
        data.append(comment.body)

    for post in user.submissions.new(limit=limit):
        text = post.title + "\n" + post.selftext
        data.append(text)

    return "\n\n".join(data)
