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

fallback_counter = 0

def get_bot_response(user_input):
    global fallback_counter
    user_input = user_input.lower()

    for keyword, response in responses.items():
        if keyword in user_input:
            fallback_counter = 0
            return response

    fallback_counter += 1

    if fallback_counter >= 3:
        fallback_counter = 0
        return "It seems I'm having trouble understanding your request. Please reach out to our human customer service representative at support@techgadget.com or call 1-800-TECHGAD."

    return "I'm not sure how to respond to that. Can you try asking something else?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! If you have any more questions, we're here to help.")
        break

    response = get_bot_response(user_input)
    print(f"Bot: {response}")