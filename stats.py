import streamlit as st
import altair as alt
import pandas as pd

st.header("Stats")

st.write(f"Guess history: {st.session_state['guess_history']}")

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

chart = alt.Chart(guess_alt).mark_circle(size=100).encode(
    x = alt.X("guessing_attempt:Q", title="Guessing Attempt"),
    y = alt.Y("guess:Q", title="Your Guess"),
    color = alt.Color("point_color:N", scale=None)
)

st.altair_chart(chart, use_container_width=True)

if "#008000" in st.session_state['colors']:
    st.success(f"You won in {len(st.session_state['guess_history'])} guesses!")

# add the clues history
# ...


# add clues history, number of clues.




if st.button("Go to the Game"):
    st.switch_page("app.py")
