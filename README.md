# Research Assistant

An AI-powered command-line research assistant built with Python and the Google Gemini API.

## Features

* Load and display notes from text files
* Summarize notes into key points
* Explain concepts in simple language
* Generate multiple-choice quizzes
* Ask custom questions based on notes
* Create flashcards for revision
* Generate text-based mind maps
* Save generated outputs

## Tech Stack

* Python
* Google Gemini API
* python-dotenv

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run the application:

```bash
python assistant.py
```

## Menu

```text
0. Load Notes
1. Display Notes
2. Summarize Notes
3. Explain Notes
4. Generate Quiz
5. Ask a Question
6. Generate Flashcards
7. Generate Mind Map
8. Exit
```
