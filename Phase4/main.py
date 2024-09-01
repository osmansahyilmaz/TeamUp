from connect import connectDB
from pymongo import errors
from bson import ObjectId

def createCollection(db, collection_name):
    try:
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        else:
            print("Collection already exists")
    except Exception as e:
        print("An error occurred: ", e)

def insert_into_collection(db, collection_name, data):
    try:
        collection = db[collection_name]
        result = collection.insert_one(data)
        print("Insertion successfully completed")
        print(f"Inserted document ID: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_all_data(db, collection_name):
    try:
        collection = db[collection_name]
        result = collection.find()
        for document in result:
            print(document)
    except Exception as e:
        print(f"An error occurred: {e}")

def read_filtered_data(db, collection_name, filter):
    try:
        collection = db[collection_name]
        result = collection.find(filter)
        for document in result:
            print(document)
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_record_by_id(db, collection_name, record_id):
    try:
        collection = db[collection_name]
        query = {"_id": ObjectId(record_id)}
        result = collection.delete_one(query)
        if result.deleted_count == 1:
            print(f"Successfully deleted record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

def update_record_by_id(db, collection_name, record_id, update_fields):
    try:
        collection = db[collection_name]
        query = {"_id": ObjectId(record_id)}
        update = {"$set": update_fields}
        result = collection.update_one(query, update)
        if result.matched_count == 1:
            print(f"Successfully updated record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    db = connectDB()

    while True:
        print("Welcome to the MongoDB Interface")
        print("1 - Create a collection")
        print("2 - Read all data in a collection")
        print("3 - Read data with filtering")
        print("4 - Insert data")
        print("5 - Delete data")
        print("6 - Update data")
        print("7 - Exit")

        option = int(input("Selected option: "))

        if option == 1:
            collection_name = input("Enter collection name: ")
            createCollection(db, collection_name)
        elif option == 2:
            collection_name = input("Enter collection name: ")
            read_all_data(db, collection_name)
        elif option == 3:
            collection_name = input("Enter collection name: ")
            field = input("Enter field name to filter: ")
            value = input(f"Enter value for {field}: ")
            filter = {field: value}
            read_filtered_data(db, collection_name, filter)
        elif option == 4:
            collection_name = input("Enter collection name: ")
            data = {}
            while True:
                field = input("Enter field name (or type 'done' to finish): ")
                if field == 'done':
                    break
                value = input(f"Enter value for {field}: ")
                data[field] = value
            insert_into_collection(db, collection_name, data)
        elif option == 5:
            collection_name = input("Enter collection name: ")
            record_id = input("Enter record ID to delete: ")
            delete_record_by_id(db, collection_name, record_id)
        elif option == 6:
            collection_name = input("Enter collection name: ")
            record_id = input("Enter record ID to update: ")
            update_fields = {}
            while True:
                field = input("Enter field name to update (or type 'done' to finish): ")
                if field == 'done':
                    break
                value = input(f"Enter new value for {field}: ")
                update_fields[field] = value
            update_record_by_id(db, collection_name, record_id, update_fields)
        elif option == 7:
            break
        else:
            print("Invalid option, please try again.")
