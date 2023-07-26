import pymongo

# MongoDB connection details
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = mongo_client["sample_database"]  # Replace with your desired database name
collection = db["sample_collection"]  # Replace with your desired collection name

def insert_data():
    # Sample data to be inserted
    data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Alice", "age": 25, "city": "San Francisco"},
        {"name": "Bob", "age": 35, "city": "Los Angeles"}
    ]

    # Insert the data into the collection
    collection.insert_many(data)
    print("Data inserted successfully!")

def retrieve_data():
    # Retrieve all documents from the collection
    all_documents = collection.find()
    for doc in all_documents:
        print(doc)

    # Query for specific documents
    query = {"city": "New York"}
    new_yorkers = collection.find(query)
    print("New Yorkers:")
    for doc in new_yorkers:
        print(doc)

if __name__ == "__main__":
    # Insert data into the collection
    insert_data()

    # Retrieve and display the data from the collection
    retrieve_data()
