import csv
import re

from pymongo import MongoClient



def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    mongo_bd = client[db]
    tickets_collection = mongo_bd['tickets']

    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        row_list = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = dict(row)
            row['Цена'] = int(row['Цена'])
            row_list.append(row)
        tickets_collection.insert_many(row_list)
        # print(tickets_collection)




def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке, например "Seconds to"),
    и вернуть их по возрастанию цены
    """

    regex = re.compile('укажите регулярное выражение для поиска. ' \
                       'Обратите внимание, что в строке могут быть специальные символы, их нужно экранировать')


if __name__ == '__main__':
    client = MongoClient()
    read_data('artists.csv', 'tickets_db')
