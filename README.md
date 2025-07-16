# Reddit Persona Extractor

This tool scrapes posts and comments from a Reddit user and generates a detailed user persona using an LLM model . Useful for analyzing digital behavior or as part of user research.

## Features

- Scrapes posts and comments using PRAW
- Constructs a persona with attributes (goals, frustrations, hobbies, etc.)
- Cites specific Reddit content for each trait
- Outputs to a `.txt` file

## Requirements

- Python 3.7+
- PRAW
- LLM Models
- Reddit API credentials

## Setup

1. Clone the repo:
```bash
git clone https://github.com/Harmangillcs/Persona-Extractor.git
cd Persona-Extractor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
```

## Usage

```bash
python main.py 
```


## Example

See `persona_output/persona_output.txt` for a sample output.
