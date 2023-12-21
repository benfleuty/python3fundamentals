contacts = {
    'number': 4,
    'students':
        [
            {'name':'Ben Fleuty', 'email': 'ben@example.com'},
            {'name':'Sven Fleuty', 'email': 'sven@example.com'},
            {'name':'Jen Fleuty', 'email': 'jen@example.com'},
            {'name':'Ken Fleuty', 'email': 'ken@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])