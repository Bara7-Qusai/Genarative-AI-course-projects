# Dictionary containing predefined responses for specific user inputs
responses = {
    "hi": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "hello": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "hey": "Hello! Welcome to TechGadget Support. How can I assist you today?",
    "do you have smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "smartwatches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "smart watches": "Yes, we have a variety of smartwatches. You can check them out on our products page.",
    "shipping time": "Shipping usually takes 3-5 business days.",
    "how long does shipping take": "Shipping usually takes 3-5 business days.",
    "delivery time": "Shipping usually takes 3-5 business days.",
    "shipping methods": "We offer standard, expedited, and overnight shipping.",
    "delivery methods": "We offer standard, expedited, and overnight shipping.",
    "return policy": "You can return products within 30 days of receipt for a full refund.",
    "how to return": "To return a product, please visit our returns page for a step-by-step guide.",
    "return process": "To return a product, please visit our returns page for a step-by-step guide.",
    "won’t turn on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "won't start": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "won’t power on": "Make sure your gadget is charged. If it still won’t turn on, you can visit our troubleshooting page.",
    "reset device": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "reset gadget": "To reset your device, hold down the power button for 10 seconds. If that doesn't work, please check the manual for a factory reset.",
    "bye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!",
    "goodbye": "Thank you for visiting TechGadget. If you have more questions, feel free to ask. Goodbye!"
}

# Counter to track how many times the bot fails to understand the user's input
fallback_counter = 0

# Function to get the bot's response based on user input
def get_bot_response(user_input):
    global fallback_counter  # Access the global fallback counter
    user_input = user_input.lower()  # Convert user input to lowercase

    # Check if any predefined keywords are in the user input
    for keyword, response in responses.items():
        if keyword in user_input:
            fallback_counter = 0  # Reset the fallback counter if a match is found
            return response  # Return the corresponding response

    fallback_counter += 1  # Increment the fallback counter if no match is found

    # If the bot fails to understand the user three times, direct them to human support
    if fallback_counter >= 3:
        fallback_counter = 0  # Reset the fallback counter
        return "It seems I'm having trouble understanding your request. Please reach out to our human customer service representative at support@techgadget.com or call 1-800-TECHGAD."

    # Default response if no match is found
    return "I'm not sure how to respond to that. Can you try asking something else?"

# Main loop to continuously get user input and provide responses
while True:
    user_input = input("You: ")  # Get user input
    if user_input.lower() in ["quit", "exit", "bye"]:  # Check if the user wants to exit
        print("Bot: Goodbye! If you have any more questions, we're here to help.")
        break  # Exit the loop if the user wants to quit

    response = get_bot_response(user_input)  # Get the bot's response
    print(f"Bot: {response}")  # Print the bot's response
