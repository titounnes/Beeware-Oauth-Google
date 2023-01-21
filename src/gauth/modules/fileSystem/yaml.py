import yaml 
from gauth.modules.fileSystem.file import File

class Yaml(object):    
    def load(self, path):
        path = File().get_path(path)
        if path:
            with open(path, 'r') as f:
                return yaml.load(f, Loader=yaml.FullLoader)
        else:
            return "File %s is not exists"%(path)     