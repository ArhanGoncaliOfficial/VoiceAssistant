<h1>VoiceAssistant</h1>

<p>
    The VoiceAssistant project is a comprehensive and customizable voice assistant application designed to enhance user interaction through voice commands. Utilizing advanced wake word detection with the Porcupine engine, this assistant can perform various tasks such as providing weather updates, managing emails, sending WhatsApp notifications, controlling ESP32 devices, and retrieving information from Wikipedia. The project integrates multiple technologies, including Selenium for web automation, Pyttsx3 for text-to-speech, and various APIs for seamless functionality. Ideal for smart home applications and personal productivity, VoiceAssistant offers an extensible framework for adding new features and customizations.
</p>
<br>
<h1>PROJECT IS UNDER DEVELOPMENT</h1>
<br>
<h2>Repository Overview</h2>
<ul>
    <li><strong>Owner:</strong> <a href="https://github.com/ArhanGoncaliOfficial">ArhanGoncaliOfficial</a></li>
</ul>

<h2>Project Structure</h2>

<h3>Configuration and Data Files</h3>
<ul>
    <li><code>assistant.cfg</code>: Configuration file for the assistant.</li>
    <li><code>jarvis_en_windows_v3_0_0.ppn</code>: Wake word model for the assistant. (Using <code>jarvis</code> for now.)</li>
</ul>

<h3>Driver Files</h3>
<ul>
    <li><code>chromedriver.exe</code>: ChromeDriver executable for Selenium automation.</li>
    <li><code>data/First Run</code>, <code>data/Local State</code>, <code>data/Default/Preferences</code>: Data files for ChromeDriver.</li>
</ul>

<h3>Source Code Files</h3>
<ul>
    <li><code>app.py</code>: Main entry point for the web application.</li>
    <li><code>assistant_response.py</code>: Manages the assistant's responses.</li>
    <li><code>audio_recognizer.py</code>: Handles audio recognition. 🚧</li>
    <li><code>config.py</code>: Configuration handler.</li>
    <li><code>email_manager.py</code>: Manages email functionalities. 🚧</li>
    <li><code>esp32_manager.py</code>: Manages interactions with ESP32. 🚧</li>
    <li><code>main.py</code>: Another main entry point, central script. 🚧</li>
    <li><code>selenium_cookie_collector.py</code>: Manages cookies with Selenium. 🚧</li>
    <li><code>socket_test.py</code>: For testing socket connections. 🚧</li>
    <li><code>wake_word_detector.py</code>: Detects wake words.</li>
    <li><code>weather.py</code>: Retrieves weather information. 🚧</li>
    <li><code>whatsapp_manager.py</code>: Manages WhatsApp notifications. 🚧</li>
    <li><code>wikipedia_manager.py</code>: Retrieves information from Wikipedia. 🚧</li>
</ul>

<h3>🚧 Web Files 🚧</h3>
<ul>
    <li><code>static/styles/index.css</code>: CSS styles for the web interface.</li>
    <li><code>templates/index.html</code>: HTML template for the web interface.</li>
</ul>

<h2>Setup Instructions</h2>
<ol>
    <li>
        <strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/ArhanGoncaliOfficial/VoiceAssistant.git
cd VoiceAssistant</code></pre>
    </li>
    <li>
        <strong>Install Dependencies:</strong>
        <p>Ensure you have <code>pip</code> installed and then install the required Python packages:</p>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>
        <strong>Configuration:</strong>
        <p>Update the <code>assistant.cfg</code> file with your custom settings.</p>
    </li>
    <li>
        <strong>Running the Assistant:</strong>
        <p>Start the application using the main script:</p>
        <pre><code>python src/main.py</code></pre>
    </li>
</ol>

<h2>Features</h2>
<ul>
    <li><strong>Wake Word Detection:</strong> Using the Porcupine wake word engine.</li>
    <li><strong>Voice Responses:</strong> Utilizes <code>pyttsx3</code> for text-to-speech.</li>
    <li><strong>Weather Updates:</strong> Fetches weather data from OpenWeatherMap.</li>
    <li><strong>WhatsApp Notifications:</strong> Manages notifications using Selenium and ChromeDriver.</li>
    <li><strong>Email Management:</strong> Handles sending and receiving emails.</li>
    <li><strong>ESP32 Interaction:</strong> Controls and manages interactions with ESP32 devices.</li>
    <li><strong>Wikipedia Integration:</strong> Retrieves and reads out Wikipedia information.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.</p>

<h2>Contact</h2>
<p>For any inquiries, please contact <code>arhangoncaliofficial@gmail.com</code></p>

<h2>Acknowledgements</h2>
<p>Made by <b>Arhan Goncalı</b></p>
