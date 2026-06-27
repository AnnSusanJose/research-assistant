from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])
print("chatbot loading.. performes on sample.txt")
with open("sample.txt", "r") as file:
        content = file.read()
def load_notes():
    print(content)
def summarize_notes(content):
    prompt = f"""
    Summarize the following notes in 5 bullet points:

    {content}
    """
    res=chat.send_message(prompt)
    print("Summary: ",res.text)
    return res
def explain(content):
    prompt = f"""
    Explain the following notes in simple terms:
    
    {content}
    """
    res=chat.send_message(prompt)
    print("Explanation: ",res.text)
    return res
def generate_quiz(content):
    prompt = f"""
    Generate a quiz based on the following notes. Include 5 multiple-choice questions with 4 options each and provide the correct answer for each question:

    {content}
    """
    res=chat.send_message(prompt)
    print("Quiz: ",res.text)
    return res
def save_out(response):
    with open("output.txt", "a") as file:
        file.write(response)
while True:
    print("---MENU---")
    print("0.LOAD NOTES")
    print("1.SUMMARIZE NOTES")
    print("2.EXPLAIN NOTES")
    print("3.GENERATE QUIZ")
    print("4.EXIT")
    try:
        choice=int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice==0:
        load_notes()
    elif choice==1:
         result=summarize_notes(content)
         save_out(result.text)
    elif choice==2:
        result=explain(content)
        save_out(result.text)
    elif choice==3:
        result=generate_quiz(content)
        save_out(result.text)
    elif choice==4:
        print("exiting")
        break
    else:
        print("Invalid choice. Please try again.")
    

