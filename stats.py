import streamlit as st
import altair as alt
import pandas as pd

st.header("Stats")

guess_data = {
    "guessing_attempt": list(range(1, len(st.session_state['guess_history']) + 1)),
    "guess": st.session_state['guess_history'],
    "point_color": st.session_state['colors']
}

# We tried a streamlit scatter chart first but run into problems with the color names for the
# points (turns out that scatter charts in streamlit treat string values as category labels
# (and NOT literal colors, like I wanted), sorts them in alphabetical order and applies its
# own default theme pallette. So green always came before red, which means wrong guesses were
# displayed as green and correct as red - the opposite of what we wanted). The only robust
# solution (or rather the only one I came up with, I'm sure there's more) that wasn't a
# walk-around, was to use altair.

guess_alt = pd.DataFrame(guess_data)

guess_history_str = ", ".join(str(guess) for guess in st.session_state['guess_history'])

chart = alt.Chart(guess_alt).mark_circle(size=100).encode(
    x = alt.X("guessing_attempt:Q", title="Guessing Attempt",  axis=alt.Axis(tickMinStep=1, format="d")),
    y = alt.Y("guess:Q", title="Your Guess", axis=alt.Axis(tickMinStep=1, format="d"), scale=alt.Scale(domain=[1, 100])),
    color = alt.Color("point_color:N", scale=None)
).properties(
    title = f"Your Guess History: {guess_history_str}",
)

st.altair_chart(chart, use_container_width=True)

if "#008000" in st.session_state['colors']:
    st.success(f"You won in {len(st.session_state['guess_history'])} guesses!")

with st.expander("Hint history", expanded=True):
    for i, hint in enumerate(reversed(st.session_state.ai_wrapper.hint_history), start=1):
        with st.container(border=True):
            st.badge(
                "Good question!" if hint["valid"] else "Bad question :(",
                color="green" if hint["valid"] else "red"
            )
            st.markdown(
                f"**Q:** {hint['question']}  \n\n"
                f"**A:** {hint['answer']}"
            )

# add the clues history, number of clues
# add the sztrzałka czasu, na której widać kiedy był guess a kiedy clue


if st.button("Go to the Game"):
    st.switch_page("game.py")
