import speech_recognition as sr
import sys

r=sr.Recognizer()
r.dynamic_energy_threshold = False

with sr.Microphone() as src:
    audio=r.listen(src,timeout=3)
    

nameoftheFile=""
try: 
    nameoftheFile=sys.argv[1]
    f = open(nameoftheFile, "a")
    f.write(r.recognize_google(audio)+"\n")
    f.close()
except IndexError:
    print(r.recognize_google(audio))
    
    