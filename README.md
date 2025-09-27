🧩 NERINTALES

NERINTALES — a prototype system for Named Entity Recognition (NER) and intertextuality analysis in Finnish, Swedish and Russian languages 

About the Project
This project allows you to:  
- Upload a text
- Extract named entities using spaCy and Stanza
- Analyze intertextuality by comparing entities  
- View results through a Flask web interface

Contacts
GitHub @PertTaVa 


🧩 NERINTALES 
NERINTALES — прототип системы для извлечения именованных сущностей (NER) и анализа интертекстуальных связей на финском, шведском и русском языках.
О проекте
Этот проект позволяет:
- Загружать текст
- Извлекать именованные сущности (NER) с помощью spaCy и Stanza
- Анализировать интертекстуальность через сравнение сущностей
- Просматривать результаты через веб-интерфейс на Flask.
Как запустить
1. Создайте и активируйте виртуальное окружение:
    bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\Activate.ps1  # Windows PowerShell
2. Установите зависимости:
    bash
    pip install -r requirements.txt
    python -m spacy download ru_core_news_sm
    python -c "import stanza; stanza.download('fi'); stanza.download('sv')"
3. Запустите приложение:
    bash
    python run.py
4. Откройте в браузере:
    http://127.0.0.1:5000
Структура проекта:
- run.py — точка входа Flask приложения
- app/ — папка с кодом веб-приложения и шаблонами
- src/ — код для извлечения сущностей и анализа
- requirements.txt — список зависимостей
Контакты:
Татьяна Перцева - автор проекта
GitHub @PertTaVa 

---

