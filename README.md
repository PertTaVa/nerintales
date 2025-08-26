# 🧩 NERINTALES

**NERINTALES** — a prototype system for Named Entity Recognition (NER) and intertextuality analysis in fairy tales in Russian, Finnish, and Swedish.

---

## About the Project
This project allows you to:  
- Upload a fairy tale text in three languages: Russian, Finnish, Swedish  
- Extract named entities using **spaCy** and **Stanza**  
- Analyze intertextuality by comparing entities  
- View results through a **Flask web interface**

## Contacts
GitHub @PertTaVa 
---

# 🧩 NERINTALES 

**NERINTALES** — прототип системы для извлечения именованных сущностей (NER) и анализа интертекстуальных связей в сказках на русском, финском и шведском языках.

## О проекте
Этот проект позволяет:
- Загружать текст сказки на трёх языках: русский, финский, шведский
- Извлекать именованные сущности с помощью spaCy и Stanza
- Анализировать интертекстуальность через сравнение сущностей
- Просматривать результаты через веб-интерфейс на Flask

## Как запустить
1. Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\Activate.ps1  # Windows PowerShell
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    python -m spacy download ru_core_news_sm
    python -c "import stanza; stanza.download('fi'); stanza.download('sv')"
    ```

3. Запустите приложение:
    ```bash
    python run.py
    ```

4. Откройте в браузере:
    ```
    http://127.0.0.1:5000
    ```
## Структура проекта

- `run.py` — точка входа Flask приложения
- `app/` — папка с кодом веб-приложения и шаблонами
- `src/` — код для извлечения сущностей и анализа
- `requirements.txt` — список зависимостей

## Контакты
Татьяна Перцева - автор проекта
GitHub @PertTaVa 

---

