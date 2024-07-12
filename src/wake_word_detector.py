import pvporcupine
import pyaudio
import struct

class WakeWordDetector:
    def __init__(self, wake_word_model_path: str, access_key: str) -> None:
        """
        Constructor method. Initializes the WakeWordDetector class with the specified wake word model path and access key.
        
        Args:
            wake_word_model_path (str): The path to the wake word model file.
            access_key (str): The access key for the Porcupine wake word engine.
        """
        self.wake_word_model_path = wake_word_model_path
        self.access_key = access_key
    
    def listen_for_wake_word(self):
        """
        Listens for the wake word using the Porcupine wake word detection engine.
        
        Returns:
            bool: Returns True if the wake word is detected, otherwise returns False.
        """
        porcupine = None
        pa = None
        audio_stream = None
        
        try:
            # Initialize the Porcupine wake word detection engine
            porcupine = pvporcupine.create(
                access_key=self.access_key,
                keyword_paths=[self.wake_word_model_path])
            
            # Initialize the PyAudio stream
            pa = pyaudio.PyAudio()
            audio_stream = pa.open(rate=porcupine.sample_rate,
                                   channels=1,
                                   format=pyaudio.paInt16,
                                   input=True,
                                   frames_per_buffer=porcupine.frame_length)
            print("[ WakeWordDetector ] - Currently running the Wake Word Detector...")
            
            while True:
                # Read audio stream
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
                
                # Process the audio frame
                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0:
                    print("[ Wake Word Detected ] - Assistant is not in sleep mode anymore.")
                    return True  # Returning True when the wake word is detected 
                else:
                    pass
        except Exception as e:
            print("[ WakeWordDetector | Error on: 'listen_for_wake_word' function ] - Error Message:\n", e)
            return False
        finally:
            # Cleanup resources
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()
            if porcupine is not None:
                porcupine.delete()
