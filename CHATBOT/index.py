class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hello! How can I help you today?",
            "bye": "Goodbye! Have a great day!",
            "help": "Sure! What do you need help with?",
            "weather": "The weather is always changing! What would you like to know?",
            "name": "I am a simple rule-based chatbot. My name is T-800.",
            "news": "I'm not updated on the latest news, but you can check reliable news sources for that."
        }

    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "I'm sorry, I don't understand that. Can you please rephrase your question?"


# Example usage
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    print("Chatbot: Hi! I'm T-800. Type 'exit' or 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)