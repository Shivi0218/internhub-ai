import streamlit as st
from ai_engine import analyze_profile

# 1. Page Configuration
st.set_page_config(page_title="InternHub AI", page_icon="🎓", layout="wide")

# 2. Premium CSS (Adaptive & Beautiful)
st.markdown("""
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Gradient Header Text (Centered) */
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #FF512F, #DD2476);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3.5rem;
        text-align: center;
        padding-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        opacity: 0.8;
        margin-bottom: 20px;
    }

    /* Modern Card Styling */
    .stTextArea, .stTextInput {
        background-color: transparent !important;
    }
    
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* The "Magic" Button */
    .stButton>button {
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%);
        color: white;
        border: none;
        border-radius: 12px;
        height: 4em;
        width: 100%;
        font-weight: 600;
        font-size: 18px;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(221, 36, 118, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(221, 36, 118, 0.6);
    }
    
    /* Subheaders */
    h3 {
        font-weight: 600;
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section (Centered, No Icon)
st.markdown('<div class="gradient-text">InternHub AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle"> Your Personal AI Career Coach</div>', unsafe_allow_html=True)

st.markdown("---")

# 4. Main Split Layout (Profile vs Job)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 👤 Your Profile")
    st.caption("Tell the AI about yourself.")
    
    with st.container():
        skills = st.text_area(" Technical Skills", placeholder="e.g. Python, SQL, React, AWS...", height=120)
        interests = st.text_area(" Interests", placeholder="e.g. AI Agents, Fintech, Data Viz...", height=100)
        experience = st.text_area(" Experience / Projects", placeholder="e.g. Built a weather app using API...", height=150)

with col2:
    st.markdown("### 💼 Target Internship")
    st.caption("Paste the details of the job you want.")
    
    with st.container():
        jd_role = st.text_input("Role Title", placeholder="e.g. AI Engineering Intern")
        jd_skills = st.text_input("Required Skills (from JD)", placeholder="e.g. PyTorch, NLP, Docker")
        jd_desc = st.text_area(" Job Description", placeholder="Paste the full JD text here...", height=300)

# 5. Action Section
st.markdown("---")
analyze_btn = st.button(" ANALYZE MATCH & OPTIMIZE RESUME ")

# 6. Results Display
if analyze_btn:
    if not skills or not jd_desc:
        st.warning(" Please fill in your **Skills** and the **Job Description** above.")
    else:
        # Simple spinner
        with st.spinner("Analyzing..."):
            # Combine Inputs
            full_jd = f"Role: {jd_role}\nRequired Skills: {jd_skills}\nDescription: {jd_desc}"
            student = f"Skills: {skills}\nInterests: {interests}\nExperience: {experience}"

            # Run Logic
            result_text = analyze_profile(student, full_jd)
        
        # Display Results
        st.markdown("###  Analysis Report")
        
        # Using a container for the result to make it stand out
        with st.container():
            st.markdown(result_text)