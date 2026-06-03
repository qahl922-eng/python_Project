# Recording sound using sounddevice module.
# It took me 4 days to do this project by the way... 
'''I highly recommend you to read the Library and module pdf to further understand the full concepts used here in this project'''
import sounddevice as sd
import wave as wv
import numpy as np

duration = int(input('How much would you like to record: '))
sampate = 44100

# This function below gives You the list of all availible input & output devices.
#print(sd.query_devices())   # Comment this function out to run the code...
# This is a paramter, which sets both default input and output devices...
sd.default.device = (2, 5) 

# The funcion sd.rec records the sound coming from selected microphone...
print('Recording is started...')
audio = sd.rec(duration * sampate,  samplerate = sampate, channels = 1,)
sd.wait()    # This  pauses the execution untill the rec function is done recording..
print('Recording is Done!')

# This line convets the data which is in -1 -> +1 range coming from rec function to 16-bit binary integers...
num11 = np.int16(audio * 32767)

# This function plays the sound recorded in rec function...
print('Playing the sound now!')
se = sd.play(audio, samplerate = 44100)
sd.wait()

# Here we are using wave module's open function to save that audio data into wave files
with wv.open('record1.wav', 'wb') as rr:
    rr.setframerate(sampate)
    rr.setnchannels(1)
    rr.setsampwidth(2)
    rr.writeframes(num11.tobytes())   # This .tobytes() method converts 16-bit data to bytes, thats what .wav file takes in.
print('recording saved as well')