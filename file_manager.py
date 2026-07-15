import json

class FileManager:

    def load_json(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    def save_json(self,filename,data):
        with open(filename,"w") as file:
            json.dump(data,file,indent=4)
