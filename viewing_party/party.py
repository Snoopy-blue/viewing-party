# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    else:
        return None

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie) 

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie) 
    
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]: # Loop through movies in a list. 
        # user_data["watchlist"] = list contains mutiple dictionaries
        # movie = each element of the list, dictionary contains title, genere, rating. 

        if movie["title"] == title: # dictionary[key], value of "title"
            #movie_to_watch = movie
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)      

    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
# Return 0.0 if the user has not watched any movies
    if len(user_data["watched"]) == 0:
        return 0.0

    total_rating = 0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]
# Calculate and return the average rating
    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_counts = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]

        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1
# Find the genre with the highest count
    max_count = 0
    most_watched_genre = None

    for genre, count in genre_counts.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    onlyme_watched = []
    friends_watched_list = get_friends_watched_list(user_data)
    me_watched_list = user_data["watched"]

    for movie in me_watched_list:
        if movie not in friends_watched_list:
            onlyme_watched.append(movie)

    return onlyme_watched 

def get_friends_unique_watched(user_data): 
    onlyfriends_watched = []
    friends_watched_list = get_friends_watched_list(user_data)
    me_watched_list = user_data["watched"]

    for movie in friends_watched_list:
        if movie not in me_watched_list:
            onlyfriends_watched.append(movie)

    return onlyfriends_watched   

"""Function below is a helper funciton, if there are mutiple friends with their watched lists, we want to have a clean summed friends watched list without any duplication to work on."""
def get_friends_watched_list(user_data):
    friends_watched_list = []
    for movie_watched in user_data["friends"]:
        for movie in movie_watched["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)

    return friends_watched_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []

    onlyfriends_watched_list = get_friends_unique_watched(user_data)
    for movie in onlyfriends_watched_list:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie["genre"] == most_watched_genre:
            recommendations.append(movie)


    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []

    friends_watched_list = get_friends_watched_list(user_data)

    for movie in user_data["favorites"]:
        if movie not in friends_watched_list:
            recommendations.append(movie)

    return recommendations