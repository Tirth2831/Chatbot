'''
Step 1: Get User Input
Use the input() function to take user input.

Step 2: Define Rules
Create a dictionary with key-value pairs.

Step 3: Process User Input
Convert user input to lowercase and check for keywords.

Step 4: Create a Chatbot Loop
Run the chatbot in a loop until the user exits.

Step 5: Testing and Expansion
Test with different inputs and add more rules.
'''
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    rules = {
        "hello": "Hello there! How can I help you?",
        "hi": "Hi! Nice to see you.",
        "how are you": "I am doing well, thank you for asking!",
        "bye": "Goodbye! Have a great day!",
        "weather": "I'm sorry, I cannot provide real-time weather information."
    }

    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Chatbot:", rules["bye"])
            break
        
        response = None
        for key in rules:
            if key in user_input:
                response = rules[key]
                break
        
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")
    
chatbot()