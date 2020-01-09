## Abbot 
#### A chatbot framework for humans

Abbot(powered by Flask) is a developer-friendly framework to rapidly create chatbots while maintaining customizability.

### Example

```python
from abbot import Abbot

app = Abbot()

hello_utterances = ['Hi', 'Hello', 'How are you', 'What is up', 'Sup']

@app.intent("greeting", hello_utterances)
def hello():
    return "Hello!"

app.start()
```

### Running the example 
`# TODO: Convert to pip package`

1. Clone the repository
2. cd into Abbot
3. `pip install -r requirements.txt`
4. `python example.py`

