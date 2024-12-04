import streamlit as st


def run_about_me():
    """Function to run the About Me page."""
    st.subheader("Hello! I'm AWAIZ")


if __name__ == "__main__":
    st.set_page_config(page_title="About Awaiz", layout="wide", initial_sidebar_state="expanded")
    run_about_me()