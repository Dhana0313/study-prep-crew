from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

# Import our team members and assignments from the other files
from agents import researcher, synthesizer, examiner
from tasks import research_task, synthesize_notes_task, create_exam_task

# Build the Crew
study_prep_crew = Crew(
    agents=[researcher, synthesizer, examiner],
    
    # Here is the array you just mentioned! 
    # Because it is sequential, Task 1 must finish before Task 2 starts.
    tasks=[research_task, synthesize_notes_task, create_exam_task],
    
    # We explicitly tell them to work like an assembly line
    process=Process.sequential,
    
    # Turning on verbose lets you watch their "thinking" process in the terminal
    verbose=True 
)

# Start the workflow!
print("Starting the Study Prep Crew... This may take a few minutes. 📚")
result = study_prep_crew.kickoff()

print("All tasks complete! Check your folder for the new PDF/Markdown files.")

# source venv/Scripts/activate