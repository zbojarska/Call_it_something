import streamlit as st

st.header("Stats")

st.write(f"Guess history: {st.session_state['guess_history']}")

guess_data = {
    "guessing_attempt": list(range(1, len(st.session_state['guess_history']) + 1)),
    "guess": st.session_state['guess_history']
    }

st.scatter_chart(data=guess_data, x="guessing_attempt", y="guess", x_label="Guessing Attempt", y_label="Your Guess", color=None, size=None, width="stretch", height="content", use_container_width=None, alt=None)


# add the clues history
# ...


# display guess history, number of guesses it took
# to win, clues history, number of clues.




if st.button("Go to the Game"):
    st.switch_page("app.py")
