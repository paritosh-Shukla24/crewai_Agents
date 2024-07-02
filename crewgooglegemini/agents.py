from crewai import Agent
import os
from dotenv import load_dotenv
load_dotenv()
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
## call the gemini models

llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",verbose=True,temperature=0.5,google_api_key=os.getenv("google_api_key")
)

news_researcher = Agent( 
    role="Senior Researcher",
    goal="Uncover ground Breaking Technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."        
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a write agent with custom tools responsible in writing news BlockingIOError
news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
