from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

greeting_agent = Agent(
    name="Greeting Agent",
    instructions="You are a greeting agent, your task is to say Waalaiku-Alssalam, when someone says Assalamualaikum or anything similar.",
    model=model,
    
)


user_input = input("Enter a message: ")


agent_result = Runner.run_sync(greeting_agent, user_input)

print(agent_result.final_output)