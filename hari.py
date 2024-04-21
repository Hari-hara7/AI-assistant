import speech_recognition as sr
import pyttsx3
import webbrowser


recognizer = sr.Recognizer()


engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello! I'm your AI assistant. How can I help you today?")
    while True:
        user_input = listen().lower()
        if "hello" in user_input:
            speak("Hello! How can I assist you?")
        elif "how are you" in user_input:
            speak("I'm doing well, thank you for asking!")
        elif "open chrome" in user_input:
            speak("Opening Google Chrome")
            webbrowser.open("https://www.google.com")
        elif "bye" in user_input or "exit" in user_input:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I didn't catch that. Can you repeat?")

if __name__ == "__main__":
    main()
