# Get-Mail-Code-Rambler

![image](https://github.com/Underneach/Get-Mail-Code-Rambler/assets/137613889/256e1b3c-b09c-4a01-ad17-b51790cb5ae0)

Писал для себя, ускоряет ручную регистрацию акков с получением кода через письмо на почту.
Работа с почтой выполняется в отдельном потоке через imap, сделана обработка ошибок и копирование кода нажатием на кнопку с ним. Поиск кода идёт по регулярке.


### Написано для Rambler, но можно поставить любой другой сервис:

IMAP_SERVER = 'imap.rambler.ru'
https://github.com/Underneach/Get-Mail-Code-Rambler/blob/3540f9192fcae0701d286f5c9d2d9051c63d1628/main.py#L209

### Сборка в EXE
1. pip install -r requirements.txt
2. запустить build.bat
