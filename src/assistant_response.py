import pyttsx3

class AssistantResponse:
    def __init__(self, rate: int, volume: float, voice_index: int):
        """
        Initializes the AssistantResponse class with the specified rate, volume, and voice index.
        
        Args:
            rate (int): The speech rate for the text-to-speech engine.
            volume (float): The volume for the text-to-speech engine.
            voice_index (int): The index of the voice to be used by the text-to-speech engine.
        """
        self.rate = rate
        self.volume = volume
        self.voice_index = voice_index
        
    def assistant_respond(self, response: str):
        """
        Makes the assistant respond with the given text using the text-to-speech engine.
        
        Args:
            response (str): The response text to be spoken by the assistant.
        
        Returns:
            str: Returns an empty string if the response is None.
        """
        engine = pyttsx3.init(driverName='sapi5')  # Initialize the TTS engine with the 'sapi5' driver.
        voices = engine.getProperty('voices')  # Get the available voices.
        engine.setProperty("rate", self.rate)  # Set the speech rate.
        engine.setProperty("volume", self.volume)  # Set the volume.
        engine.setProperty("voice", voices[self.voice_index].id)  # Set the voice using the voice index.

        if response is None:  # Check if the response is None.
            return ""
        
        engine.say(text=response)  # Make the engine say the response text.
        engine.runAndWait()  # Wait for the speech to finish.
        engine.stop()  # Stop the engine.
