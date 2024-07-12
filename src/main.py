from audio_recognizer import AudioRecognizer
from wake_word_detector import WakeWordDetector
from assistant_response import AssistantResponse
from weather import WeatherAPIController
from config import ConfigReader
from datetime import datetime
import time

"""

[ UNDER CONSTRUCTION ]

"""

class AssistantMain:
    def __init__(self) -> None:
        self.audio_recognizer = None
        self.wake_word_detector = None
        self.assistant_response = None
        self.weather_controller = None
        self.sleep = True
        self.setAssistant()

    def setAssistant(self):
        config = ConfigReader(config_path=r'data\\assistant.cfg')
        assistant_configuration = config.get_assistant_configuration()
        assistant_audio_engine_settings = config.get_assistant_audio_engine_settings()
        audio_processing_settings = config.get_audio_processing_settings()
        api_container = config.get_api_container()

        if api_container is None or 'porcupine_access_key' not in api_container:
            print("Porcupine access key not found in configuration.")
            return

        self.audio_recognizer = AudioRecognizer(
            language_to_process=audio_processing_settings['language_to_process'], 
            timeout_duration=audio_processing_settings['process_timeout_duration']
        )
        
        self.wake_word_detector = WakeWordDetector(
            wake_word_model_path=r'data\\jarvis_en_windows_v3_0_0.ppn', 
            acces_key=api_container['porcupine_access_key']
        )
        
        self.assistant_response = AssistantResponse(
            rate=assistant_audio_engine_settings['rate'], 
            volume=assistant_audio_engine_settings['volume'], 
            voice_index=assistant_audio_engine_settings['voice_index']
        )

        self.weather_controller = WeatherAPIController(
            api_key=api_container['openweathermap_api_key'],
            unit='metric'
        )

        self.duration_to_be_awake = audio_processing_settings['duration_to_be_awake']


    def go_to_sleep(self):
        self.sleep = True
        print("[ SLEEP MODE ]")

    def wake_up(self):
        self.sleep = False
        print("[ AWAKE MODE ]")
        self.assistant_response.assistant_respond(response="Awake mode!")

    def main(self):
        while True:
            if self.sleep:
                if self.wake_word_detector is not None:
                    if self.wake_word_detector.listen_for_wake_word():
                        self.wake_up()

            if not self.sleep:
                if self.audio_recognizer is not None:
                    recognized_text = self.audio_recognizer.listen()

                    if recognized_text == None:
                        self.go_to_sleep()

                    elif "time" in recognized_text:  
                        current_time = datetime.now().strftime("%H:%M")
                        self.assistant_response.assistant_respond(response=f"It is currently {current_time}.")

                    elif "weather" in recognized_text:
                        city = self.weather_controller.get_location()
                        weather_dict = self.weather_controller.get_weather(city=city['City'])
                        weather_description = weather_dict['Weather']
                        self.assistant_response.assistant_respond(response=weather_description)

            else:
                time.sleep(0.1)

if __name__ == "__main__":
    assistant = AssistantMain()
    assistant.main()
