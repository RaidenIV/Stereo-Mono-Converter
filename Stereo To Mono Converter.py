from pydub import AudioSegment

sound = AudioSegment.from_wav("file path") # Load file
sound = sound.set_channels(1) # Set to mono (1 channel)
sound.export("file path", format="wav") # Create mono file in .wav file format