import subprocess   


# subprocess = Python se terminal commands chalane ka tarika. open -a WhatsApp Mac mein koi bhi app kholta hai.

def open_app(app_name:str) ->str:
    # to open in mac
    subprocess.Popen(["open","-a",app_name])
    return f"{app_name} opened broo ji "

def close_app(app_name:str)->str:
    # to close in mac
    subprocess.run(["pkill","-x",app_name])
    return f"{app_name} closed broo ji"


def speak(text:str)->str:
    subprocess.Popen(["say",text])
    return "Speaking!"