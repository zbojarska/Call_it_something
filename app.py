import streamlit as st

page1 = st.Page("game.py", title="Play", icon="🤔")
page2 = st.Page("stats.py", title="Stats", icon="📈")

pg = st.navigation(pages=[page1, page2])
pg.run()
