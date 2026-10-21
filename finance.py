import os

from agno.agent import Agent

from agno.models.google import Gemini

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools


from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Gemini(api_key=os.getenv("gemini_api")),
        tools=[ YFinanceTools(),DuckDuckGoTools() ],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock",
        instructions=["use given tools whenever possible. Format your response using markdown and use tables to display data where possible."],
        debug=True
    )


agent = build_agent()
agent.print_response("share the microsoft stock price in INR and show the current exchange rate.")

