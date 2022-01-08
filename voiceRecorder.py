import sounddevice
from scipy.io.wavfile import write
import datetime
def record_sound():
    try:
        duration = int(input("For how much time do u want to record the voice: "))
        fs=44100
        print("Recording will now start.....")
        record_voice = sounddevice.rec(int(duration*fs),samplerate=fs,channels=2)
        sounddevice.wait()
        write(f"Recording{datetime.datetime.now().strftime('%Y%m%d')}.wav",fs,record_voice)
    except:
        print("A problem has occurred")
    finally:
        print("Closing this session")

while True:
    choice = input("Do u want to record the voice; To end press -1:")
    if choice.lower()=='y' or choice[0].lower()=='y':
        record_sound()
    elif int(choice)==-1:
        print("Exiting the program")
        break

    else:
        continue