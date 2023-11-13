from tinydb import TinyDB


test_db = [
    {
        'name': 'Form1',
        'user_name': 'text',
        'lead_email': 'email',
        'phone_number': 'phone',
    },
    {
        'name': 'Form2',
        'Email': 'email',
        'Phone': 'phone',
        'Date': 'date',
        'Description': 'text',
    },
    {
        'name': 'Form3',
        'First_name': 'text',
        'Last_name': 'text',
        'Phone': 'phone',
        'Address': 'text',
    },
    {
        'name': 'Form4',
        'Date': 'date',
        'Description': 'text',
    }
]


db = TinyDB('app/services/db.json')


# db.insert_multiple(test_db)


# for item in db:
#     print(item)
