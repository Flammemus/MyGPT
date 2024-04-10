import openai
import json
from art import *

with open("myApiKey.json", "r") as f:
    apiKeyData = json.load(f)

myApiKey = apiKeyData["myApiKey"]
openai.api_key = myApiKey

prevMsg = []

print("@*----------------------------------------------------------------------------------------------*@")
tprint("MyGPT")
print("\nWelcome to MyGPT! Here you can:\n")

def menu():
    print("- Chat")
    print("- View\n")

    action = input(": ")
    print("")

    if action.lower() == "chat":
        chatting()
    
    if action.lower() == "view":
        viewing()
    
def viewing():
    print("Displaying chat logs...\n")
    for i in prevMsg:
        print(i, "\n")

def chatting():
    print("Chat started, type 'Back' to return to the menu\n")

    t = True
    while t:

        action = input(": ")

        if action.lower() == "back":
            print("\n------------------------\n")
            print("Welcome back!\n")
            menu()
            t = False

        else:

            prevMsg.append("You: " + action)

            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"These are the previous messages: {prevMsg}. Answer future questions with the previous messages in mind."},
                {"role": "user", "content": f"{action}"}
            ]

            gptOutput = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=2048,
                messages=messages
            )

            prevMsg.append("- " + gptOutput["choices"][0]["message"]["content"])

            print("")
            print("-", gptOutput["choices"][0]["message"]["content"]), print()

menu()