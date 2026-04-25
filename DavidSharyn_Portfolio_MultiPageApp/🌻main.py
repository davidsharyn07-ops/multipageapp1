import streamlit as st

main = st.Page("🌻main.py", default=True)
Home = st.Page("Pages/1 👩🏻‍💻Home.py")
About = st.Page("Pages/2 👩🏻‍💼About.py")
SKills= st.Page("Pages/3 🤓Skills.py")
Projects = st.Page("Pages/4 💻Projects.py")
Contact = st.Page("Pages/5 💌Contact.py")

pg =  st.navigation([main, Home , About , SKills , Projects , Contact])
pg.run()

st.title("🌻This is my Portfolio")
st.markdown("""
Take an insight of my innovation hub!

guide side bar to know me more:
- 👩🏻‍💻Home
- 👩🏻‍💼About
- 🤓SKills
- 💻Projects
- 💌Contact
""")

st.info("This app shows my skills and information about python and others.")

