# Guessing Game 🤔

A number-guessing game built with **Streamlit** and an AI-powered hint system. The app picks a secret number between **1 and 100**. Your goal is to guess it—but instead of asking for the number directly, you can ask an AI assistant creative, context-based questions to narrow down the possibilities.

## How to play

1. Start a game. A random number from 1 to 100 is generated for you.
2. Ask the AI for clues using the chat input. Questions must place the secret number in a **specific, real-world scenario** and generally assume a Yes/No answer.
3. Use the answers to make a guess in the number input field and click **Submit**.
4. Keep guessing until you find the number, or click **New Game** to start over.

For example, you can ask:

- *“Would it be possible to have this many children?”*
- *“If this number were my age, would I be allowed to drive?”*
- *“If I weighed this much, would I be considered skinny?”*

Questions like *“Is the number even?”* or *“Is it greater than 50?”* are not allowed. The assistant is instructed not to reveal the number or provide direct numerical clues.

## Features

- **AI-powered hints:** An LLM responds to scenario-based questions about the secret number.
- **Question feedback:** The hint history marks questions as accepted or rejected, with green and red labels.
- **Guess tracking:** See which numbers you've tried and whether each guess was correct.
- **Stats page:** An interactive chart plots your guesses in order, using red for incorrect guesses and green for correct ones. It also displays your hint history and a win message when applicable.
- **API key management:** Enter your UOS AI API key in a dialog and change it later in the sidebar. Connection errors are reported in the interface.
- **Light and dark themes:** Custom green color palettes for both modes.

## Getting started

### Requirements

- Python and `pip`
- A **UOS AI API key** with access to the university's LiteLLM service

You can obtain a key at [keyosk.uni-osnabrueck.de](https://keyosk.uni-osnabrueck.de/).

### Installation

Clone or download the repository, then open a terminal in its root directory.

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
```

On Windows, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

Open the local URL shown in your terminal. When prompted, enter your UOS AI API key. The app checks the key before enabling the AI chat.

## Project structure

```text
.
├── app.py                    # Navigation between Play and Stats
├── game.py                   # Game logic, guessing UI, and hint history
├── stats.py                  # Guess visualization and history
├── ai_utils.py               # AI client, API key handling, and hint generation
├── requirements.txt         # Python dependencies
└── .streamlit/
    └── config.toml          # Light and dark green themes
```

The archive also includes `streamlit-examples/` with example apps and `old_README` with the original coursework instructions.

## How the AI hints work

The app connects to the University of Osnabrück's LiteLLM-compatible API using the OpenAI Python SDK. It sends each question to the `Ornith-1.5-35B-A3B` model together with instructions that include the current secret number.

The assistant is instructed to answer valid scenario-based questions briefly, refuse other requests, and never reveal the number directly. Question validity is **inferred from the wording of the model's response**, so the green/red labels are a heuristic at best.

## Tech stack

- [Streamlit](https://streamlit.io/) — web interface and session state
- [OpenAI Python SDK](https://github.com/openai/openai-python) — client for the LiteLLM-compatible API
- [Pandas](https://pandas.pydata.org/) — guess-history data
- [Altair](https://altair-viz.github.io/) — interactive statistics chart

## Notes

- The application uses `st.session_state` to retain the current game, guesses, and hint history across Streamlit reruns. These are session-level and do not survive e.g. page refreshment.
- **New Game** generates another number and clears the guess and hint histories.
- All requests to the AI model are separate, it does not have memory of the previous conversation. 
- AI responses may not always follow the game rules perfectly, since hints and question classification rely on the language model.
- Keep your API key private; do not commit it to the repository.