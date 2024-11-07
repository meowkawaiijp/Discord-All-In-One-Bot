import json,os
class config():
    def __init__(self):
        self._configpath = "./config/config.json"
        self._config = self.load()
    def setup(self):
      c = open(self._configpath,'w')
      return json.load(c)
    def load(self):
        if not os.path.exists(self._configpath):
            return self.setup()
        c = open(self._configpath,'r')
        return json.load(c)
    def save(self,name,value):
        self._config[name] = value
        return