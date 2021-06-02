## easySpeech
<p align="center">
<a href="https://github.com/SaptakBhoumik/easySpeech/"><img width="727" src="https://img.shields.io/badge/easySpeech-lightgray.svg?logo=appveyor&longCache=true&style=popout"></a>
</p> 

---
[![GitHub issues](https://img.shields.io/github/issues/SaptakBhoumik/easySpeech)](https://github.com/SaptakBhoumik/easySpeech/issues)
[![GitHub forks](https://img.shields.io/github/forks/SaptakBhoumik/easySpeech)](https://github.com/SaptakBhoumik/easySpeech/network/members)
[![GitHub stars](https://img.shields.io/github/stars/SaptakBhoumik/easySpeech)](https://github.com/SaptakBhoumik/easySpeech/stargazers)
[![GitHub license](https://img.shields.io/github/license/SaptakBhoumik/easySpeech)](https://www.github.com/SaptakBhoumik/easySpeech/tree/master/LICENSE)
![GitHub last commit](https://img.shields.io/github/last-commit/SaptakBhoumik/easySpeech)
![GitHub contributors](https://img.shields.io/github/contributors/SaptakBhoumik/easySpeech)
[![Downloads](https://static.pepy.tech/badge/easySpeech)](https://pypi.org/project/easySpeech)

<hr>
easySpeech is an open source python wrapper for google speech to text api that doesn't require PyAaudio(So you specially windows user don't have to deal with the errors while installing PyAudio) and also works with hugging face transformers
<br>


## Installation
You can install easySpeech very easily using the following command<br>
```
pip3 install easySpeech
```

## Usage
* Using google speech to text api <br>
By default easySpeech comes with a default api key which you can for testing purposes using the following code.
```
from easySpeech import speech
a=speech.speech('google')
print(a)
```
For production purpose use your own key because google can revoke the default api key at any time. Get your own api key from http://www.chromium.org/developers/how-tos/api-keys and use the following code
```
from easySpeech import speech
a=speech.speech('google',key="your api key")
print(a)
```
Specifying the duration of speech recognition in seconds(default value is 5 seconds)
```
from easySpeech import speech
a=speech.speech('google',duration = 10)
print(a)
```
Specifying the sample frequency(default is 44100)
```
from easySpeech import speech
a=speech.speech('google',duration = 10,freq = 44100)
print(a)
```
Specifying the language(works only for google speech api and default is english)
```
from easySpeech import speech
a=speech.speech('google',language="en-US")
print(a)
```
Converting an audio file to text(Currently it supports only wav file)
```
from easySpeech.recognize import *
r = Recognizer()
recording = AudioFile('recording.wav')
with recording as source:
    audio = r.record(source)
text=r.recognize_google(audio,key=None, language="en-US", show_all=False)
```

* Using hugging face transformers(works offline and no need of any kind of api key)
For using easySpeech with hugging face transformers use the following code.
```
from easySpeech import speech
a=speech.speech('ml')
print(a)
```
Specifying the duration of speech recognition in seconds(default valus is 5 seconds)
```
from easySpeech import speech
a=speech.speech('ml',duration = 10)
print(a)
```
Specifying the sample frequency(default is 44100)
```
from easySpeech import speech
a=speech.speech('ml',duration = 10,freq = 44100)
print(a)
```
Converting an audio file to text(Currently it supports only wav file)
```
from easySpeech import ml
a=ml.ml('recording.wav')
print(a)
```
* Recording audio <br>
For recording audio use the following code
```
from easySpeech import record
import sounddevice as sd
freq = 44100
duration = 5
recording = sd.rec(int(duration * freq), 
                    samplerate=freq, channels=2)

record.write("recording.wav", recording, freq, sampwidth=2)
```
<br>


## How to contribute
Since it is a free software , you can contribute to make it better. New contributors are always welcome, whether you write code, create resources, report bugs, or suggest features.

The easySpeech is written primarily in Python3x

Have a look at the [open issues](https://github.com/SaptakBhoumik/easySpeech/issues) to find a mission that resonates with you.


<hr>

# Contact
Email: saptakbhoumik@gmail.com <br />
If you find any bug make a <a href="https://github.com/SaptakBhoumik/easySpeech/issues">issue</a> **immediately.**
<br>

# License
easySpeech is lisenced under MIT license
```
MIT License | Copyright (c) 2021 SaptakBhoumik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software
```

