from crewai import Agent
from tools import yt_tool
# Create Senior Blog Content Researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal="ge the relevant Video content for the topic{topic} from Yt channel",
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
       
    ),
    tools=[],
    allow_delegation=True
)

# Creting a senior blog writer agent with YT tools

blog_writer=Agent(
        role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)