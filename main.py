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

def menu():
    print("Welcome to MyGPT! Here you can:\n")
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
    if not prevMsg:
        print("Your chat logs are empty. Returning to the menu.\n")
        menu()

    else:
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
                {"role": "system", "content": f"You are a helpful friend. These are the previous messages from your conversation: {prevMsg}"},
                {"role": "user", "content": f"{action}"}
            ]

            gptOutput = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=2048,
                messages=messages
            )

            gptResponse = gptOutput["choices"][0]["message"]["content"]

            prevMsg.append("GPT: " + gptResponse)

            print("")
            print("- " + gptResponse), print()

            with open("chatLogs.json", "a") as f:

                json.dump(prevMsg, f, indent=4)
                f.write('\n')

menu()