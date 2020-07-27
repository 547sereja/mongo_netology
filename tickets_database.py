import csv
import re

from pymongo import MongoClient
import pymongo


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    mongo_db = client[db]
    tickets_collection = mongo_db['tickets']

    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        row_list = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Цена'] = int(row['Цена'])
            row_list.append(row)
        tickets_collection.insert_many(row_list)
        print(tickets_collection)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    mongo_db = client[db]
    tickets_collection = mongo_db['tickets']
    sorted_list = list(tickets_collection.find().sort('Цена', pymongo.ASCENDING))
    print(sorted_list)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """
    mongo_db = client[db]
    tickets_collection = mongo_db['tickets']
    regex = re.compile(name)
    sorted_list = list(tickets_collection.find({'Исполнитель': regex}).sort('Цена', pymongo.ASCENDING))
    print(sorted_list)


if __name__ == '__main__':
    client = MongoClient()
    read_data('artists.csv', 'tickets_db')
    find_cheapest('tickets_db')
    find_by_name('Seconds to', 'tickets_db')
