import streamlit as st

st.title("👩🏻‍💼About")

st.image("Pages/sharyn.jpg", width=200, caption="Sharyn")
st.write("""
Helllo, Im Sharyn 3rd Year college Student. I am a passionate technology enthusiast with a focus on making and 
learning codes through innovative solutions.
I thrive on challenges and continuously seek to enhance my skills.
""")

st.subheader("Some info about me")
st.write("**Birthday:** July 26, 2005")
st.write("**Location:** Capsay, Aroroy, Masbate")
st.write("**Languages Spoken:** Filipino, English")

st.subheader("Hobbies")
hobbies = [
    "👩🏻‍🍳 Cooking",
    "📚 Reading Fiction Novels",
    "👀 Watching Horror Movies",
    "🖍️ Making Design Deco",
    "👩🏻‍🌾 Gardening",
]

for hobby in hobbies:
    st.write(hobby)

st.subheader("Education")
st.write("- BACHERLOR OF SCIENCE IN COMPUTER SCIENCE")
st.write("- Specialized in making codes")

st.subheader("Goals")
st.write("""
- To become a Full Stack Developer with expertise in cloud solutions.
- To contribute towards impactful technology initiatives globally.
""")