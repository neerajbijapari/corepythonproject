import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init()
r = sr.Recognizer()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')


def Say(msg):
 engine.say(msg)
 engine.runAndWait()
def Listen():
 Text = ""
 with sr.Microphone() as source:
  print("Listening......")
  audio = r.listen(source)
  Text = r.recognize_google(audio)
  print("You Said: ",Text)
 return Text

while True:
    choice = str.lower(Listen())
    if "hello" in choice:
        print("Hello Boss")
        Say("Hello Boss")

    elif "open google" in choice:
        Say("Sure Boss, Opening Google")
        webbrowser.open("https://www.google.com")
        print("Sure Boss, Opening Google")

    elif "open youtube" in choice:
        Say("Sure Boss, Opening Youtube")
        webbrowser.open("https://www.youtube.com")
        print("Sure Boss, Opening Youtube")

    elif "open a website" in choice:
        Say("Sure Boss, What Do You Want to See")
        SiteName = str.lower(str.strip(Listen()))
        webbrowser.open("https://www."+SiteName+".com")
        print("Sure Boss, What Do You Want to See")

    elif "search on google" in choice:
        Say("Sure Boss, What Do You Want to search")
        topicName = str.lower(str.strip(Listen()))
        webbrowser.open("https://www.google.com/search?q="+topicName)
        print("Sure Boss, What Do You Want to Search")

    elif "search on youtube" in choice:
        Say("Sure Boss, What Do You Want to search")
        topicName = str.lower(str.strip(Listen()))
        webbrowser.open("https://www.youtube.com/results?search_query="+topicName)
        print("Sure Boss, What Do You Want to Search")

    elif "good morning" in choice:
        print("Good Morning Boss")
        Say("Good Morning Boss")

    elif "good afternoon" in choice:
        print("Good Afternoon Boss")
        Say("Good Afternoon Boss")

    elif "good evening" in choice:
        print("Good Evening Boss")
        Say("Good Evening Boss")

    elif "good night" in choice:
        print("Good Night Boss")
        Say("Good Night Boss")

    elif "how are you" in choice:
        print("I'm doing great, Boss! Hope you are too.")
        Say("I'm doing great, Boss! Hope you are too.")

    elif "what's up" in choice or "whats up" in choice:
        print("All good here, Boss!")
        Say("All good here, Boss!")

    elif "how is it going" in choice:
        print("Everything's going well, Boss!")
        Say("Everything's going well, Boss!")

    elif "greetings" in choice:
        print("Greetings Boss!")
        Say("Greetings Boss!")

    elif "hey" in choice:
        print("Hey Boss!")
        Say("Hey Boss!")

    elif "nice to meet you" in choice:
         print("Nice to meet you too, Boss!")
         Say("Nice to meet you too, Boss!")

    elif "long time no see" in choice:
        print("Yes Boss, it's been a while!")
        Say("Yes Boss, it's been a while!")

    elif "pleasure to meet you" in choice:
        print("Pleasure is mine, Boss!")
        Say("Pleasure is mine, Boss!")

    elif "good to see you" in choice:
        print("Good to see you too, Boss!")
        Say("Good to see you too, Boss!")

    elif "bye" in choice:
        print("Bye Boss")
        Say("Bye Boss")
        break
    else:
        print("Sorry, I can't understand.")
        Say("Sorry, I can't understand.")