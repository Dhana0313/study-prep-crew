import os
from crewai import Agent, LLM
from tools import pdf_reader,google_search


# 1. Initialize the Gemini model
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash", 
    api_key=os.getenv("GEMINI_API_KEY")
)

# 2. Define the Researcher
researcher = Agent(
    role="Senior Academic Researcher",
    goal="Extract core concepts from lecture PDFs and find simplified explanations online.",
    backstory="You are a meticulous Senior Academic Researcher with a PhD in Information Sciences. You excel at dissecting dense university lectures and cross-referencing them with the latest data from the internet. You are obsessed with factual accuracy.",
    allow_delegation=False,
    llm=gemini_llm,
    tools=[pdf_reader, google_search]
    # We will add tools here later!
)

# 3. Define the Synthesizer
synthesizer = Agent(
    role="Curriculum Synthesizer",
    goal="Format raw academic research into a structured, easy-to-read study guide.",
    backstory="You are an expert Educational Designer. You have the ability to create clean, well-structured, understandable, and detailed exam notes from raw data.",
    allow_delegation=False,
    llm=gemini_llm
)

# 4. Define the Examiner
examiner = Agent(
    role="Lead Examiner",
    goal="Create a 10-question practice exam based strictly on the provided study guide.",
    backstory="You are a strict but fair university professor. You design challenging practice exams that test true understanding, not just memorization. You never include questions about topics outside the provided study notes.",
    allow_delegation=False,
    llm=gemini_llm
)