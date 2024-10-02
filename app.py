import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command from the user
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {command}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Can you say that again?")
            return None
        return command.lower()

# Function to respond to voice commands
def respond(command):
    if 'hello' in command:
        speak("Hello! How can I assist you today?")

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif 'search' in command:
        speak("What would you like to search for?")
        query = take_command()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query} on Google")

    elif 'wikipedia' in command:
        speak("What should I search on Wikipedia?")
        query = take_command()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia, {summary}")
            except wikipedia.exceptions.DisambiguationError:
                speak(f"Multiple results found for {query}, please be more specific.")
            except Exception:
                speak(f"Sorry, I couldn't find any information on {query}.")

    elif 'exit' in command or 'bye' in command:
        speak("Goodbye! Have a nice day!")
        exit()

    else:
        speak("Sorry, I didn't understand that. Can you repeat it?")

# Main loop
if __name__ == "__main__":
    speak("Voice assistant initialized. Say hello to start.")
    
    while True:
        command = take_command()
        if command:
            respond(command)
