# Pyssistant

Pyssistant is designed to be an conversational interface builder. With some simples lines of code you can create a simple assistente to perform actions to you

# How to use

The first step to create an assistant with pyssistant is to import its dependencies, as shown in the following line

```
from pyssistant.dialog import Dialog
```

Then you'll have to create your dialog list, containing the commands and its answers, 

```
features = []
features.append(feature("report", function=get_report))
features.append(feature("bye", answer="See you later :)", function=get_bye))
```

## dependencies

* [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)
* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx)

## Extra information

* This project is being built using python 2.7
* suggestions are always welcome :)
