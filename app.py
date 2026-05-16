import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Habeebullah's App", page_icon="🚀")

# 2. The App Header
st.title("Welcome to My Professional App")
st.subheader("Created at the University of Lagos")

# 3. User Interaction
name = st.text_input("Enter your name to get started:")

service = st.selectbox(
    "What can I help you with today?",
    ["App Development", "Data Analysis", "Digital Design", "Just saying Hi!"]
)

# 4. The Action Button
if st.button("Launch App"):
    if name:
        st.success(f"Welcome, {name}! You have selected: {service}")
        st.balloons() 
    else:
        st.warning("Please enter your name first!")

# 5. Sidebar
st.sidebar.title("App Settings")
st.sidebar.info("This app is currently in Development Mode.")