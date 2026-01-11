# InternHub AI: Intelligent Resume Matcher

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini AI](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

### 🔗 [Live Demo Available Here](https://internhub-ai-shivi0218.streamlit.app)

---

## 📖 Overview
**InternHub AI** is a semantic analysis tool designed to bridge the gap between students and internships. Unlike traditional ATS systems that rely on simple keyword matching, this tool uses **Google's Gemini 1.5 Flash LLM** to "read" a resume like a human recruiter would.

It analyzes the *context* of a student's skills and compares it against the specific requirements of a Job Description (JD) to provide:
1.  **📊 Match Score:** A quantified percentage of fit.
2.  **⚠️ Skill Gap Analysis:** Identification of critical missing tools or concepts.
3.  **📝 Resume Optimization:** Actionable, specific advice to tailor the resume for that specific role.

---

## 🛠️ Tech Stack
* **Frontend:** Python (Streamlit) for a clean, responsive "SaaS-style" dashboard.
* **AI Engine:** Google Gemini (Generative AI SDK) for reasoning and text analysis.
* **Environment:** `python-dotenv` for secure API key management.
* **Version Control:** Git & GitHub.

---

## 🧠 How It Works (The Logic)
The core value of this project lies in its **System Prompt Design**.

1.  **Data Ingestion:** The app accepts unstructured text inputs for "Student Profile" (Skills, Interests, Experience) and "Target Internship" (Role, JD, Required Skills).
2.  **Prompt Engineering:** I constructed a role-playing system prompt that instructs the LLM to act as an **"Expert Technical Recruiter."**
3.  **Semantic Analysis:** instead of `if "Python" in text`, the AI evaluates if the student's *experience* with Python matches the *depth* required by the JD.
4.  **Graceful Error Handling:** Implemented `try-except` blocks to handle API rate limits and connection timeouts, ensuring a smooth user experience.

---

## 🚀 How to Run Locally

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

## 📝 Assumptions & Decisions
* **Model Choice:** I selected `gemini-1.5-flash-latest` (or `gemini-pro`) because it offers the best balance of **low latency** and **high reasoning capability** for this specific text-analysis task.
* **Input Format:** The current version assumes text-based input. In a production environment, I would integrate `PyPDF2` to parse PDF resumes directly.
* **Scoring Logic:** The score is AI-generated based on semantic relevance, not a deterministic algorithm. This mimics the subjective nature of human hiring.

---

## 👤 Author
**Shivi Parashar**
* **Role:** AI Engineering Intern Applicant
* **Assignment:** InternHub AI Track 2