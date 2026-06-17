from crewai import Task
from agents import researcher, synthesizer, examiner

# Task 1: For the Researcher
research_task = Task(
    description="Read the provided 'lecture.pdf'. Extract the core concepts, then search the web to find simplified explanations and real-world examples for those complex topics.",
    expected_output="A raw text summary combining the core concepts from the PDF with the simplified web explanations.",
    agent=researcher
)

# Task 2: For the Synthesizer
synthesize_notes_task = Task(
    description="Take the researcher's raw data and create a detailed study guide.",
    expected_output="A well-structured study guide with clear headings and bullet points.",
    agent=synthesizer,
    output_file="lecture_notes.md" 
)

# Task 3: For the Examiner
create_exam_task = Task(
    description="Review the lecture notes and create a 10-question practice exam with answers.",
    expected_output="A practice exam document followed by an answer key.",
    agent=examiner,
    output_file="practice_exam.md" 
)