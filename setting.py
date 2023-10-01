import os
import json


def Save_settings(self, regexp: str, imap: str) -> None:
    if os.path.exists(os.getenv('APPDATA') + '\\getmail_settings.json'):
        try:
            path = os.getenv('APPDATA')
            with open(path + '\\getmail_settings.json', 'r') as file:
                data = json.loads(file.read())
                regexp_list = data['regexp_list']
                imap_list = data['imap_list']
        except FileNotFoundError:
            pass

        if regexp_list and imap_list:
            regexp_list.append(regexp)
            regexp_list = list(set(regexp_list))
            imap_list.append(imap)
            imap_list = list(set(imap_list))
            self.ui.Textline_regular.clear()
            self.ui.Textline_regular.addItems(regexp_list)
            self.ui.Textline_imap.clear()
            self.ui.Textline_imap.addItems(imap_list)

            data = {
                'regexp_list': regexp_list,
                'imap_list': imap_list
            }

            with open(path + '\\getmail_settings.json', 'w') as file:
                file.write(json.dumps(data))
        else:
            data = {
                'regexp_list': [regexp],
                'imap_list': [imap]
            }
            self.ui.Textline_regular.addItems(regexp)
            self.ui.Textline_imap.addItems(imap)
            with open(path + '\\getmail_settings.json', 'w') as file:
                file.write(json.dumps(data))
    else:
        data = {
            'regexp_list': [regexp],
            'imap_list': [imap]
        }
        self.ui.Textline_regular.addItems(regexp)
        self.ui.Textline_imap.addItems(imap)
        with open(os.getenv('APPDATA') + '\\getmail_settings.json', 'w') as file:
            file.write(json.dumps(data))


def Load_settings(self) -> None:

    if os.path.exists(os.getenv('APPDATA') + '\\getmail_settings.json'):
        try:
            path = os.getenv('APPDATA')
            with open(path + '\\getmail_settings.json', 'r') as file:
                data = json.loads(file.read())
                regexp_list = list(set(data['regexp_list']))
                imap_list = list(set(data['imap_list']))
            self.ui.Textline_regular.addItems(regexp_list)
            self.ui.Textline_imap.addItems(imap_list)
        except FileNotFoundError:
            pass
