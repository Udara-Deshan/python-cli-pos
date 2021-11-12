from os import waitpid
import json
import os
from pprint import pprint

__db_location__ = "db/item"
__item_folder__ = f"{__db_location__}/items"
__item_last_id__ = f"{__db_location__}/item_id.db"


def init():
    db()


def db():
    os.makedirs(__item_folder__)


def set_command_and_params(command, params):
    if command == "init":
        init()
    elif command == "create":
        __item_create__()
    elif command == "find":
        __item_find__(*params)
    elif command == "findAll":
        __item_all__()
    elif command == "search":
        __item_search__(*params)


def __item_create__():
    item = Item()
    item.name = input("Enter item name : ")
    item.qty = input("Enter item qty : ")
    item.price = input("Enter item base price : ")
    item.save()
    print("Item is success added")


def __item_find__(item_id):
    item = Item()
    item.find(item_id)
    print(item.item_id, item.name, item.qty, item.price)


def __item_all__():
    item = Item()
    items = item.all()
    for item in items:
        print(item.item_id, item.name, item.qty, item.price)
    # pprint(items)


def get_items():
    item = Item()
    return item.all()


def __item_search__(key, value):
    item = Item()
    results = item.search(key, value)
    pprint(results)


class Item:
    def __init__(self):
        self.item_id = None
        self.price = None
        self.qty = None
        self.name = None
        if os.path.exists(__item_last_id__):
            with open(__item_last_id__, "r") as last_id_f:
                self.last_id = int(last_id_f.readline())
        else:
            self.last_id = 0

    def save(self):
        item_id = self.last_id + 1
        _data_ = {
            "itemId": item_id,
            "name": self.name,
            "qty": self.qty,
            "price": self.price
        }
        with open(f"{__item_folder__}/{item_id}.db", "w") as item_file:
            json.dump(_data_, item_file)

        self.last_id += 1
        with open(__item_last_id__, "w") as f:
            f.write(str(self.last_id))

    @staticmethod
    def all():
        item_file_names = os.listdir(__item_folder__)
        items = []
        for item_file_name in item_file_names:
            item = Item()
            Item.__get_item_by_path(
                item, f"{__item_folder__}/{item_file_name}")
            items.append(item)
        return items

    def find(self, item_id):
        Item.__get_item_by_path(self, f"{__item_folder__}/{item_id}.db")

    def __get_item_by_path(self, path):
        with open(path, "r") as item_file:
            _data_ = json.load(item_file)
            self.item_id = int(_data_["itemId"])
            self.name = _data_["name"]
            self.qty = _data_["qty"]
            self.price = _data_["price"]

    def search(self, key, value):
        items = self.all()
        result_items = []
        for item in items:
            item_value = getattr(item, key)
            if item_value == value:
                result_items.append(item)
        return result_items

    def __repr__(self):
        return f"itemId:{self.item_id},name:{self.name},price:{self.qty},price:{self.price}"

    def __str__(self):
        return f"itemId:{self.item_id},name:{self.name},price:{self.qty},price:{self.price}"
