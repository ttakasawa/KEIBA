
from __future__ import print_function

class BaseAgent:
    def __init__(self, config):
        self.config = config

    def loadModel(self, filename):
        raise NotImplementedError

    def saveModel(self, filename):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError

    def trainModel(self):
        raise NotImplementedError

    def validateModel(self):
        raise NotImplementedError

    def hp_tune(self):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError