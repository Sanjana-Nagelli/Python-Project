import pyttsx3
import PyPDF2
from tkinter.filedialog import *

converter = pyttsx3.init()
  
converter.setProperty('rate', 200)
# Set volume 0-1
converter.setProperty('volume', 1.0)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
  
# Use female voice
converter.setProperty('voice', voice_id)
  
converter.runAndWait()

book=askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages

for num in range(0,pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait() 