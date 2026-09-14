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

    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
