import wolframalpha
import PySimpleGUI as sg
import wikipedia

app_id = "censored api key"
client = wolframalpha.Client(app_id)

sg.theme('DarkPurple')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Lieutenant - At your duty!', layout)

import pyttsx3
engine = pyttsx3.init()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None,'Cancel'):
        break
    try:
        wiki_ans = wikipedia.summary(values[0],sentences=2)
        wolfram_ans = next(client.query(values[0]).results).text
        engine.say(wolfram_ans)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_ans,"Wikipedia Result: "+wiki_ans)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_ans = next(client.query(values[0]).results).text
        engine.say(wolfram_ans)
        sg.PopupNonBlocking(wolfram_ans)
    except wikipedia.exceptions.PageError:
        wolfram_ans = next(client.query(values[0]).results).text
        engine.say(wolfram_ans)
        sg.PopupNonBlocking(wolfram_ans)
    except:
        wiki_ans = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_ans)
        sg.PopupNonBlocking(wiki_ans)

    engine.runAndWait()
window.close()