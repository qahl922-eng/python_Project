'''This is my project, that i am going to solve on my own. 
Voice Recorder with Multiple Takes: Build a program that lets you record multiple clips one after
 another, and then merges them all into a single WAV file at the end.What it should do:
1. Ask the user how many clips they want to record
2. For each clip, ask for the duration, record it, and play it back immediately
3. After all clips are done, merge them into one single WAV file called final_recording.wav'''


import sounddevice as sd
import wave
import numpy as np

sd.default.device = (2, 5)
filelist = []

while True:
    try:
        RecordN = int(input('How many Times do you want to record Audio: '))
        break        # The break only executes if the input was valid — if it throws a ValueError, the loop just continues and asks again.
    except ValueError:
        print('please only Enter the number of Times you want to Record')

for el in range(RecordN):

    print('Recording # %d' %(el+1))
    Samplerate = 44100
    while True:
        try:
            time = int(input('How long do you want to record: '))
            break        
        except ValueError:
            print('please only Enter the number of seconds you want to Record')
    print('Recording Starts')
    record = sd.rec(Samplerate*time, Samplerate, channels=1)
    sd.wait()

    print('Playing recording # %d' %(el+1))
    sd.play(record, Samplerate)
    sd.wait()

    filelist.append(record)

print()
print('all recording done')

sd.play(np.concatenate(filelist), Samplerate)
sd.wait()

print('Combining and saving all the audio files...')
Files = np.concatenate(filelist)
with wave.open('final_recoding.wav', 'wb') as fl:
    fl.setframerate(Samplerate)
    fl.setnchannels(1)
    fl.setsampwidth(2)
    fl.writeframes(np.int16(Files * 32767).tobytes())
print('Files are saved and every thing is Done')
