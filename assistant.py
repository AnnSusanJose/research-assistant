from dotenv import load_dotenv
import os
import google.generativeai as genai
from pypdf import PdfReader


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])
notes=""
print("chatbot loading.. performes on sample.txt")
def load_doc(fname):
    if fname.lower().endswith(".txt"):
        with open(fname, "r") as file:
            content = file.read()
            return content
    elif fname.lower().endswith(".pdf"):
        reader = PdfReader(fname)
        notes = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                notes += text + "\n"
        return notes
    else:
        raise ValueError("Unsupported file format. Please provide a .txt or .pdf file.")
def summarize_notes(content):
    prompt = f"""
    Summarize the following notes in 5 bullet points:

    {content}
    """
    try:
        res=chat.send_message(prompt)
        print("---Summary---",res.text)
        return res
    except Exception as e:
        print("Error occurred while summarizing notes:", e)
        return None
def explain(content):
    prompt = f"""
    Explain the following notes in simple terms:
    
    {content}
    """
    try:
        res=chat.send_message(prompt)
        print("---Explanation---",res.text)
        return res
    except Exception as e:
        print("Error occurred while explaining notes:", e)
        return None
def generate_quiz(content):
    prompt = f"""
    Generate a quiz based on the following notes. Include 5 multiple-choice questions with 4 options each and provide the correct answer for each question:

    {content}
    """
    try:
        res=chat.send_message(prompt)
        print("---Quiz---",res.text)
        return res
    except Exception as e:
        print("Error occurred while generating quiz:", e)
        return None
def ask_qn(content):
    qn=input("Enter your question: ")
    prompt = f"""
    Using only these notes:

    {content}

    Answer this question:

    {qn}
    """
    try:
        res=chat.send_message(prompt)
        print("---Answer---",res.text)
        return res
    except Exception as e:
        print("Error occurred while asking question:", e)
        return None
def gen_fcards(content):
    prompt = f"""
    Generate flashcards based on the following notes. Each flashcard should have a question on one side and the answer on the other side. Provide 5 flashcards:

    {content}
    """
    try:
        res=chat.send_message(prompt)
        print("---Flashcards---",res.text)
        return res
    except Exception as e:
        print("Error occurred while generating flashcards:", e)
        return None
def gen_mindmap(content):
    prompt = f"""
    Generate a mind map based on the following notes. Provide a visual representation of the relationships between different concepts:

    {content}
    """
    try:
        res=chat.send_message(prompt)
        print("---Mind Map---",res.text)
        return res
    except Exception as e:
        print("Error occurred while generating mind map:", e)
        return None
def analyse_paper(content):
    prompt = f"""
    Analyze this research paper and provide:

1. Title
2. Problem Statement
3. Methodology
4. Dataset Used
5. Evaluation Metrics
6. Results
7. Limitations
8. Future Work
    {content}
    """
    try:
        res=chat.send_message(prompt)
        print("---Paper Analysis---",res.text)
        return res
    except Exception as e:
        print("Error occurred while analysing paper:", e)
        return None
def save_out(oname,response):
    with open(oname, "a", encoding="utf-8") as file:
        file.write(response)
while True:
    print("---MENU---")
    print("0.LOAD DOCUMENT")
    print("1.DISPLAY NOTES")
    print("2.SUMMARIZE NOTES")
    print("3.EXPLAIN NOTES")
    print("4.GENERATE QUIZ")
    print("5.Ask a question")
    print("6.GENERATE FLASHCARDS")
    print("7.GENERATE MINDMAP")
    print("8.ANALYSE PAPER")
    print("9.EXIT")
    try:
        choice=int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice==0:
        fname=input("Enter the filename: ")
        try:
            notes=load_doc(fname)
        except FileNotFoundError:
            print("File not found.")
        except ValueError as e:
            print(e)
    elif choice==1:
        print("---Notes---")
        print(notes)
    elif choice==2:
         result=summarize_notes(notes)
         save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\summary.txt", result.text)
    elif choice==3:
        result=explain(notes)
        save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\explain.txt", result.text)
    elif choice==4:
        result=generate_quiz(notes)
        save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\quiz.txt", result.text)
    elif choice==5:
        result=ask_qn(notes)
        save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\question.txt", result.text)
    elif choice==6:
        result=gen_fcards(notes)
        save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\flashcards.txt", result.text)
    elif choice==7:
        result=gen_mindmap(notes)
        save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\mindmap.txt", result.text)
    elif choice==8:
        result=analyse_paper(notes)
        save_out(r"C:\Users\admin\OneDrive\Desktop\projects\research-assistant\output\paper_analysis.txt", result.text)
    elif choice==9:
        print("exiting")
        break
    else:
        print("Invalid choice. Please try again.")
    

