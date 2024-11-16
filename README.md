# Описание
Персональный голосовой помощник, призванный облегчить некоторые рутинные задачи человека.

# Реализуемый функционал
Возможности программы включают в себя:
* Примитивное ведение диалога (приветствие, прощание, исполнение команд)
* Открытие веб-сайтов
* Сообщение времени и даты

__От прочего функционала было решено отказаться в силу сложности реализации__

# Архитектура
[Диаграмма вариантов использования](https://github.com/Tukk0/Python2024/blob/development/docs/Use-case%20diagram.png).
Список предполагаемых возможных команд (урезаны в связи со сложностью реализации) и описание их функционала приведены в виде [таблицы](https://github.com/Tukk0/Python2024/blob/development/docs/Commands.jpg).
[Диаграмма классов](https://github.com/Tukk0/Python2024/blob/development/docs/Class_diagram.jpg).
Система классов слегка изменена для большей гибкости и эффективности работы программы.

[Список зависимостей](https://github.com/Tukk0/Python2024/blob/development/docs/requirements.txt)

Инструкция по установке и запуску:
```
git clone git@github.com:Tukk0/Python2024.git VoiceAssistant
cd VoiceAssistant
pip install -r requirements.txt
cd src
python3 main.py
```
Примечание: требуется версия Python 3.10
