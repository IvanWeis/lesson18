# Часть3. ФОРМИРОВАНИЕ ОТЧЕТОВ СПОМОЩЬЮ ЗАПРОСОВ

# Импортируем необходимые библиотеки
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# В текущей папке создаем файл своей БД  hh.sqlite
engine = create_engine('sqlite:///hh.sqlite', echo=False) # echo=False - эхо ОТКЛЮЧЕНО, чтобы не мешалось

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

# ПИШЕМ ЗАПРОСЫ НА ВЫБОРКУ ДАННЫХ ИЗ ТАБЛИЦ:
Session = sessionmaker(bind=engine)
session = Session() # создаем сессию

# выбрать ВСЕ записи таблицы region, поля id  и name:
result = session.query(Region.id, Region.name).all()
print('Все записи таблицы region :')
print(result)
print()

# выбрать ВСЕ записи таблицы vacancy, поля id, name, region_id:
result = session.query(Vacancy.id, Vacancy.name, Vacancy.region_id).all()
print('Все записи таблицы vacancy :')
print(result)
print()

# выбрать записи таблицы vacancy, поля id, name, region_id, ТОЛЬКО для Москвы:
result = session.query(Vacancy.id, Vacancy.name, Vacancy.region_id).filter(Vacancy.region_id == 'Москва').all()
print('Вакансии из региона "Москва" :')
print(result)
