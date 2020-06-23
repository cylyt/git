import json

def main():
    mydict = {
        'name': 'Jack',
        'age ': 38,
        'qq': 123456,
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('D:\\date.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('Done')
if __name__ =='__main__':
    main()