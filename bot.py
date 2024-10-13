from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

local_llm = "llama3.1:8b"
llm = ChatOllama(model=local_llm, keep_alive='20m', max_tokens=1024, temperature=0.2, base_url='http://ollama:11434')
template = """You are a meeting bot, act like a assistant and help with the query.
Query: {question}"""

prompt = ChatPromptTemplate.from_template(template)

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        question = turn_context.activity.text
        formatted_prompt = prompt.format(question=question)
        response = llm.invoke(formatted_prompt)
        await turn_context.send_activity(f"'{ response.content }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
