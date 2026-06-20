import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# ==========================
# GEMINI CONFIGURATION
# ==========================

genai.configure(api_key="Enter your API key")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)

history = []


# ==========================
# CHATBOT GUI
# ==========================

class ChatbotGUI:

    def __init__(self, root):
        self.root = root

        self.root.title("🤖 Gemini AI Assistant")
        self.root.geometry("950x750")
        self.root.configure(bg="#151521")

        # HEADER

        header = tk.Frame(root, bg="#0F172A", height=70)
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text="🤖 Gemini AI Assistant",
            bg="#0F172A",
            fg="#00FFAA",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=15)

        # CHAT AREA

        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Segoe UI", 11),
            bg="#1E293B",
            fg="white",
            insertbackground="white",
            bd=0,
            padx=15,
            pady=15
        )

        self.chat_area.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        self.chat_area.config(state=tk.DISABLED)

        self.chat_area.tag_config(
            "user",
            foreground="#38BDF8",
            font=("Segoe UI", 11, "bold")
        )

        self.chat_area.tag_config(
            "bot",
            foreground="#4ADE80",
            font=("Segoe UI", 11)
        )

        self.chat_area.tag_config(
            "system",
            foreground="#FBBF24",
            font=("Segoe UI", 10, "italic")
        )

        # BOTTOM FRAME

        bottom = tk.Frame(root, bg="#151521")
        bottom.pack(fill=tk.X, padx=10, pady=10)

        self.entry_msg = tk.StringVar()

        self.entry_box = tk.Entry(
            bottom,
            textvariable=self.entry_msg,
            bg="#334155",
            fg="white",
            insertbackground="white",
            relief=tk.FLAT,
            font=("Segoe UI", 12)
        )

        self.entry_box.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=10
        )

        self.entry_box.bind("<Return>", self.send_msg)

        # SEND BUTTON

        self.send_btn = tk.Button(
            bottom,
            text="🚀 Send",
            command=self.send_msg,
            bg="#22C55E",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 11, "bold"),
            padx=20
        )

        self.send_btn.pack(side=tk.LEFT, padx=10)

        # CLEAR BUTTON

        self.clear_btn = tk.Button(
            bottom,
            text="🗑 Clear",
            command=self.clear_chat,
            bg="#EF4444",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 11, "bold"),
            padx=20
        )

        self.clear_btn.pack(side=tk.LEFT)

        # STATUS BAR

        self.status = tk.Label(
            root,
            text="Ready",
            anchor="w",
            bg="#0F172A",
            fg="white"
        )

        self.status.pack(fill=tk.X)

        # WELCOME MESSAGE

        self.add_bot_message(
            "Hello! I am Gemini AI. How can I help you today?"
        )

    # ==========================
    # HELPER METHODS
    # ==========================

    def add_user_message(self, text):
        self.chat_area.config(state=tk.NORMAL)

        self.chat_area.insert(
            tk.END,
            f"\n🧑 You:\n{text}\n\n",
            "user"
        )

        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def add_bot_message(self, text):
        self.chat_area.config(state=tk.NORMAL)

        self.chat_area.insert(
            tk.END,
            f"🤖 Gemini:\n{text}\n\n",
            "bot"
        )

        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def add_system_message(self, text):
        self.chat_area.config(state=tk.NORMAL)

        self.chat_area.insert(
            tk.END,
            text + "\n",
            "system"
        )

        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def clear_chat(self):
        global history

        history = []

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state=tk.DISABLED)

        self.add_bot_message(
            "Chat cleared successfully."
        )

    # ==========================
    # SEND MESSAGE
    # ==========================

    def send_msg(self, event=None):

        msg = self.entry_msg.get().strip()

        if not msg:
            return

        self.entry_msg.set("")

        self.add_user_message(msg)

        self.status.config(text="Gemini is thinking...")

        self.add_system_message("⏳ Gemini is typing...")

        self.root.after(
            100,
            lambda: self.get_response(msg)
        )

    # ==========================
    # GEMINI RESPONSE
    # ==========================

    def get_response(self, msg):

        global history

        try:

            chat_session = model.start_chat(
                history=history
            )

            response = chat_session.send_message(msg)

            model_response = response.text

            history.append(
                {
                    "role": "user",
                    "parts": [msg]
                }
            )

            history.append(
                {
                    "role": "model",
                    "parts": [model_response]
                }
            )

        except Exception as e:
            model_response = f"Error:\n{e}"

        self.chat_area.config(state=tk.NORMAL)

        try:
            self.chat_area.delete("end-3l", "end-1l")
        except:
            pass

        self.chat_area.config(state=tk.DISABLED)

        self.add_bot_message(model_response)

        self.status.config(text="Ready")


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    print("Starting Gemini AI Assistant...")

    root = tk.Tk()

    app = ChatbotGUI(root)

    root.mainloop()
