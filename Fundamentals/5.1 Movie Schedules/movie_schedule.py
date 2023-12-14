current_movies = {
    'The Grinch': '11:00am',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm',
    'Christmas Vacation': '5:00pm'
}

print('We are showing the following movies:')

for movie in current_movies:
    print(movie)

requested_movie = input('Which movie would you like the showtime for?\n')

showtime = current_movies.get(requested_movie)

if showtime:
    print(f'{requested_movie} is playing at {showtime}')
else:
    print(f'We are not showing {requested_movie}')
