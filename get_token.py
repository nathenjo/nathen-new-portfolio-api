def get_key(db):
    collection = db['app-keys']
    result = collection.find_one()
    return result['key']
