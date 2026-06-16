import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="Enter your API key")

# Create the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the chatbot model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

history = []

class  https://visualstudio.microsoft.com/downloads/ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("700x700")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30, state='disabled')
        self.chat_area.pack(pady=10)

        self.entry_msg = tk.StringVar()
        self.entry_box = tk.Entry(root, textvariable=self.entry_msg, width=70)
        self.entry_box.pack(side=tk.LEFT, padx=10)
        self.entry_box.bind("<Return>", self.send_msg)

        self.send_button = tk.Button(root, text="Send", command=self.send_msg)
        self.send_button.pack(side=tk.RIGHT, padx=10)

    def send_msg(self, event=None):
        msg = self.entry_msg.get()
        if msg:
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.insert(tk.END, "You: " + msg + "\n")
            self.chat_area.config(state=tk.DISABLED)
            self.entry_msg.set("")

            # Chatbot logic here
            global history
            chat_session = model.start_chat(history=history)
            response = chat_session.send_message(msg)
            model_response = response.text

            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.insert(tk.END, "Bot: " + model_response + "\n")
            self.chat_area.config(state=tk.DISABLED)

            history.append({"role": 'user', "parts": [msg]})
            history.append({"role": 'model', "parts": [model_response]})

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()


