import email
import imaplib
import re

from PyQt5.QtCore import QThread, pyqtSignal


class GetCode(QThread):
    send_code = pyqtSignal(str)

    def __init__(self, mail_data, regular_string):
        super().__init__()
        self.mail_data = mail_data
        self.regular_string = regular_string

    def run(self):
        try:
            split_string = self.mail_data.split(":")
            USERNAME = split_string[0]
            PASSWORD = split_string[1]
            IMAP_SERVER = 'imap.rambler.ru'
        except IndexError:
            self.send_code.emit("Неверные данные")
            return
        try:
            # Подключение к почтовому серверу
            mail = imaplib.IMAP4_SSL(IMAP_SERVER)
            mail.login(USERNAME, PASSWORD)

            # Выбор почтового ящика (в данном случае - входящие)
            mail.select('INBOX')

            # Поиск последнего письма
            result, data = mail.search(None, 'ALL')
            latest_email_id = data[0].split()[-1]
            result, data = mail.fetch(latest_email_id, '(RFC822)')

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

            # Извлечение кода с помощью регулярного выражения
            pattern = self.regular_string
            match = re.search(pattern, text)
            if match:
                code = match.group(1)
                self.send_code.emit(code)
            else:
                self.send_code.emit("Код не найден.")

            # Закрытие соединения с почтовым сервером
            mail.close()
            mail.logout()

        except imaplib.IMAP4_SSL.error as e:
            self.send_code.emit("Ошибка подключения")
        except imaplib.IMAP4.error as e:
            self.send_code.emit("Неверные данные")
        except Exception as e:
            print(e)
