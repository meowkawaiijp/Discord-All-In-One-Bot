import json,os
class config():
    def __init__(self):
        self.configpath = "./config/config.json"
        self._config = self.load()
    def setup(self):
      c = open(self.configpath,'w')
      self._config = json.load(c)
      self.save('token',None)
      return self._config
    def load(self):
        if not os.path.exists(self.configpath):
            return self.setup()
        c = open(self.configpath,'r')
        return json.load(c)
    def save(self,name,value):
        self._config[name] = value