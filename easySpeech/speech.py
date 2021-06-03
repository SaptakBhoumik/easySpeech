# import required libraries
import sounddevice as sd
from .recognize import *
from .record import *
from .ml import *


def speech(using,freq = 44100,duration = 5,key=None, language="en-US", show_all=False):
    # Start recorder with the given values of 
    # duration and sample frequency
    recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()
    write("recording.wav", recording, freq, sampwidth=2)
    if using.lower()=='google':
        r = Recognizer()
        recording = AudioFile('recording.wav')
        with recording as source:
            audio = r.record(source)
        text=r.recognize_google(audio,key, language, show_all)

    elif using.lower()=='ml':
        text=ml('recording.wav')
    
    else:
        text='engine not found'
    return text

def google_audio(file,key=None, language="en-US", show_all=False):
    r = Recognizer()
    recording = AudioFile(file)
    with recording as source:
        audio = r.record(source)
    text=r.recognize_google(audio,key, language, show_all)
    return text

def recorder(name,duration = 5,freq = 44100):  
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    write(name, recording, freq, sampwidth=2)