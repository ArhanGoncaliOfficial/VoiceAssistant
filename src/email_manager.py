import imaplib
import email
from email.header import decode_header

"""

[ UNDER CONSTRUCTION ]

"""

"""
Credentials list must be in this order:
[EMAIL_ADDRESS, PASSWORD]
"""

class EmailNotificationManager:
    def __init__(self, credentials:list) -> None:
        self.credentials = credentials
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")

    def get_email_count_data(self) -> int:

        """ This function returns data of an email count from defined email account. """

        self.mail.login(self.credentials[0], self.credentials[1])
        self.mail.select("inbox")
        status, response = self.mail.search(None, "(UNSEEN)")
        unread_count = len(response[0].split())

        if status == "OK":
            self.mail.close()
            self.mail.logout()

            return int(unread_count)
        
        else:
            return "Could not gather email information."
    
    def get_detailed_email_info(self) -> dict:
        """ This function returns a dict of detailed email info. (sender, content) """
        try:
            self.mail.login(self.credentials[0], self.credentials[1])
            self.mail.select("inbox")
            
            status, messages = self.mail.search(None, "ALL")
                     
            mail_ids = messages[0].split()
            
            emails_dict = {}
            
            for mail_id in mail_ids:
                status, msg_data = self.mail.fetch(mail_id, "(RFC822)")
                
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        
                        sender = msg.get("From")
                        
                        content = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                content_type = part.get_content_type()
                                if "text/plain" in content_type:
                                    charset = part.get_content_charset()
                                    content += part.get_payload(decode=True).decode(charset)
                        else:
                            content = msg.get_payload(decode=True).decode()
                        
                        emails_dict[sender] = content.strip()
            
            self.mail.close()
            self.mail.logout()
            
            return emails_dict
        
        except Exception as e:
            print(f"Exception: {str(e)}")
            return None
