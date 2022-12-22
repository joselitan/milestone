# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = [
            {'title': 'Captain', 'director': 'Chris Evans', 'year': '2008'},
            {'title': 'Iron Man', 'director': 'Robert Downey Jr', 'year': '2008'}
          ]

# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Create other functions for:
#   - listing movies
def listing_movies():
    for i in range(0, len(movies)):
        print(f'details of your movie were found {movies[i]}')
def finding_movies():
    res = None
    search_title = input("Enter the title for your movie: ")
    for movie in movies:
        if movie['title'] == search_title:
            res = movie
            break
    print("The title was found: " + str(res))


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        print(f'You are about to add a movie')
        add_movie()
    elif selection == "l":
        print(f'Here is the list of all movies added by you')
        listing_movies()
    elif selection == "f":
        print(f'Find your movie by entering title')
        finding_movies()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!