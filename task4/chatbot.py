def chatbot():
    print("=" * 50)
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit the chat.")
    print("=" * 50)

    while True:
        # Take user input
        user = input("\nYou: ").strip().lower()

        # Greetings
        if "hello" in user or "hi" in user or "hey" in user:
            print("Bot: Hi! 👋 Nice to meet you.")

        # Asking about the chatbot
        elif "how are you" in user:
            print("Bot: I'm fine, thanks! How about you?")

        elif "i am fine" in user or "i'm fine" in user:
            print("Bot: That's great to hear! 😊")

        elif "what is your name" in user or "your name" in user:
            print("Bot: My name is Python Chatbot.")

        elif "who created you" in user:
            print("Bot: I was created using Python.")

        # Education-related questions
        elif "python" in user:
            print("Bot: Python is a popular programming language used for AI, web development, automation, and data science.")

        elif "math" in user or "mathematics" in user:
            print("Bot: Mathematics is the study of numbers, patterns, and logical reasoning.")

        elif "computer" in user:
            print("Bot: Computer Science is the study of computers, programming, and algorithms.")

        elif "course" in user:
            print("Bot: There are many courses like Python, Java, Web Development, AI, and Machine Learning.")

        # Thank you
        elif "thank" in user:
            print("Bot: You're welcome! 😊")

        # Exit
        elif "bye" in user:
            print("Bot: Goodbye! Have a great day! 👋")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Run the chatbot
chatbot()