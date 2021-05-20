# Movie ratings

film_rating = [
    'universal -> everyone can watch.',
    'pg --> General viewing, but some scenes may be unsuitable for young children.',
    '12 --> Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.',
    '15 --> No one younger than 15 may see a 15 film in a cinema.',
    '18 --> No one younger than 18 may see an 18 film in a cinema.'
]

leave = True
while leave:
    rating = input('What rating would you like to learn about? Type exit to leave.  ')
    if rating.lower() == 'exit':
        print('Thank you for checking out the ratings')
        leave = False
    elif rating.lower() == 'u':
        print(film_rating[0])
    elif rating.lower() == 'pg':
        print(film_rating[1])
    elif rating.lower() == '12':
        print(film_rating[2])
    elif rating.lower() == '15':
        print(film_rating[3])
    elif rating.lower() == '18':
        print(film_rating[4])
    else:
        print('Please enter a valid value')