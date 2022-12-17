from pydub import AudioSegment
import wave
import os
import numpy as np
from matplotlib import pyplot as plt

# AudioSegment.ffmpeg = "D:\SOFTWARE\FFMPEG\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

file_name = "jingle-bell.mp3"


def convert_mp3_to_wav(file_name):
    sound = AudioSegment.from_mp3('./Audio/{0}.mp3'.format(file_name))
    sound.export("./Audio/{0}.wav".format(file_name), format="wav")

def extract_audio_from_video(file_name):
    print("todo")


def plot_frequency(channel_array, framerate, n_channels):
    plt.figure(figsize=(8, 5))

    for i in range(n_channels):
        plt.subplot(n_channels, 1, i + 1)
        plt.specgram(channel_array[i], Fs=framerate, vmin=-30, vmax=50)
        plt.title("Channel {0}".format(i + 1))
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.colorbar()

    plt.show()

def plot_signal(channel_array, time_array, n_channels):
    plt.figure(figsize=(8, 5))

    for i in range(n_channels):
        print("Channel Shape: {0}".format(channel_array[i].shape))
        plt.subplot(n_channels, 1, i + 1)
        plt.plot(time_array, channel_array[i])
        plt.title("Channel {0}".format(i + 1))
        plt.xlabel("Time (s)")
        plt.ylabel("Signal Value")
    
    plt.show()

def visualize_audio(file):
    file_name, file_extension = os.path.splitext(file)

    if file_extension == ".mp3":
        convert_mp3_to_wav(file_name)
        file_extension = ".wav"

    if file_extension == ".wav":
        wav_audio = wave.open('./Audio/{0}.wav'.format(file_name), "rb")

        # The number of frames per second
        framerate = wav_audio.getframerate()

        # Total number of frames in this audio
        n_frames = wav_audio.getnframes()

        # The length of audio
        audio_len = n_frames/framerate

        # The number of channels
        n_channels = wav_audio.getnchannels()

        print("\nFramerate: {0}\nNumber of frames: {1}\nAudio length(s): {2}\nNumber of channels: {3}\n".format(framerate, n_frames, audio_len, n_channels))

        signal_wave = wav_audio.readframes(n_frames)
        signal_array = np.frombuffer(signal_wave, np.int16)

        time_array = np.linspace(0, audio_len, num=n_frames)

        channel_array = [signal_array[i::n_channels] for i in range(n_channels)]
        
        # Plot Signal
        plot_signal(channel_array, time_array, n_channels)

        # Plot Frequency
        plot_frequency(channel_array, framerate, n_channels)

    else:
        print("This file extension {file_extension} is not supported!".format(file_extension))
    



visualize_audio(file_name)

