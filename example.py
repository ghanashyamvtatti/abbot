"""
Example script that demonstrates how Abbot can be used
"""
from abbot import Abbot

app = Abbot()

hello_utterances = ['Hi', 'Hello', 'How are you', 'What is up', 'Sup']
day_utterances = ['What day is today?', 'What day is it?']


@app.intent("greeting", hello_utterances)
def hello():
    return "Hello!"


@app.intent("day", day_utterances)
def day():
    # TODO: Come up with a way to support multiple responses (of which one will be chosen at random)
    return "Today is a Sunday"


app.start()
