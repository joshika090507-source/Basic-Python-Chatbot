print("Welcome to My Chatbot!")

name = input("Enter your name: ")

print("Hello", name)

while True:
    message = input("You: ")

    if message.lower() == "hello":
        print("Bot: Hello! How can I help you?")

    elif message.lower() == "how are you":
        print("Bot: I am fine. Thank you!")

    elif message.lower() == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
