import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def analyze_profile(student_profile, job_description):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    # USE THE EXACT NAME FROM YOUR LIST
    model = genai.GenerativeModel("gemini-flash-latest")

    prompt = f"""
    You are an expert HR Specialist and AI Career Coach. 
    Analyze the following student profile against the internship description.
    
    STUDENT PROFILE:
    {student_profile}

    INTERNSHIP DESCRIPTION:
    {job_description}

    Please provide the following in your response:
    1. Match Percentage (0-100% Score)
    2. Internship Match Summary (How well do they fit?)
    3. Skill Gap Explanation (What specific technical or soft skills are missing?)
    4. Resume Improvement Suggestions (How can they tailor their resume for this specific JD?)
    5. Final Recommendation (Short "Hire" or "Train" recommendation)
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # If rate limit (429) happens, give a clear message
        if "429" in str(e):
             return "⚠️ AI Busy: You hit the free quota limit. Please wait 1 minute and try again."
        return f"Error connecting to AI: {str(e)}"