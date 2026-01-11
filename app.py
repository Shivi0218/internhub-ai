import streamlit as st
from ai_engine import analyze_profile
import pdfplumber

# 1. Page Setup
st.set_page_config(page_title="InternHub AI", page_icon="🎓", layout="wide")

# 2. Professional Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0E1117; }
    
    .main-title {
        background: linear-gradient(90deg, #FF512F, #DD2476);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800; font-size: 3.2rem; text-align: center;
    }
    
    /* Premium Button */
    div.stButton > button {
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%) !important;
        color: white !important; border: none !important;
        border-radius: 8px !important; height: 3.5rem !important;
        width: 100%; font-weight: 700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">InternHub AI</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; opacity:0.7;">ATS-Optimized Resume Analysis & Strategy</p>', unsafe_allow_html=True)
st.markdown("---")

# 3. Dual-Column Input
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### Candidate Profile")
    with st.container(border=True):
        u_skills = st.text_area("Skills", placeholder="e.g. Python, SQL, NLP", height=80)
        u_interests = st.text_area("Interests", placeholder="e.g. Machine Learning, Fintech", height=80)
        u_exp = st.text_area("Projects & Experience", placeholder="Describe your background...", height=150)
        student_data = f"Skills: {u_skills}\nInterests: {u_interests}\nExperience: {u_exp}"

with col2:
    st.markdown("### Job Description")
    with st.container(border=True):
        role_title = st.text_input("Role Title", placeholder="e.g. Data Science Intern")
        
        # RESTRICTION: One JD option either Text or PDF
        jd_toggle = st.toggle("Upload PDF instead of Pasting", value=False)
        
        final_jd = ""
        if not jd_toggle:
            final_jd = st.text_area("Paste JD Content", height=230)
        else:
            uploaded_file = st.file_uploader("Upload JD PDF", type=["pdf"])
            if uploaded_file:
                try:
                    with pdfplumber.open(uploaded_file) as pdf:
                        pages = [page.extract_text() for page in pdf.pages]
                        final_jd = "\n".join(filter(None, pages))
                    st.success(f"Loaded PDF: {uploaded_file.name}")
                except Exception as e:
                    st.error("Error reading PDF. Please ensure it is a valid text-based PDF.")

# 4. Action and Output
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Generate Match Analysis & Tailored Resume"):
    if not u_skills or not final_jd:
        st.error("Incomplete Data: Please provide both your skills and the job description.")
    else:
        with st.status("AI Analyzing Data...", expanded=True) as status:
            full_jd_input = f"Role: {role_title}\nJD: {final_jd}"
            report = analyze_profile(student_data, full_jd_input)
            status.update(label="Analysis Complete", state="complete", expanded=False)

        # Handling Results
        if "⚠️ AI Busy" in report:
            st.warning(report)
        else:
            st.markdown("## Career Optimization Report")
            with st.container(border=True):
                st.markdown(report)
                
                # Download Option
                st.download_button(
                    label="Download Report & Resume",
                    data=report,
                    file_name=f"{role_title.replace(' ', '_')}_Report.txt",
                    mime="text/plain"
                )