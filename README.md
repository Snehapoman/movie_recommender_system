# movie_recommender_system

This is a content-based movie recommendation web app built with Streamlit that suggests movies similar to the one selected by the user. The recommendation engine uses cosine similarity to calculate similarity scores between movies based on their content features.

## Features
-Interactive UI built with Streamlit.<br>
-Content-based filtering using cosine similarity.<br>
-Top 5 similar movie recommendations for a selected movie.<br>
-Movie posters fetched from The Movie Database (TMDb) API.<br>
-Fast recommendations powered by pre-computed similarity matrix (similarity.pkl).<br>

## How It Works
Data Preparation

A dataset of movies is processed and stored as movie.pkl (containing movie IDs, titles, and other features).
Feature vectors for movies are generated from their metadata (such as genres, keywords, cast, etc.).
Cosine similarity is computed between all pairs of movies, and the resulting similarity matrix is stored in similarity.pkl.<br>

Recommendation Process<br>

When a user selects a movie, the app finds its index in the dataset.
Retrieves similarity scores from the precomputed matrix.
Sorts the scores to find the top 5 most similar movies.
Fetches the movie posters using TMDb API.
Displays recommendations in a visually appealing layout.

Cosine Similarity<br>

Cosine similarity measures the cosine of the angle between two vectors in a multi-dimensional space.
It is ideal for measuring similarity between text/metadata-based feature vectors, regardless of their magnitude.

