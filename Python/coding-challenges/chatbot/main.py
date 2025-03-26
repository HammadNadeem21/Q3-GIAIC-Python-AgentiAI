# for get envirnment variable
import os

import chainlit as ch
import google.generativeai as genai

# for get env file
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

@ch.on_chat_start
async def handle_chat_start():
    await ch.Message(content="Hello, How can I help you?").send()


@ch.on_message
async def handle_message(message:ch.Message):   
    prompt = message.content

    response = model.generate_content(prompt)

    response_text = response.text if hasattr(response, "text") else ""

    await ch.Message(content=response_text).send()

    