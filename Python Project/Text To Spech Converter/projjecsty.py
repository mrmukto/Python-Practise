from gtts import gTTS
import os
fh = open("audio.txt", "r")
rtex = fh.read().replace("\n"," ")
language = "en"
output = gTTS(text=rtex, lang=language, slow=False)
output.save("save.mp3")
fh.close()
os.system(" start save.mp3")