import os
from dotenv import load_dotenv # в терминале: pip install python-dotenv

load_dotenv()


class Data:

    LOGIN = os.getenv("LOGIN") # получаем переменную окружения, которую записали в файле .env
    PASSWORD = os.getenv("PASSWORD")
