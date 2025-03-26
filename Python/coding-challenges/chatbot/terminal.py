import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# get envirnment veriable from env file
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:

    user_input = input("Enter your message or quite: ")

    if user_input == "quite":
        print("Thank you for chatting")
        break

    response = model.generate_content(user_input)



    print(response.text)
