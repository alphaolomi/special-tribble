#!/usr/bin/env python3

from tinydb import TinyDB,Query
from rich import print

db = TinyDB('app.json')
users_table = db.table('users')

users_table.insert({	
	'name': 'John Doe',
	'email' : 'johndoe@example.com',
	'dob' : '12/12/1997',
	'create_at' : '12/12/2021'

})
users_table.insert({	
	'name': 'Jane Doe',
	'email' : 'janedoe@example.com',
	'dob' : '12/08/1997',
	'create_at' : '12/12/2021'

})

# All
# print(users_table.truncate())
print(users_table.all())