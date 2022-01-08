import os
python_interpreter = "/home/mihir/Desktop/experimental/bin/python3"
print("Starting the process of recording the audio!")
os.system(f"{python_interpreter} /home/mihir/Desktop/ChatBot/voiceRecorder.py")
print("Starting the process of generating a text file")
os.system(f"{python_interpreter} /home/mihir/Desktop/ChatBot/voiceWriter.py")