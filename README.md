#  InternHub AI: Intelligent Resume Matcher

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

### 🔗 [Live Demo Available Here](https://internhub-ai-shivi0218.streamlit.app)

---

##  Project Overview
**InternHub AI** is an AI-powered evaluation engine designed to simulate a human technical recruiter. Unlike traditional Applicant Tracking Systems (ATS) that rely on rigid keyword matching, this tool uses **Google's Gemini 1.5 Flash model** to understand the *context* of a candidate's experience and compare it semantically against a Job Description (JD).

###  Key Features
* **PDF Support:** Users can upload Job Descriptions directly as PDF files (processed via `pdfplumber`).
* **Semantic Matching:** Analyzes meaning rather than just counting words (e.g., understanding that "CNNs" implies "Deep Learning").
* **Quantified Fit Score:** Generates a 0-100% match score based on technical alignment.
* **Tailored Resume Rewrites:** The AI rewrites the candidate's profile into a professional format optimized for the specific JD.
* **Downloadable Reports:** Users can download the full analysis and rewritten resume as a text file.

---

## Technical Architecture

### Tech Stack
* **Frontend:** `Streamlit` (Python) - Interactive dashboard with real-time status updates and file handling.
* **PDF Processing:** `pdfplumber` - For robust extraction of text from uploaded Job Description PDFs.
* **AI Model:** `Google Gemini 1.5 Flash` (via `google-genai` SDK) - Selected for its high reasoning capability and large context window.
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
* **Model Choice:** I selected `gemini-1.5-flash` because it offers the optimal balance of **low latency** (speed) and **reasoning accuracy** for real-time text analysis.
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