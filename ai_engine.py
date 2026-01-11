import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def analyze_profile(student_profile, job_description):
    # Ensure API Key is present
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY not found in environment variables."
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-flash-latest")

    # Structured Prompt for Professional Output
    prompt = f"""
    You are a professional ATS (Applicant Tracking System) Expert and Career Coach.
    Analyze the student profile against the Internship JD.

    STUDENT PROFILE:
    {student_profile}

    INTERNSHIP DESCRIPTION:
    {job_description}

    Provide the response with these specific sections:
    1. ATS & CONFIDENCE SCORE: (Give a % score and a brief justification)
    2. INTERNSHIP MATCH SUMMARY: (A concise summary of their fit)
    3. SKILL GAP EXPLANATION: (List missing technical and soft skills)
    4. SIMPLE RECOMMENDATION: (Provide a clear 'Hire' or 'Train' verdict)
    5. TAILORED RESUME REWRITE: (Rewrite their profile into a professional resume format optimized for this JD)
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Essential Rate Limit (429) Handling
        if "429" in str(e):
             return "⚠️ AI Busy: You hit the free quota limit. Please wait 1 minute and try again."
        return f"Error connecting to AI: {str(e)}"