# Gemini AI Chatbot GUI

A simple desktop chatbot application built using Python, Tkinter, and Google's Gemini AI API. This project provides a user-friendly graphical interface for interacting with the Gemini model in real time while maintaining conversation history.

---

## Features

* Interactive GUI built with Tkinter
* Integration with Google Gemini AI
* Real-time AI-generated responses
* Conversation history support
* Scrollable chat interface
* Send messages using Enter key or Send button
* Lightweight and easy to customize


---

## Technologies Used

* Python 3.x
* Tkinter
* Google Generative AI (Gemini API)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemini-chatbot-gui.git
cd gemini-chatbot-gui
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API Key

Create a `.env` file or set an environment variable:

```bash
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get your API key from Google AI Studio.

---

## Run the Application

```bash
python chatbot.py
```

---

## Application Output

When the application starts, a chatbot window opens.

### Sample Conversation

```text
You: Hello

Bot: Hello! How can I assist you today?

You: What is Python?

Bot: Python is a high-level programming language known for
its simplicity, readability, and versatility. It is widely
used in web development, data science, automation, AI, and
many other fields.
```

---

## GUI Preview

```text
 ---------------------------------------------------------
|                      Gemini Chatbot                     |
|---------------------------------------------------------|
| You: Hello                                              |
| Bot: Hello! How can I assist you today?                 |
|                                                         |
| You: What is Python?                                    |
| Bot: Python is a high-level programming language...     |
|                                                         |
|                                                         |
|---------------------------------------------------------|
| [ Type your message here ]              [ Send ]        |
 ---------------------------------------------------------
```

---

## Screenshots

### Main Interface

![Chatbot GUI](images/chatbot-gui.png)

### Conversation Example

![Conversation](images/chatbot-conversation.png)

---

## Requirements

```txt
google-generativeai
```

Install manually:

```bash
pip install google-generativeai
```

---

## Features Demonstrated

* GUI Development with Tkinter
* Gemini AI Integration
* Event Handling
* Conversation Memory
* Real-Time Response Generation
* Python Desktop Application Development

---

## Future Improvements

* Dark Mode
* Voice Input
* Voice Output
* Chat History Export
* Multiple Chat Sessions
* Streaming Responses
* Improved UI Design
* Theme Customization

---

## Security Notice

Do NOT expose your API key in public repositories.

Recommended approach:

* Store API keys in environment variables
* Add `.env` to `.gitignore`
* Never hardcode API keys in source code


## Author

Developed using Python, Tkinter, and Google Gemini AI.
