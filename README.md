#  InternHub AI: Intelligent Resume Matcher

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

### 🔗 [Live Demo Available Here](https://internapp-ai-bw9loguvnykw5oyy2otybt.streamlit.app/)

---

##  Project Overview
**InternHub AI** is an AI-powered evaluation engine designed to simulate a human technical recruiter. Unlike traditional Applicant Tracking Systems (ATS) that rely on rigid keyword matching, this tool uses **Google's Gemini Flash model** to understand the *context* of a candidate's experience and compare it semantically against a Job Description (JD).

### Key Features
* **Adaptive Premium UI:** A glassmorphic dashboard that automatically adjusts for **Light and Dark modes** for a seamless user experience.
* **Smart PDF Parsing:** Robust extraction of job requirements from PDF files using `pdfplumber`.
* **Chain-of-Thought Analysis:** Advanced AI logic that evaluates skill "depth" and "evidence" rather than just existence.
* **Tailored Career Strategy:** Provides optimized resume summaries and specific project recommendations to fill identified gaps.
* **One-Click Export:** Download your full gap analysis and rewritten resume content as a professional text report.

---

## Technical Architecture

### Tech Stack
* **Core:** `Python 3.11+`
* **Frontend:** `Streamlit` (Python) - Interactive dashboard with real-time status updates and file handling.
* **PDF Processing:** `pdfplumber` - For robust extraction of text from uploaded Job Description PDFs.
* **AI Model:** `Google Gemini Flash` - Selected for its high reasoning capability and large context window.
* **Environment:** `python-dotenv` - For secure API key management.
* **Deployment:** Streamlit Community Cloud (CI/CD connected to GitHub).

---

## How It Works (The Logic)
1.  **Data Ingestion:** The app captures unstructured text (Skills, Projects, Experience) from the user and supports both Text and PDF inputs for Job Descriptions.
2.  **Context Construction:** It combines the Student Profile and the Job Description into a single prompt context block.
3.  **Prompt Engineering:** A custom "Role-Playing" system prompt instructs the Gemini LLM to act as an **"Expert Technical Recruiter."**
    * *Instruction:* "Analyze this candidate against this JD. Ignore formatting fluff. Focus on proven skills. Return response in structured Markdown format."
4.  **Response Parsing:** The app renders the AI's analysis into a structured UI and provides a downloadable text file option.

---

## How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Shivi0218/internhub-ai.git](https://github.com/Shivi0218/internhub-ai.git)
    cd internhub-ai
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up API Key**
    Create a `.env` file in the root directory and add your Google Gemini API key:
    ```bash
    GEMINI_API_KEY="your_api_key_here"
    ```

5.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## Project Structure
```text
internhub-ai/
├── 📄 app.py              # Frontend: Streamlit Dashboard & PDF Logic
├── 📄 ai_engine.py        # Backend: Gemini API Logic & Prompt Engineering
├── 📄 requirements.txt    # Dependencies: List of libraries used
├── 📄 .gitignore          # Security: Ensures .env and venv are not uploaded
└── 📄 README.md           # Documentation: Project overview and setup
```
---

## Assumptions Made
* **Model Choice:** I selected `gemini-flash` because it offers the optimal balance of **low latency** (speed) and **reasoning accuracy** for real-time text analysis.
* **PDF Handling:** The current PDF parser (`pdfplumber`) assumes the uploaded JDs are text-based PDFs, not scanned images.
* **Scoring Logic:** The match score is AI-generated based on semantic relevance rather than a deterministic keyword count algorithm. This mimics the subjective but expert nature of human hiring.
* **Data Privacy:** User data is processed in-session and is not stored persistently in a database for this prototype.

---

## Future Improvements
* **OCR Integration:** Add `pytesseract` to handle scanned/image-based PDF uploads.
* **User Authentication:** Implement **Google/GitHub OAuth** (via Firebase) to allow users to save their profile history.
* **Visual Analytics:** Add interactive charts (using `Plotly`) to track how a user's resume match score improves over time.
* **Job Market Insights:** Connect to external APIs (like LinkedIn) to fetch real-time "Trending Skills" for the specific role.
* **Multi-Model Support:** Abstract the AI layer to allow users to switch between Gemini, GPT-4, or Claude for comparative analysis.

---

##  Author
**Shivi Parashar**
* **Role:** AI Engineering Intern Applicant
* **University:** Bennett University  
* **Batch:** 2026
* **Enrollment:** E22CSEU0401