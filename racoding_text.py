import sounddevice as sd
from scipy.io.wavfile import write

# सेटिंग: 44100 samples
fs = 44100 
seconds = 10  # recoding time zone

print("Recording started... 5 second tak boliye...")

# recoding start time
my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

# wait for end voice
sd.wait() 

print("Recording finished! Saving file...")

# फाइल को 'output.wav' के नाम से सेव करें
write('output.wav', fs, my_recording) 

print("File saved as 'output.wav'. Check your folder!")