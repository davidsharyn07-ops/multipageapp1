import streamlit as st

st.title("💌Contact")

with st.form("contact_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    message = st.text_area("Your Message")
    
    submit = st.form_submit_button("Send Message")
    
    if submit:
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been sent successfully.")
        else:
            st.error("Please fill in all fields before sending.")

st.markdown("---")
st.write("📍 **Location:** Aroroy, Bicol, Philippines")
st.write("🔗 [GitHub](https://github.com) | 💻 [Facebook](https://facebook.com)")