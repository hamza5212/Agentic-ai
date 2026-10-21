
import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat

load_dotenv()


eng_agent = Agent(
    name="English Agent",
    role="Answer the user's question in English."
)


hindi_agent = Agent(
    name="Hindi Agent",
    role="Answer the user's question in Hindi using Devanagari script."
)


chi_agent = Agent(
    name="Chinese Agent",
    role="Answer the user's question in Simplified Chinese."
)


team_leader = Team(
    name="Multilingual Team",
    members=[eng_agent, hindi_agent, chi_agent],
    model=OpenAIChat(
        id="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    ),
    description="A team that answers every question in English, Hindi, and Chinese.",
    instructions=[
        "Delegate the same original question to every member.",
        "All three members must answer every question.",
        "Do not skip any member or choose only one agent.",
        "Present all three answers, clearly labeled by language."
    ],
    delegate_to_all_members=True,
    markdown=True,
    show_members_responses=True
)

if __name__ == "__main__":
    team_leader.print_response("What is the capital of India?")
