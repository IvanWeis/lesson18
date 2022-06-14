# Часть2. РЕДАКТИРОВАНИЕ БАЗЫ ДАННЫХ (три строки в таблицу region и три строки в таблицу vacance)

# Импортируем необходимые библиотеки
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

Base.metadata.create_all(engine)

# создаем записи (экземпляры класса (таблицы) - строки данной таблицы)
Session = sessionmaker(bind=engine)
session = Session() # создаем сессию

# в таблицу region добавляем три записи (три строки)
session.add_all([Region('Москва'), Region('Питер'), Region('Екатеринбург')])

# в таблицу vacancy добавляем три записи (три строки)
session.add_all([Vacancy('Python-developer', 'Москва'), Vacancy('Python-developer', 'Питер'), Vacancy('Java-developer', 'Москва')  ])

session.commit() # выполняем сессию (коммитим изменения)