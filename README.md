# 📚 AI Study Prep Crew

An automated, multi-agent AI system built with **CrewAI** and **Google Gemini** that transforms raw university lecture PDFs into structured study guides and tailored practice exams. 

## 🚀 Overview

This project orchestrates a team of specialized AI agents working sequentially to process educational materials. Instead of manually reading dense academic texts, this system automates the study preparation pipeline.

### The AI Crew:
1. **The Researcher:** Ingests the `lecture.pdf`, extracts core academic concepts, and uses search tools to find simplified explanations.
2. **The Synthesizer:** Takes the Researcher's raw data and formats it into clean, highly structured Markdown study notes (`lecture_notes.md`).
3. **The Examiner:** Reviews the newly created study guide and generates a 10-question practice exam with an answer key (`practice_exam.md`), strictly testing only the provided material.

## 🛠️ Technology Stack
* **Framework:** [CrewAI](https://www.crewai.com/)
* **LLM Provider:** Google Gemini
* **Vector Database:** ChromaDB (via `embedchain`)
* **Tools:** `PDFSearchTool` (RAG), `DuckDuckGoSearchRun` (Web Search)
* **Language:** Python 3.12+

## ⚙️ Setup & Installation

### Prerequisites
* Python 3.12 or higher.
* *Windows Users:* Ensure you have the [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe) installed to run the local ChromaDB vector database.

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR-USERNAME/study-prep-crew.git](https://github.com/YOUR-USERNAME/study-prep-crew.git)
cd study-prep-crew
