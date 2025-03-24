import chainlit as ch


@ch.on_message
async def main(message: ch.Message):

    response = f"you said: {message.content}"

    await ch.Message(content=response).send()