from task2.connection import Connection


def get_all_cats(connection: Connection):
    try:
        cats = connection.get_collection().find()
        for cat in cats:
            print(f"Name: {cat['name']}  Age: {cat['age']}  Features: {" ".join(cat['features'])}")
    except Exception as e:
        print(f"Error: {e}")


def find_by_name(connection: Connection, name):
    try:
        cats = connection.get_collection().find({"name": name})
        print("Результат пошуку:")
        i = 1
        for cat in cats:
            print(f"{i}  Name: {cat['name']}  Age: {cat['age']}  Features: {" ".join(cat['features'])}")
            i += 1
    except Exception as e:
        print(f"Error: {e}")


def change_age(connection, name_to_search, new_age):
    try:
        result = connection.get_collection().update_one({"name": name_to_search}, {"$set": {"age": int(new_age)}})
        message = "Вік змінено" if result.matched_count > 0 else "Нічого не змінилось"
        print(message)
    except ValueError as e:
        print("Невірний вік")
    except Exception as e:
        print(f"Error: {e}")


def add_feature(connection, name, new_feature):
    try:
        result = connection.get_collection().update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.modified_count > 0:
            print(f"Характеристика додана коту.")
        else:
            print("Нічого не змінилось")
    except Exception as e:
        print(f"Error: {e}")


def delete_cat(connection, name):
    try:
        result = connection.get_collection().delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кіт видалений.")
        else:
            print("Нічого не змінилось")
    except Exception as e:
        print(f"Error: {e}")


def delete_all(connection):
    try:
        connection.get_collection().delete_many({})
        print("Колекція була очищена")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    connection = Connection()

    while True:
        print("---------- М е н ю ----------")
        print("1. Cписок віх котів")
        print("2. Пошук")
        print("3. Змінити вік")
        print("4. Додати фічу")
        print("5. Видалити кота")
        print("6. Видалити всіх котів")

        choice = input("Введіть число >>> ")
        if choice == "1":
            get_all_cats(connection)
        elif choice == "2":
            name_to_search = input("Імʼя кота >>> ")
            find_by_name(connection, name_to_search)
        elif choice == "3":
            name_to_search = input("Імʼя кота >>> ")
            new_age = input("Введіть вік >>> ")
            change_age(connection, name_to_search, new_age)
        elif choice == "4":
            name_to_search = input("Імʼя кота >>> ")
            new_feature = input("Введіть фічу >>> ")
            add_feature(connection, name_to_search, new_feature)
        elif choice == "5":
            name_to_search = input("Імʼя кота >>> ")
            delete_cat(connection, name_to_search)
        elif choice == "6":
            delete_all(connection)
        else:
            print("Спробуй ще.")
