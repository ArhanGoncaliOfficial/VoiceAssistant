import configparser

class ConfigReader:
    def __init__(self, config_path: str) -> None:
        """
        Initializes the ConfigReader class and reads the given configuration file.
        If the file cannot be read, it prints an error message.
        
        Args:
            config_path (str): Path to the configuration file.
        """
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        read_files = self.config.read(filenames=self.config_path)
        if not read_files:
            print(f"Configuration file {self.config_path} not found or could not be read.")
        else:
            print(f"Configuration file {self.config_path} read successfully.")

    def get_assistant_configuration(self):
        """
        Reads the assistant configuration from the configuration file.
        
        Returns:
            dict: A dictionary containing the assistant's name and wake word.
        """
        try:
            assistant_name = self.config.get('AssistantConfiguration', 'name')
            wake_word = self.config.get('AssistantConfiguration', 'wake_word')
            return {
                "name": assistant_name,
                "wake_word": wake_word
            }
        except configparser.NoSectionError as e:
            print(f"Section not found: {e.section}")
        except configparser.NoOptionError as e:
            print(f"Option not found: {e.option}")
        return None

    def get_assistant_audio_engine_settings(self):
        """
        Reads the assistant's audio engine settings from the configuration file.
        
        Returns:
            dict: A dictionary containing the rate, volume, and voice index for the audio engine.
        """
        try:
            assistant_speech_rate = self.config.getint('AssistantAudioEngineSettings', 'rate')
            assistant_speech_volume = self.config.getfloat('AssistantAudioEngineSettings', 'volume')
            assistant_voice_index = self.config.getint('AssistantAudioEngineSettings', 'voice_index')
            return {
                "rate": assistant_speech_rate,
                "volume": assistant_speech_volume,
                "voice_index": assistant_voice_index
            }
        except configparser.NoSectionError as e:
            print(f"Section not found: {e.section}")
        except configparser.NoOptionError as e:
            print(f"Option not found: {e.option}")
        return None

    def get_audio_processing_settings(self):
        """
        Reads the audio processing settings from the configuration file.
        
        Returns:
            dict: A dictionary containing the language to process, process timeout duration,
                  and duration to be awake.
        """
        try:
            language_to_process = self.config.get('AudioProcessingSettings', 'language_to_process')
            process_timeout_duration = self.config.getint('AudioProcessingSettings', 'process_timeout_duration')
            duration_to_be_awake = self.config.getint('AudioProcessingSettings', 'duration_to_be_awake')

            return {
                "language_to_process": language_to_process,
                "process_timeout_duration": process_timeout_duration,
                "duration_to_be_awake": duration_to_be_awake
            }
        except configparser.NoSectionError as e:
            print(f"Section not found: {e.section}")
        except configparser.NoOptionError as e:
            print(f"Option not found: {e.option}")
        return None

    def get_api_container(self):
        """
        Reads the API keys from the configuration file.
        
        Returns:
            dict: A dictionary containing the Porcupine access key and OpenWeatherMap API key.
        """
        try:
            porcupine_access_key = self.config.get('API_Container', 'porcupine_access_key')
            openweathermap_api_key = self.config.get('API_Container', 'openweathermap_api_key')
            return {
                "porcupine_access_key": porcupine_access_key,
                "openweathermap_api_key": openweathermap_api_key
            }
        except configparser.NoSectionError as e:
            print(f"Section not found: {e.section}")
        except configparser.NoOptionError as e:
            print(f"Option not found: {e.option}")
        return None
