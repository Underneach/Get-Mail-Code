import email
import imaplib
import re

from PyQt5.QtCore import QThread, pyqtSignal


class GetCode(QThread):
    send_code = pyqtSignal(str)

    def __init__(self, USERNAME, PASSWORD, IMAP_SERVER, regular_string):
        super().__init__()
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.IMAP_SERVER = IMAP_SERVER
        self.regular_string = regular_string

    def get_last_email_text(self, IMAP_SERVER, USERNAME, PASSWORD):

        # Подключение к почтовому серверу
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(USERNAME, PASSWORD)

        # Выбор почтового ящика
        mail.select('INBOX')

        # Поиск последнего письма
        result, data = mail.search(None, 'ALL')

        # Проверка на пустую почту
        if len(data[0].split()) == 0:
            mail.close()
            mail.logout()
            return None

        last_email_id = data[0].split()[-1]
        result, data = mail.fetch(last_email_id, '(RFC822)')

        # Извлечение текста письма
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        text = ""

        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    text = part.get_payload(decode=True).decode('utf-8')
        else:
            text = email_message.get_payload(decode=True).decode('utf-8')

        mail.close()
        mail.logout()
        return text

    def run(self):

        try:
            email_text = self.get_last_email_text(self.IMAP_SERVER, self.USERNAME, self.PASSWORD)

            if email_text is None:
                self.send_code.emit("Почтовый ящик пуст")
                return

            match = re.search(self.regular_string, email_text)

            if match:
                code = match.group(1) if match.group(1) else match.group(0)
                self.send_code.emit(code)
            else:
                self.send_code.emit("Код не найден.")

        except imaplib.IMAP4_SSL.error:
            self.send_code.emit("Ошибка подключения")
        except imaplib.IMAP4.error:
            self.send_code.emit("Неверные данные")
        except Exception as e:
            print(e)
