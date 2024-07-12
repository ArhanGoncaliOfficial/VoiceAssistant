from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsAppNotificationManager:
    def __init__(self, PATH:str) -> None:
        """
        Initializes the WhatsAppNotificationManager class and opens WhatsApp Web in an incognito Chrome browser window.
        
        Args:
            PATH (str): The path to the ChromeDriver executable.
        """
        self.path = PATH
        chrome_options = Options()
        chrome_options.add_argument('--incognito') # Open browser in incognito mode
        self.driver = driver = webdriver.Chrome(service=Service(self.path), options=chrome_options)

        driver.get("https://web.whatsapp.com")
        

    def get_detailed_notification_info(self) -> dict:

        """
        Get detailed information about unread messages for each contact listed.
        
        Returns:
            dict: A dictionary with contact names as keys and the number of unread messages as values.
        """

        try:
            chat_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x10l6tqk.xh8yej3.x1g42fcv"))
            )
            
            unread_message_data = {}
            
            for chat in chat_elements:
                try:
                    name_element = chat.find_element(By.CSS_SELECTOR, "span[title]")
                    name = name_element.get_attribute("title")
            
                    unread_indicator = chat.find_elements(By.CSS_SELECTOR, "div._ahlk")
                    if unread_indicator:
                        unread_count_element = unread_indicator[0].find_element(By.CSS_SELECTOR, "span")
                        unread_count = int(unread_count_element.text) if unread_count_element.text.isdigit() else 0
                    else:
                        unread_count = 0

                    unread_message_data[name] = unread_count
                    
                except Exception as inner_e:
                    print(f"An error occurred inside loop: {inner_e}")
                    continue

            return unread_message_data

        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

    def get_unread_message_count_data(self) -> int:

        """
        Get the total count of unread messages.
        
        Returns:
            int: The total number of unread messages.
        """

        try:
            unread_message_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div._ahlk span.x1rg5ohu.x173ssrc.x1xaadd7.x682dto.x1e01kqd.x12j7j87.x9bpaai.x1pg5gke.x1s688f.xo5v014.x1u28eo4.x2b8uid.x16dsc37.x18ba5f9.x1sbl2l.xy9co9w.x5r174s.x7h3shv"))
            )
            print(unread_message_elements)  

            whatsapp_unread_message_count = 0

            for element in unread_message_elements:
                if element.text.isdigit():
                    whatsapp_unread_message_count += int(element.text)
            return whatsapp_unread_message_count
        except Exception as e:
            print(f"No new messages found or an Exception occured:\n{e}")

    def get_unread_chat_count_data(self) -> int:

        """
        Get the total count of chats with unread messages.
        
        Returns:
            int: The total number of chats with unread messages.
        """

        try:
            unread_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x10l6tqk.x14ipxcb.x1oozmrk span.x1rg5ohu.x173ssrc.x1xaadd7.x682dto.x1e01kqd.x12j7j87.x9bpaai.x1pg5gke.x1s688f.xo5v014.x1u28eo4.x2b8uid.x16dsc37.x18ba5f9.x1sbl2l.xy9co9w.x5r174s.x7h3shv"))
            )
            whatsapp_unread_message_count = []
            for element in unread_elements:
                if element.text.isdigit():
                    whatsapp_unread_message_count.append(element.text)
            return int(whatsapp_unread_message_count[0])
        except Exception as e:
            print(f"An error occurred while getting unread chat count: {e}")