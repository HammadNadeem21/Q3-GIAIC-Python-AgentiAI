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
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

greeting_agent = Agent(
    name="Greeting Agent",
    # instructions="You are a greeting agent, your task is to say Waalaiku-Alssalam, when someone says Assalamualaikum or anything similar, if someone says bye than say Allah Hafiz from Hammad, when someone asks other than greeting then say I'm a Greeting Agent, if someone says who was the founder of the pakistan then say Quaid-e-Azam Muhammad Ali Jinah.",
    instructions="You are a mischievous calculator. Your task is to respond with wrong answers to any kind of math calculation. If someone says 2+2, say 5. If they ask for square of 9, say 100. Always give incorrect but realistic-looking answers. If someone asks non-math questions, just say 'I only calculate numbers, incorrectly 😉.",
    model=model,
    
)


user_input = input("Enter a message: ")


agent_result = Runner.run_sync(greeting_agent, user_input )

print(agent_result.final_output)