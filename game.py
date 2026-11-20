import random
import streamlit as st
from ai_utils import AIWrapper

st.title("Guessing Game")

st.subheader("How to play")

st.markdown("""
:blue-background[Your goal:] Ask creative questions to get clues about the number generated for you between 1 and 100 & guess it.
"""
)
st.markdown("""
:blue-background[Rules:] You are allowed to ask the AI chat for clues, 
but there's a catch! The clues can only take a form of questions putting the number in a specific context.
For example you're allowed to ask: :blue["Would it be possible to have this many children?"] or :blue["If this number was 
my age, would I be allowed to drive?"], or :blue["If I would weight this much, would I be considered skinny?"], and so 
on. Any questions about the number that are not putting it in a specific context will be rejected by the AI chat.
"""
)

st.info("Turn on your imagination and try to come up with creative questions that will help you guess the number! Good luck!")

col1, col2 = st.columns([2, 1])
with col1:
    # create a new random number if we don't have one yet
    if "number" not in st.session_state:
        st.session_state["number"] = random.randint(1,100)

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

# create an empty list for colors (for the scatter chart in stats page) if we don't have one yet:
if "colors" not in st.session_state:
    st.session_state["colors"] = []

if st.button("New Game"):
    st.session_state["number"] = random.randint(1,100)
    st.session_state["guess_history"] = []
    st.session_state["colors"] = []
    # also clear the clues history!!!
    # ...

if submitted:
    st.write(f"You submitted: {guess}")
    # Add the guess to the guess history:
    st.session_state["guess_history"].append(guess)
    # Run your calculation or other action here.
    if guess == st.session_state["number"]:
        st.success("Yeah! You did it!")
        st.session_state['colors'].append("#008000")
        st.balloons()
    else:
        st.error("Nah-uh! Try again!")
        st.session_state['colors'].append("#FF0000")
        st.write(f"Guess history: {st.session_state['guess_history']}")
        # st.info(f"Debug info: The number is {st.session_state['number']}")



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