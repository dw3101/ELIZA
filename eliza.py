# Step 1: Install and Import Libraries
# (Uncomment the next line if running in Jupyter/Colab; in standard Python just install via pip in terminal)
# !pip install textblob

import re
import random
from textblob import TextBlob

# Step 2: Pronoun Swapping Helper
def swap_pronouns(text):
    swaps = {
        "i": "you", "me": "you", "my": "your", "am": "are",
        "you": "I", "your": "my", "mine": "yours", "myself": "yourself"
    }
    words = text.lower().split()
    return ' '.join([swaps.get(word, word) for word in words])

# Step 3: Define ELIZA's Patterns and Responses
patterns = {
    r"I need (.*)": [
        "Why do you need {0}?",
        "Would it really help you to get {0}?",
        "Are you sure you need {0}?"
    ],
    r"I want (.*)": [
        "What would it mean to you if you got {0}?",
        "Why do you want {0}?",
        "Suppose you got {0}, what would you do then?"
    ],
    r"I feel (.*)": [
        "Why do you feel {0}?",
        "What makes you feel {0}?",
        "Do you often feel {0}?"
    ],
    r"I am feeling (.*)": [
        "Why are you feeling {0}?",
        "What led you to feel {0}?"
    ],
    r"I am (.*)": [
        "How long have you been {0}?",
        "Why are you {0}?",
        "Do you enjoy being {0}?"
    ],
    r"I'm (.*)": [
        "How long have you been {0}?",
        "Why are you {0}?"
    ],
    r"Because (.*)": [
        "Is that the real reason?",
        "What other reasons come to mind?",
        "Does that reason apply to anything else?"
    ],
    r"Why don't you ([^\?]*)\??": [
        "Do you really think I don't {0}?",
        "Perhaps eventually I will {0}.",
        "Why do you want me to {0}?"
    ],
    r"Why can't I ([^\?]*)\??": [
        "Do you think you should be able to {0}?",
        "If you could {0}, what would you do?"
    ],
    r"I can't (.*)": [
        "What makes you think you can't {0}?",
        "Have you tried?",
        "What would it take for you to {0}?"
    ],
    r"I remember (.*)": [
        "What does that memory mean to you?",
        "Why do you recall {0} just now?",
        "Does thinking of {0} bring up any other memories?"
    ],
    r"I think (.*)": [
        "Do you doubt {0}?",
        "Why do you think {0}?",
        "What makes you think {0}?"
    ],
    r"I (like|love|enjoy) (.*)": [
        "What do you like about {1}?",
        "Why do you {0} {1}?",
        "How often do you {0} {1}?"
    ],
    r"I (hate|dislike) (.*)": [
        "Why do you {0} {1}?",
        "What happened to make you {0} {1}?"
    ],
    r"I study (.*)": [
        "What do you enjoy about studying {0}?",
        "Is {0} your favorite subject?"
    ],
    r"I work at (.*)": [
        "What do you do at {0}?",
        "How do you feel about your work at {0}?"
    ],
    r"My (mother|father|parent|sister|brother|family) (.*)": [
        "Tell me more about your {0}.",
        "How does your relationship with your {0} affect you?"
    ],
    r"(.*) friend(.*)": [
        "Tell me more about your friends.",
        "Do your friends influence you?"
    ],
    r"(.*) (sad|happy|angry|excited|anxious|depressed|tired|lonely)(.*)": [
        "How long have you felt {1}?",
        "What do you think causes you to feel {1}?"
    ],
    r"(.*)\?": [
        "Why do you ask that?",
        "What do you think?",
        "How would you answer that?"
    ],
    r"Yes": [
        "You seem quite positive.",
        "I'm glad to hear that."
    ],
    r"No": [
        "Why not?",
        "Are you saying 'no' just to be negative?"
    ],
    r"Hello(.*)": [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?"
    ],
    r"Hi(.*)": [
        "Hi! How are you feeling today?",
        "Hello! What would you like to talk about?"
    ],
    r"quit": ["Goodbye!"],
    r"(.*)": [
        "Please tell me more.",
        "Let's change focus a bit... Tell me about your family.",
        "Can you elaborate on that?",
        "How does that make you feel?"
    ]
}

# Step 4: The Main ELIZA Loop
def eliza():
    print("ELIZA: Hello! How are you feeling today? (Type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("ELIZA: Goodbye!")
            break
        response_given = False
        for pattern, responses in patterns.items():
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                groups = tuple(swap_pronouns(g) for g in match.groups())
                response = random.choice(responses)
                print("ELIZA: " + response.format(*groups))
                response_given = True
                break
        if not response_given:
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            if sentiment > 0.2:
                print("ELIZA: You sound positive! Tell me more.")
            elif sentiment < -0.2:
                print("ELIZA: I'm sorry you're feeling down. Want to talk more about it?")
            else:
                print("ELIZA: Please tell me more.")

# Step 5: Run Your Bot!
if __name__ == "__main__":
    eliza()