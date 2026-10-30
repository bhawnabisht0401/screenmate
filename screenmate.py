import pandas as pd

movies = pd.read_csv("movies.csv")

print(movies.head())
print(movies.columns)
print(len(movies))
movie = movies[movies["title"] == "Toy Story (1995)"]

print(movie)
print(movie["genres"])
genres = movie["genres"].iloc[0]

print(genres)
genre_list = genres.split("|")

print(genre_list)
for genre in genre_list:
    print(genre)

other_movie = movies[movies["title"] == "Jumanji (1995)"]

print(other_movie)
other_genres = other_movie["genres"].iloc[0]

print(other_genres)
other_genre_list = other_genres.split("|")

print(other_genre_list)
common_genres = set(genre_list) & set(other_genre_list)

print(common_genres)
similarity = len(common_genres)

print(similarity)
all_genres = set(genre_list) | set(other_genre_list)

print(all_genres) 
similarity_score = len(common_genres) / len(all_genres)

print(similarity_score)
similarity_percentage = similarity_score * 100

print(similarity_percentage)
# Compare Toy Story with all movies

# ScreenMate - Movie Recommendation System

# Get the selected movie's genres
print("Welcome to ScreenMate!")

movie_title = input("Enter a movie name exactly as shown in the dataset: ")


selected_movie = movies[
    movies["title"].str.lower().str.contains(movie_title.lower(), regex=False)
]

if selected_movie.empty:
    print("Movie not found. Please check the movie title.")
    exit()

movie_title = selected_movie.iloc[0]["title"]
genre_list = selected_movie["genres"].iloc[0].split("|")

# Compare with other movies
similarity_results = []

for index, row in movies.iterrows():

    # Do not recommend the selected movie itself
    if row["title"] == movie_title:
        continue

    current_genres = row["genres"].split("|")

    common = set(genre_list) & set(current_genres)

    score = len(common)

    similarity_results.append((row["title"], score))

# Sort from highest similarity to lowest
similarity_results.sort(key=lambda x: x[1], reverse=True)

# Display Top 5
print("\nScreenMate - Top 5 Movie Recommendations")

for title, score in similarity_results[:5]:
    print(title, "-", score, "common genres")