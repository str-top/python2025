import pickle

# Исходный словарь
data = {
    'id': 5192,
    'media': {
        'spoiler': False,
        'photo': {
            '_': 'Photo',
            'id': 52716568027271,
            'sizes': [
                {
                    '_': 'PhotoStrippedSize',
                    'type': 'i',
                    'bytes': b'\x01\x02\x03...'
                },
                {
                    '_': 'PhotoSize',
                    'size': 45678
                }
            ]
        }
    }
}

serialized_data = pickle.dumps(data)

print("Сериализованные данные:", serialized_data)

deserialized_data = pickle.loads(serialized_data)

print("Восстановленный словарь:", deserialized_data)

assert data == deserialized_data, "Данные не совпадают после сериализации и десериализации"
