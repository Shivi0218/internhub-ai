# InternHub AI: Intelligent Resume Matcher

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

### 🔗 [Live Demo Available Here](https://internapp-ai-bw9loguvnykw5oyy2otybt.streamlit.app)

---

##  Project Overview
**InternHub AI** is not just a keyword matcher. It is an AI-powered evaluation engine designed to simulate a human technical recruiter. 

Traditional Application Tracking Systems (ATS) often reject good candidates because they lack exact keywords. This tool uses **Google's Gemini 1.5 Pro/Flash model** to understand the *context* of a candidate's experience and compare it semantically against a Job Description (JD).

###  Key Features
* **Semantic Matching:** Analyzes meaning, not just words (e.g., understands that "sklearn" relates to "Machine Learning").
* **Quantified Fit Score:** Generates a 0-100% match score based on technical alignment.
* **Gap Analysis:** Identifies specific "Missing Skills" that are critical for the role.
* **Actionable Feedback:** Acts as a Career Coach, offering specific resume tailoring advice.
---

##  Technical Architecture

###  Tech Stack
* **Frontend:** `Streamlit` (Python) - Chosen for rapid development and interactive data visualization.
* **AI Model:** `Google Gemini 1.5 Flash` - Selected for its high reasoning capability, large context window, and low latency.
* **Logic:** `Prompt Engineering` - Custom "Role-Playing" system prompts to enforce structured JSON output.
* **Deployment:** Streamlit Community Cloud (CI/CD connected to GitHub).

---

###  How It Works (The Logic)
1.  **Data Ingestion:** The app captures unstructured text (Skills, Projects, Experience) from the user.
2.  **Context Construction:** It combines the User Profile + Job Description into a single context block.
3.  **Prompt Engineering:** The system sends a strict instruction set to the LLM:
    > *"You are an Expert Technical Recruiter. Analyze this candidate against this JD. Ignore formatting fluff. Focus on proven skills. Return response in structured format."*
4.  **Response Parsing:** The app cleans the AI response and renders it into a user-friendly Dashboard UI.

---

##  How to Run Locally

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

##  Project Structure
```text
internhub-ai/
├── 📄 app.py              # Frontend: Streamlit Dashboard & UI
├── 📄 ai_engine.py        # Backend: Gemini API Logic & Prompt Engineering
├── 📄 requirements.txt    # Dependencies: List of libraries used
├── 📄 .gitignore          # Security: Ensures .env and venv are not uploaded
└── 📄 README.md           # Documentation: Project overview and setup
```
---

##  Assumptions & Decisions
* **Model Choice:** I selected `gemini-1.5-flash-latest` (or `gemini-pro`) because it offers the best balance of **low latency** and **high reasoning capability** for this specific text-analysis task.
* **Input Format:** The current version assumes text-based input. In a production environment, I would integrate `PyPDF2` to parse PDF resumes directly.
* **Scoring Logic:** The score is AI-generated based on semantic relevance, not a deterministic algorithm. This mimics the subjective nature of human hiring.

---
##  Future Improvements
* **Document Parsing:** Integrate `PyPDF2` or `python-docx` to allow users to upload PDF/Word resumes directly, removing the need for manual copy-pasting.
* **User Authentication:** Implement **Google/GitHub OAuth** (via Firebase or Streamlit-Authenticator) to allow users to save their profile and history securely.
* **Visual Analytics:** Add interactive charts (using `Plotly` or `Altair`) to track how a user's resume match score improves over time with different edits.
* **Job Market Insights:** Connect to external APIs (like LinkedIn or Indeed) to fetch real-time "Trending Skills" for the specific role being analyzed.
* **Multi-Model Support:** Abstract the AI layer to allow users to switch between **Gemini 1.5**, **GPT-4**, or **Claude 3** for comparative analysis.

---

##  Author
**Shivi Parashar**
* **Role:** AI Engineering Intern Applicant
* **Assignment:** InternHub AI 
* **Focus:** LLMs, Python, AI