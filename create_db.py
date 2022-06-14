# Часть1. СОЗДАНИЕ БАЗЫ ДАННЫХ (декларативным способом)
# - создаем БД  hh.sqlite
# - создаем две таблицы: region и vacancy
# - связь между этими таблицами (по полю region_id таблицы vacancy) устанавливается автоматически (код писать ненадо)
#   (region_id таблицы vacancy связывается с первичным ключом id таблицы region)

# Импортируем необходимые библиотеки
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

# В текущей папке создаем файл своей БД  hh.sqlite
engine = create_engine('sqlite:///hh.sqlite', echo=True) # echo=True - эхо включено, чтобы при отладке выводились сообщения

Base = declarative_base() # создаем класс Base (класс таблиц) декларативным методом

# От класса Base создаем Класс (таблицу) region, с необходимыми полями (столбцами)
class Region(Base):   # создаем Модель (объект, таблицу в БД) Region
    __tablename__ = 'region'  # название теблицы
    id = Column(Integer, primary_key=True)  # id - первичный ключ
    name = Column(String)  # только одно поле (колонка) name - содержит имя региона
    def __init__(self, name):
        self.name = name

# От класса Base создаем Класс (таблицу) vacancy, с необходимыми полями (столбцами)
class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    name = Column(String) # здесь хранится название вакансии
    region_id = Column(Integer, ForeignKey('region.id')) # Для связи один ко многим создаем внешний ключ
    def __init__(self, name, region_id):
        self.name = name
        self.region_id = region_id

# Создание БД с соответствующими таблицами и сязями (команда на выполнение написанного выше Кода)
Base.metadata.create_all(engine)
