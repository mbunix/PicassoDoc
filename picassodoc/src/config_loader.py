import json

class ConfigLoader:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config =self.load_config()
        
    
    
    
    
    def load_config(self):
        with open(self.config_file_path, 'r') as file:
            config = json.load(file)
        return config
    
    def get(self ,key,default =None):
        return self.config.get(key,default)