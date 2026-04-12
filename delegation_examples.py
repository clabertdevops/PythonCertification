from pathlib import Path

class FileWrapper:
    def __init__(self, file):
       self._file = file
    
    def write(self, text):
        print("writing to file")
        self._file.write(text)
    
    def __getattr__(self, name):
        print("getting attribute ",  name)
        
        if name.startswith("_"):
            raise AttributeError(name)
        
        return getattr(self._file, name)
        
filename = "a.txt"

with open(filename, "w" ) as f:
    fw = FileWrapper(f)
    fw.write("hello")  # writing to file
    fw.flush()  # getting attribute

path = Path(filename)
if path.exists():
    path.unlink()
    print("File deleted")