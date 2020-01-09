# Define actions with corresponding intents
# Use some ML magic to figure out the best way to match utterances to intents
from functools import wraps
from flask import Flask, request
import json


class Abbot:
    """
    The main wrapper class for the bot
    Each bot is an instance of Abbot
    """

    def __init__(self):
        """
        Constructor
        Initializes intents and flask
        """
        self.intents = {}
        self.app = Flask(__name__)

    def intent(self, name, utterances):
        """
        The intent decorator function
        :param name: the intent name
        :param utterances: as of now, a list of strings
        :return:
        """
        def intent_wrapper(func):
            """
            This is where the intent handler registration happens
            :param func:
            :return:
            """
            self.intents[name] = {'function': func, 'args': [], 'kwargs': {}, 'utterances': utterances}

            @wraps(func)
            def caller(*args, **kwargs):
                """
                This method is called when the `func` function is called
                :param args:
                :param kwargs:
                :return:
                """
                self.intents[name] = {'function': func, 'args': args, 'kwargs': kwargs}

            return caller

        return intent_wrapper

    def start(self):
        """
        Starts the flask server (and hence the bot)
        # TODO: accept the port number and other details for the server
        :return:
        """
        @self.app.route('/', methods=["POST"])
        def chat_endpoint():
            """
            Default flask endpoint for conversation
            :return:
            """
            message = json.loads(request.data)['message']
            intent = self.get_intent_by_utterance(message)
            return self.resolve(intent)

        self.app.run()

    def get_intent_by_utterance(self, message):
        """
        Finds which intent function needs to be triggered based on the utterance provided
        # TODO: Use intent classification instead of string matching
        # TODO: Extend functionality to include entities and context preservation
        :param message:
        :return:
        """
        for intent, data in self.intents.items():
            if message in data['utterances']:
                return intent

    def resolve(self, name):
        """
        Calls the registered intent function given the intent name
        :param name:
        :return:
        """
        func = self.intents[name]['function']
        args = self.intents[name]['args']
        kwargs = self.intents[name]['kwargs']
        return func(*args, **kwargs)
