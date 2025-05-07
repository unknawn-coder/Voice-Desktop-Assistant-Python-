import sounddevice as sd
import soundfile as sf

def start_voice_recording(file_name, duration):
    """
    Start recording voice using the default microphone in Python.

    Args:
        file_name (str): The name of the output audio file.
        duration (int): The duration of the recording in seconds.

    Returns:
        None
    """
    # Set the sample rate and number of channels for recording
    sample_rate = 44100
    channels = 1

    # Start recording audio
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

    # Wait for the recording to finish
    sd.wait()


    # Save the recorded audio to a file
    sf.write(file_name, recording, sample_rate)

# Example usage
#recr = "audio_1"
#start_voice_recording(recr+".wav", 5)
