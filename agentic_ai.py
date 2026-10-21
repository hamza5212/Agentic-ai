import os

from agno.agent import Agent

from agno.models.google import Gemini

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model=Gemini(api_key=os.getenv("gemini_api")),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful assistant that can answer questions and provide information.",
        add_datetime_to_context=True

    )


gemini_agent = build_agent()

gemini_agent.print_response("is it safe to travel to the US right today?")

