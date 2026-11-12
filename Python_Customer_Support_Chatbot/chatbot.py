import json
import re
import random
from pathlib import Path


# Load the FAQ data
def load_faq():
    faq_path = Path(__file__).resolve().parent / "faq.json"

    try:
        with open(faq_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data["intents"]

    except FileNotFoundError:
        print("Error: faq.json file was not found.")
        return []

    except json.JSONDecodeError:
        print("Error: faq.json contains invalid JSON.")
        return []

    except KeyError:
        print("Error: FAQ data is missing the intents section.")
        return []


# Identify the customer's intent
def identify_intents(user_input, intents):

    matched_intents = []

    for intent in intents:

        for pattern in intent["patterns"]:

            if re.search(pattern, user_input, re.IGNORECASE):

                matched_intents.append(intent)
                break

    return matched_intents


# Generate a response
def generate_response(matched_intents):

    if not matched_intents:
        return "Sorry, I don't understand. Could you rephrase your question?"

    responses = []

    for intent in matched_intents:

        response = random.choice(intent["responses"])

        responses.append(response)

    return "\n".join(responses)


# Main chatbot function
def chatbot():

    intents = load_faq()

    if not intents:
        print("Chatbot cannot start without valid FAQ data.")
        return

    print("====================================")
    print("       TECHSUPPORT CHATBOT")
    print("====================================")

    print("Hello! Welcome to TechSupport.")
    print("How can I assist you today?")
    print("Type 'bye', 'exit', or 'quit' to end.")

    while True:

        try:
            user_input = input("\nYou: ").lower().strip()

            # Check for empty input
            if not user_input:
                print("Bot: Please enter a message.")
                continue

            # Check exit commands
            if user_input in ["bye", "exit", "quit"]:
                print("Bot: Thank you for chatting with us. Goodbye!")
                break

            # Identify customer intent
            matched_intents = identify_intents(user_input, intents)

            # Generate chatbot response
            response = generate_response(matched_intents)

            print("Bot:", response)

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat session ended. Goodbye!")
            break


# Run the chatbot
if __name__ == "__main__":
    chatbot()



