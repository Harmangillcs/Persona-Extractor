# Reddit Persona Extractor

This tool scrapes posts and comments from a Reddit user and generates a detailed user persona using a Hugging Face LLM model. It’s useful for digital behavior analysis or UX/user research.

## Features

- Scrapes Reddit data using PRAW
- Uses LangChain to split and process text
- Generates a structured persona with:
  - Personality
  - Hobbies & Interests
  - Goals & Motivations
  - Frustrations
  - Writing Style
  - Demographic Clues
  - Citation from Reddit content
- Outputs the result into `persona_output.txt`

## Requirements

- Python 3.7+
- PRAW
- LangChain
- HuggingFace Transformers
- FAISS
- Torch
- A Hugging Face account for model access

#setup

1. Clone the repo:
```bash
git clone https://github.com/Harmangillcs/Persona-Extractor.git
cd Persona-Extractor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
##File Structure

main.py – Main entry point, handles input and coordination
reddit_scraper.py – Fetches Reddit user content
persona_generator.py – Loads model, splits text, runs persona generation


## Usage

```bash
python main.py 
```


## Example

See `persona_output/persona_output.txt` for a sample output.
