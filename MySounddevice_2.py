'''Voice Recorder with Playback Speed Control: After recording a clip, let the user choose to play it back at 
normal speed, fast, or slow before saving it. What it should do: Record a single audio clip, Ask the user: play 
at normal, fast, or slow speed? Play it back accordingly Save the final clip as a WAV file'''

import sounddevice as sd
import numpy as np
import wave

sd.default.device = (2, 5)
samplerate = 44100

while True:
    try:
        time = int(input('How long would you like to record: '))
        break
    except ValueError:
        print('Nope, You have enter an integer') 

print('Recording Starts...')
audio = sd.rec(time*samplerate, samplerate, channels = 1)
sd.wait()
print('Recording is Done')

while True:
    try:
        speed = float(input('How Do you want to hear your audio, 0.5X or 2X. just type (0.5 or 2): '))
        break
    except ValueError:
        print('Nope, You have to enter an integer')

# if speed == 2:
#     sp = 2
# elif speed == 0.5:
#     sp = 0.5
# else:
#     print('your input is niether 2 nor 0.5, so paying at 1.')
#     sp = 1

sd.play(audio, samplerate * speed)
sd.wait()

AA = np.int16(audio * 32767)

with wave.open('Mysd2.wav', 'wb') as wv:
    wv.setframerate(samplerate*speed)
    wv.setnchannels(1)
    wv.setsampwidth(2)
    wv.writeframes(AA.tobytes())

print('All Done!')
