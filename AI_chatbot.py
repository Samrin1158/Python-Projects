#Rule based AI PYTHON  chatbot

#features
#Responds to user input
#works continuously until the user types bye 
#Easy to customize with new keywords and response 
#Demonstrate real world chatbot logic using python fundamentals

#Future Scope
#1.Add time based greeting (using datetime module)

import datetime
import time
name = input("Welcome, Enter your name : ")
presentHour=datetime.datetime.now().hour
if 5<= presentHour <=11:
    print("Good Morning," ,name)
elif 11<= presentHour <=17:
    print("Good Afternoon,",name)
elif 17 <= presentHour <=20:
    print("Good Evening,",name)
else:
    print("Good Night ",name)


#2.Add text-to-speech (using pyttsx3)
#3.Add voice input (using speech_recognition)
#4.Connect to an AI API for real answer (like OpenAI/Hugging Face)
#5.Store chat history in afile using File Handling 

print("WELCOME TO YOUR SMART AI CHATBOT")
print("You can ask me basic question,Type 'bye' to exit from the bot ")

#chatbot memory creation [dictionary of responses]
responses={
    "hello":"Hi,Welcome.How can I help you?",
    "how are you":"I am very fine .Thank you",
    "who are you":"I am smart AI Chatbot ",
    "motivate me":"Keep going. Every bug of your project makes you a better developer ",
    "happy":" Great to here that "
}
#Method/Function to get response of Chatbot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to tell that yet now . But will learn that soon"

#Take user input 
while True:
    userInput = input("Please ask your Question : ")
    reply = getResponseOfBot(userInput)
    print("Bot Response : ",reply)

    if "bye" in userInput.lower():
        break














