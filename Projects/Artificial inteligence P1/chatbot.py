import sys

def chatbot():
    
    responses = {
        "hi":"Welcome Sir",
        "hello": "Hi there! I am your rule-based AI assistant. ",
        "who are you": "I am a deterministic 'White Box' logic engine.",
        "project": "This is Project 1: The Rule-Based AI Chatbot milestone.",
        "why rules": "Rules ensure zero hallucination risk and 100% traceability. ",
        "status": "All systems operational. The logic skeleton is stable.",
        "bye": "Goodbye! Closing the digital loop. "
    }

    print("--- DecodeLabs Rule-Based Interface ---")
    print("Type 'exit' or 'bye' to stop the heartbeat loop.")

    
    while True:
        
        try:
            raw_input = input("\nYou: ")
            clean_input = raw_input.lower().strip()
        except EOFError:
            break

        
        if clean_input in ['exit', 'quit', 'bye']:
            print("Bot: " + responses.get("bye"))
            break

        reply = responses.get(clean_input, "I do not understand. Please try again. ")
        
        # OUTPUT [cite: 89]
        print(f"Bot: {reply}")

if __name__ == "__main__":
    chatbot()