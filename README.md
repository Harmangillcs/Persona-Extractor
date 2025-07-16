# Reddit Persona Extractor

This tool scrapes posts and comments from a Reddit user and generates a detailed user persona using an LLM (like GPT-4). Useful for analyzing digital behavior or as part of user research.

## Features

- Scrapes posts and comments using PRAW
- Constructs a persona with attributes (goals, frustrations, hobbies, etc.)
- Cites specific Reddit content for each trait
- Outputs to a `.txt` file

## Requirements

- Python 3.7+
- PRAW
- OpenAI API key
- Reddit API credentials

## Setup

1. Clone the repo:
```bash
git clone https://github.com/yourusername/reddit_persona_extractor.git
cd reddit_persona_extractor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
OPENAI_API_KEY=your_openai_key
```

## Usage

```bash
python main.py TheRealMaverick
```

This will create a file at `persona_output/TheRealMaverick.txt`.

## Example

See `persona_output/TheRealMaverick.txt` for a sample output.
