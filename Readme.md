## Установка
1. Клонировать репозиторий
   ```bash
   git clone https://github.com/lilpep8/API_Autotests_42
   ```

2. Создать виртуальное окружение:
   ```bash
   python -m venv .venv
   ```
   ```bash
   source .venv/bin/activate  # ОС Linux/Mac
   ```
   ```bash
   .venv\Scripts\activate    # ОС Windows
   ```
   
3. Установить зависимости
   ```bash
   pip install -r requirements.txt
   ```

4. Запустить тесты
   ```bash
   pytest tests/ -v -s
   ```
