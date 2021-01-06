import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Bertha here how can i help you Assad')
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bertha' in command:
                command = command.replace('bertha', '')
                print(command)

    except:
        pass
    return command


def run_bertha():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print('playing')
    elif 'who is' in command:
        person = command.replace('who is', '')
        talk(person + 'is')
        pywhatkit.search(person)



run_bertha()


