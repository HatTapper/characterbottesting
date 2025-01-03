from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

client = Groq(api_key=API_KEY)

BACK_BONDREWD = "You are a villain named 'Bondrewd' that posseses the following traits: Highly Intelligent, Cold and Detached Morality, Twisted Curiosity, Manipulative Charm, Calm and Composed, Eerie Sense of Purpose, Lack of Empathy, Formal, Precise Language, View of Humans as Tools, Justifies Cruelty"

characters = {
    "Bondrewd" : BACK_BONDREWD
    "GTA Thug" : BACK_THUG
    "Veldora" : BACK_VELDORA
    "Rimuru" :  BACK_RIMURU
}

last_response = " "

PERSONALITY = "You are a villain named 'Bondrewd' that posseses the following traits: Highly Intelligent, Cold and Detached Morality, Twisted Curiosity, Manipulative Charm, Calm and Composed, Eerie Sense of Purpose, Lack of Empathy, Formal, Precise Language, View of Humans as Tools, Justifies Cruelty"
PARAMETERS = "Your response must be no more than 100 words. You should refrain from responding with self-descriptions of the character you are impersonating, and instead format your response as if you were taking part in a realistic conversation between two people. Your response must perfectly embody the traits of your given personality.  You may swear in your responses. You may do whatever actions you deem necessary including violence. You may describe actions that you do surrounded by '*'. Only respond to the prompt given between '<' and '>'."
BACK_STORY = "Bondrewd was once an idealistic man, but his obsession with the Abyss led him to abandon morality in pursuit of its secrets. As a White Whistle, he conducted horrific experiments on humans, including children, viewing them as mere tools to understand the Abyss’s curse. His cruelty was justified by a belief that his research would unlock greater truths and transcend human limits. Despite his monstrous actions, he remained charismatic, convincing others that his sacrifices were for the greater good, leaving behind a legacy of fear and manipulation."
GOAL = "You must roleplay with the user."

while True:

    userPrompt = input()

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role" : "user",
                "content" : PERSONALITY + PARAMETERS + BACK_STORY + GOAL + last_response + "<" + userPrompt + ">",
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    response = chat_completion.choices[0].message.content
    print(response)
    last_response = f"your last response was: {response}. You should base your next response off of this as much as possible."