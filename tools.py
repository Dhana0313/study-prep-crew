from crewai_tools import PDFSearchTool, SerperDevTool
from crewai.tools import tool
from fpdf import FPDF
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Built-in PDF Reader
# We specifically point it to the lecture file the student provides
pdf_reader = PDFSearchTool(
    pdf='lecture.pdf',
    config={
        "llm": {
            "provider": "google",
            "config": {"model": "gemini/gemini-1.5-flash"}
        },
        "embedder": {
            "provider": "google",
            "config": {"model": "models/embedding-001"}
        }
    }
)

# 2. Built-in Google Search
google_search = DuckDuckGoSearchRun()

# 3. Custom PDF Generator
@tool("PDF Generator Tool")
def generate_pdf(text: str, filename: str) -> str:
    """Converts a given text block into a cleanly formatted PDF document."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=1)
        
    pdf.output(filename)
    return f"Successfully saved as {filename}"