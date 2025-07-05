import json
import base64

def serialize(data):
    """Сериализация словаря с обработкой бинарных данных"""
    def _encode_binary(obj):
        if isinstance(obj, dict):
            return {k: _encode_binary(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [_encode_binary(v) for v in obj]
        elif isinstance(obj, bytes):
            return {'__binary__': base64.b64encode(obj).decode('utf-8')}
        return obj
    
    return json.dumps(_encode_binary(data), indent=2)

def deserialize(json_str):
    """Десериализация с восстановлением бинарных данных"""
    def _decode_binary(obj):
        if isinstance(obj, dict):
            if '__binary__' in obj:
                return base64.b64decode(obj['__binary__'])
            return {k: _decode_binary(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [_decode_binary(v) for v in obj]
        return obj
    
    return _decode_binary(json.loads(json_str))

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
                    'bytes': b'\x01\x02\x03\x04\x05'  # Пример бинарных данных
                },
                {
                    '_': 'PhotoSize',
                    'size': 45678
                }
            ]
        }
    }
}

# Сериализация
serialized = serialize(data)
print("Сериализованные данные:")
print(serialized)

# Десериализация
deserialized = deserialize(serialized)
print("\nДесериализованные данные:")
print(deserialized)

assert deserialized == data, "Данные не совпадают после десериализации"
print("\nПроверка пройдена: данные идентичны исходным")
