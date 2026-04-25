import streamlit as st

st.title("🤓Skills")

st.subheader("My Skills")
basic_skills = {
    "Communication": 90,
    "Teamwork": 85,
    "Problem-solving": 80,
    "Adaptability": 90,
    "Time Management": 80
}

for skill, percent in basic_skills.items():
    st.write(f"{skill} ({percent}%)")
    st.progress(percent / 100)

st.subheader("Technical Skills")
technical_skills = {
    "Python": 80,
    "JavaScript": 75,
    "SQL": 85
}

for skill, percent in technical_skills.items():
    st.write(f"{skill} ({percent}%)")
    st.progress(percent / 100)

st.subheader("Design Skills")
design_skills = {
    "UI/UX Design": 70,
    "Graphic Design": 90
}

for design, percent in design_skills.items():
    st.write(f"{design} ({percent}%)")
    st.progress(percent / 100)
    
st.subheader("Tools & Technologies")
st.write("""
- Git
- Docker
- Streamlit
- Figma
- VS Code
""")