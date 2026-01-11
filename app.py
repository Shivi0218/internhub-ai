import streamlit as st
import pdfplumber
from ai_engine import analyze_profile

# 1. Page Configuration
st.set_page_config(
    page_title="InternHub AI | Career Optimizer", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Adaptive Premium CSS (Works for both Light and Dark Mode)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    /* Global Font reset */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated Gradient Title */
    .main-title {
        background: linear-gradient(-45deg, #FF512F, #DD2476, #FF512F, #DD2476);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800; 
        font-size: clamp(2rem, 8vw, 4rem); 
        text-align: center;
        margin-bottom: 0px;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .subtitle {
        text-align: center;
        font-weight: 300;
        letter-spacing: 2px;
        opacity: 0.7;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    /* Adaptive Glassmorphic Containers */
    [data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlock"] {
        background: var(--background-color);
        background-color: rgba(128, 128, 128, 0.05) !important;
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 15px;
        padding: 25px !important;
        backdrop-filter: blur(10px);
    }

    /* Adaptive Input Fields */
    .stTextArea textarea, .stTextInput input {
        border: 1px solid rgba(128, 128, 128, 0.2) !important;
        border-radius: 10px !important;
    }
    
    /* Premium Button Optimization */
    div.stButton > button {
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        height: 3.5rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(221, 36, 118, 0.3);
        margin-top: 10px;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(221, 36, 118, 0.5);
    }

    /* Footer opacity */
    .footer-text {
        text-align: center; 
        opacity: 0.5; 
        font-size: 0.8rem;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.markdown('<div class="main-title">InternHub AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-POWERED CAREER OPTIMIZATION ENGINE</div>', unsafe_allow_html=True)

# 4. Main Interface
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 👤 Candidate Profile")
    with st.container():
        u_skills = st.text_area("Technical Skills", placeholder="e.g. Python, TensorFlow, SQL", height=90)
        u_interests = st.text_area("Interests", placeholder="e.g. Computer Vision, Algorithmic Trading", height=90)
        u_exp = st.text_area("Background & Projects", placeholder="Tell us about your internship or projects...", height=180)
        student_data = f"Skills: {u_skills}\nInterests: {u_interests}\nExperience: {u_exp}"

with col2:
    st.markdown("### 🎯 Target Opportunity")
    with st.container():
        role_title = st.text_input("Internship Role", placeholder="e.g. AI Engineering Intern")
        
        st.write("") # Spacer
        jd_toggle = st.toggle("📂 Use PDF Job Description", value=False)
        
        final_jd = ""
        if not jd_toggle:
            final_jd = st.text_area("📄 Paste JD Content", placeholder="Paste the job requirements here...", height=255)
        else:
            uploaded_file = st.file_uploader("Upload JD PDF", type=["pdf"])
            if uploaded_file:
                try:
                    with pdfplumber.open(uploaded_file) as pdf:
                        pages = [page.extract_text() for page in pdf.pages]
                        final_jd = "\n".join(filter(None, pages))
                    st.success(f"✅ Successfully extracted text from {uploaded_file.name}")
                except Exception as e:
                    st.error("Failed to parse PDF. Please ensure it's not a scanned image.")

# 5. The Analysis Action
st.markdown("---")
if st.button("INITIATE ANALYSIS"):
    if not u_skills or not final_jd:
        st.error("Missing Information: Please provide both your profile details and the target JD.")
    else:
        with st.status("AI Engine Processing...", expanded=True) as status:
            full_jd_input = f"Role: {role_title}\nJD: {final_jd}"
            report = analyze_profile(student_data, full_jd_input)
            status.update(label="✅ Analysis Complete!", state="complete", expanded=False)

        if "⚠️ AI Busy" in report:
            st.warning(report)
        else:
            st.markdown("## Strategic Optimization Report")
            with st.container():
                st.markdown(report)
                
                st.write("---")
                st.download_button(
                    label="📥 SAVE REPORT & RESUME AS .TXT",
                    data=report,
                    file_name=f"{role_title.replace(' ', '_')}_Analysis.txt",
                    mime="text/plain"
                )

# 6. Footer
st.markdown("<p class='footer-text'>Built for InternHub AI </p>", unsafe_allow_html=True)