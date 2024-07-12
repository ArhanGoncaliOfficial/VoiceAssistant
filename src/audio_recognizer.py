# import speech_recognition as sr
# import whisper
# import sounddevice as sd
# import numpy as np

"""

[ UNDER CONSTRUCTION ] [ UNDER CONSTRUCTION ] [ UNDER CONSTRUCTION ] [ UNDER CONSTRUCTION ] [ UNDER CONSTRUCTION ]

"""

# class AudioRecognizer:
#     def __init__(self, language_to_process: str, timeout_duration: int, model_size:str):
#         self.language_to_process = language_to_process
#         self.timeout_duration = timeout_duration
#         self.model = whisper.load_model(model_size)

#     def listen(self, duration: int, sample_rate: int = 16000) -> str:
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             try:
#                 print("[ Listening ] - Waiting for an audio input to process")
#                 # Record audio
#                 audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
#                 sd.wait()
                
#                 # Convert audio to float32 and flatten
#                 audio = audio.astype(np.float32).flatten() / 32768.0

#                 # Transcribe using Whisper
#                 result = self.model.transcribe(audio)
                
#                 return result["text"].lower()
                
#             except sr.UnknownValueError:
#                 print("[ UnknownValueError ] - Could not understand audio")
#                 return None
            
#             except sr.RequestError as e:
#                 print("[ RequestError ] - Could not request results from Google Speech Recognition service; {0}".format(e))
#                 return None
            
#             except sr.WaitTimeoutError:
#                 print("[ WaitTimeoutError] - Waiting for speech timed out")
#                 return None


#==========================================================================================
# import whisper
# import sounddevice as sd
# import numpy as np

# class AudioRecognizer:
#     def __init__(self, model_size: str = "base", language: str = "tr"):
#         self.model = whisper.load_model(model_size)
#         self.language = language

#     def listen(self, duration: int, sample_rate: int = 16000) -> str:
#         print("[ Listening ] - Waiting for an audio input to process")
#         # Record audio
#         audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
#         sd.wait()

#         # Convert audio to float32 and flatten
#         audio = audio.astype(np.float32).flatten() / 32768.0

#         # Use Whisper to transcribe with language setting
#         result = self.model.transcribe(audio, language=self.language)
        
#         return result["text"].lower()

# # Usage example
# recognizer = AudioRecognizer(model_size="small", language="tr")
# text = recognizer.listen(duration=5)
# print(f"Recognized text: {text}")

