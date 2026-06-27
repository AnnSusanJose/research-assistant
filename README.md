# Research Assistant

An AI-powered command-line research assistant built with Python and the Gemini API. The application reads notes from a text file and provides features such as summarization, explanation, and quiz generation.

## Features

* 📄 Load and display notes from a text file
* 📝 Generate concise summaries in bullet points
* 💡 Explain complex topics in simple language
* ❓ Create multiple-choice quizzes automatically
* 💾 Save generated outputs to `output.txt`


## Technologies Used

* Python
* Gemini API
* `google-generativeai`
* `python-dotenv`

## Installation

Clone the repository:

```bash
git clone https://github.com/AnnSusanJose/research-assistant.git
cd research-assistant
```

Install dependencies:

```bash
pip install google-generativeai python-dotenv
```

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

## Usage

Run the application:

```bash
python assistant.py
```

Menu:

```text
0. LOAD NOTES
1. SUMMARIZE NOTES
2. EXPLAIN NOTES
3. GENERATE QUIZ
4. EXIT
```

The program reads content from `sample.txt` and saves generated responses to `output.txt`.

## Example Features

### Summary Generation

* Produces key points in concise bullet form.

### Simple Explanations

* Converts technical content into beginner-friendly explanations.

### Quiz Generation

* Creates five multiple-choice questions with answers based on the provided notes.

