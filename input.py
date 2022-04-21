import sounddevice as sd
from scipy.io.wavfile import write

fs=16000
print("Say YES")
record_voice= sd.rec( int ( 1 * fs ) , samplerate = fs , channels = 2 )

sd.wait()

write("out6.wav",fs,record_voice)
print ("Done.")