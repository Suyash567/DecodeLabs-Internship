# Project 1: Rule-Based AI Chatbot Milestone

A lightweight, deterministic "White Box" logic engine built in Python. This chatbot operates entirely on explicit rule-matching to guarantee zero hallucination risk and 100% response traceability.

## Core Features
*   **Deterministic Responses:** Uses exact key-value mapping to ensure predictable, reliable outputs.
*   **Zero Hallucination:** Eliminates the risk of incorrect or fabricated information by relying strictly on predefined logic.
*   **Input Normalization:** Automatically trims whitespace and converts user inputs to lowercase for robust matching.
*   **Safe Exit Handling:** Gracefully handles user termination commands (`exit`, `quit`, `bye`) and end-of-file (`EOFError`) exceptions.

## Available Triggers & Responses
The engine actively listens for the following specific prompts:
*   `hi` ➔ "Welcome Sir"
*   `hello` ➔ "Hi there! I am your rule-based AI assistant."
*   `who are you` ➔ "I am a deterministic 'White Box' logic engine."
*   `project` ➔ "This is Project 1: The Rule-Based AI Chatbot milestone."
*   `why rules` ➔ "Rules ensure zero hallucination risk and 100% traceability."
*   `status` ➔ "All systems operational. The logic skeleton is stable."
*   `bye` / `exit` / `quit` ➔ "Goodbye! Closing the digital loop."

## Requirements
*   Python 3.x (No external dependencies or libraries required)

## How to Run
1. Save the code into a file named `main.py` (or `chatbot.py`).
2. Open your terminal or command prompt.
3. Execute the script using the following command:
   ```bash
   python main.py
