import os, yaml

class Yaml(object):
    def __init__(self, pos):
        self.root = os.path.dirname(os.path.realpath(pos)) 
    
    def load(self, path):
        path = self.root+'/'+path
        if os.path.isfile(path):
            with open(path, 'r') as f:
                return yaml.load(f, Loader=yaml.FullLoader)
        else:
            return "File %s is not exists"%(path)     