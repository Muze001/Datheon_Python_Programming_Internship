 Customer Support Chatbot

 Project Overview

The Customer Support Chatbot is a rule-based chatbot developed using Python as part of the Datheon Python Programming Internship.

It assists users by answering frequently asked questions about products, pricing, business hours, delivery, returns and customer support.

The chatbot uses predefined patterns and responses to identify customer queries and provide relevant information.

 Features

- Greeting recognition.
- Keyword and regular expression matching.
- Business hours information.
- Product and pricing enquiries.
- Delivery and return information.
- Customer contact information.
- Multiple intent recognition.
- Randomized responses.
- Fallback responses for unrecognized questions.
- Conversation exit commands.
- JSON-based FAQ storage.
- Basic error handling.

 Technologies Used

- Python 3
- JSON
- Regular Expressions (`re`)
- Random module
- pathlib module

 Project Structure


Python_Customer_Support_Chatbot/
│
├── chatbot.py
├── faq.json
└── README.md

 Installation and Setup

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run the chatbot using:

bash
python chatbot.py


 Example Queries

Users can interact with the chatbot using questions such as:

- Hello
- What are your business hours?
- What products do you sell?
- How much does it cost?
- How long does delivery take?
- I want a refund.

To end the conversation, type `bye, `exit`, or `quit`.

 How It Works

The chatbot loads predefined FAQ information from `faq.json`.

It then searches user messages for matching patterns using Python's regular expression module.

When a match is found, the chatbot selects and displays an appropriate response.

If no matching intent is found, it provides a fallback response.

 Author : Muizz Ibrahim

Developed as part of the Datheon Python Programming Internship.