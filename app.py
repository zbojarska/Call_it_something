import random
import streamlit as st
from ai_utils import AIWrapper

st.title("Guessing Game")

st.subheader("chuj")

st.write("Rules here")

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

if submitted:
    st.write(f"You submitted: {guess}")
    # Run your calculation or other action here.
    if guess == st.session_state["number"]:
        st.success("Yeah! You did it!")
        st.balloons()
    else:
        st.error("Nah-uh! Try again!")
        st.info(f"Debug info: The number is {st.session_state['number']}")


wrapper = AIWrapper()

with col2:
    wrapper.main()

# Title
# rules
# a random number from 1 to 100 that stays the same
#                                     throughout guesses
# window to input the number
# AI Chat (retain history)
# Clues history window
# numbers guessed window

# let's let out the balloons if someone guesses right at the end