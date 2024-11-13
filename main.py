import ollama
import speech_recognition as sr
import pyttsx3

#  text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  #  speech rate

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    """Capture voice input and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Speech service is unavailable.")
            speak("Speech service is unavailable.")
    return None

def chat():
    model_name = "stablelm-zephyr"
    print("Welcome to the AI Voice Chatbot! Say 'exit' to end the conversation.")
    speak("Welcome to the AI Voice Chatbot! Say 'exit' to end the conversation.")

    while True:
        user_input = get_voice_input()
        if user_input is None:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            speak("Goodbye!")
            break

        # Generate response using the model
        response = ollama.generate(model=model_name, prompt=user_input)
        
        # Extract and speak only the response text
        if 'response' in response:
            bot_response = response['response']
            print(f"AI: {bot_response}")
            speak(bot_response)
        else:
            print("AI: Sorry, I didn't understand that response.")
            speak("Sorry, I didn't understand that response.")

if __name__ == "__main__":
    chat()
