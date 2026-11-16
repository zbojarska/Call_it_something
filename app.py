import random
import streamlit as st
from ai_utils import AIWrapper

st.title("Guessing Game")

st.subheader("chuj")

st.write("Rules here")
# also maybe markdown for that?
# st.markdown("""
#This is the text for page 1.
## Use markdown in Streamlit.
#Just use `markdown`syntax for longer texts.
#""")

col1, col2 = st.columns([2, 1])
with col1:
    # create a new random number if we don't have one yet
    if "number" not in st.session_state:
        st.session_state["number"] = random.randint(1,100)
        st.info("New number generated!")

    with st.form("number_form"):
        guess = st.number_input(
            "Enter a number",
            min_value=0,
            max_value=100,
            value=10,
            step=1,
        )
        submitted = st.form_submit_button("Submit")

# create an empty list for guess history if we don't have one yet
if "guess_history" not in st.session_state:
    st.session_state["guess_history"] = []

if st.button("New Game"):
    st.session_state["number"] = random.randint(1,100)
    st.session_state["guess_history"] = []
    # also clear the clues history!!!
    # ...

if submitted:
    st.write(f"You submitted: {guess}")
    # Run your calculation or other action here.
    if guess == st.session_state["number"]:
        st.success("Yeah! You did it!")
        st.balloons()
    else:
        st.error("Nah-uh! Try again!")
        # Add the guess to the guess history:
        st.session_state["guess_history"].append(guess)
        st.write(f"Guess history: {st.session_state['guess_history']}")
        st.info(f"Debug info: The number is {st.session_state['number']}")



with col2:
    if "ai_wrapper" not in st.session_state:
        st.session_state.ai_wrapper = AIWrapper()

    wrapper = st.session_state.ai_wrapper
    wrapper.main(st.session_state["number"])

# Title
# rules
# a random number from 1 to 100 that stays the same
#                                     throughout guesses
# window to input the number
# AI Chat (retain history)
# Clues history window
# numbers guessed window
# stats page
# let's let out the balloons if someone guesses right at the end