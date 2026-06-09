dict1 = {
    1: 20,
    'name': 'ent',
    'spec': 'neck/head',
    'age': 45,
    'address': {
        'street': 'a1 kalam',
        'cross': '15th',
        'city': 'kolam',
        'state': 'TN'
    }
}

print(dict1)

dict1.update({'email': 'kannisam@gmail.com'})
dict1['address']['zip'] = 879002
print(dict1)