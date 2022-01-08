import datetime
import speech_recognition as sr
filename = f"Recording{datetime.datetime.now().strftime('%Y%m%d')}.wav"
# intialize the recognizer
r = sr.Recognizer()

# load and convert it to a text file
with sr.AudioFile(filename) as source:
    # listen for the data
    audio_data = r.record(source)
    # convert to text
    text = r.recognize_google(audio_data)

# print(text)
with  open(f"{datetime.datetime.now().strftime('%y%m%d')}.txt",mode='w') as file:
    file.write(text)
