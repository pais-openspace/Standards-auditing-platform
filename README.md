# Standards-auditing-platform
Standards auditing platform (SAP) is a program for auditing by standards in the quiz format



## Dev

1. Установить и настроить виртуальное окружение (`Poetry`)
2. в `src.sap_bot.config.py` прописать токен бота
3. вызвать `main.py` в корне проекта
4. Радоваться жизни


## Own Audit

Если нужно написать аудит по выбранному стандарту, можете ознакомиться с примером в папке `templates`. Вы можете добавлять любые поля или вопросы. Вы также можете изменить шаблон отчета по своему желанию. Отчет генерируется при помощи `jinjia2`, используя кастомный шаблон в конфигурации аудита.
![config report template.png](public%2Fconfig%20report%20template.png)


Всем добра!