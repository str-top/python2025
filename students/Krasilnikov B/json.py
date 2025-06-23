import json

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
                    # 'bytes': b'\x01\x02\x03...' 
                },
                {
                    '_': 'PhotoSize',
                    'size': 45678 
                }
            ]
        }
    }
}

with open('data.json', 'w') as f:
    json.dump(data, f)
    
    
    
with open('data.json', 'r') as f:
    data = json.load(f)

print(data)    
