import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=29bf8de6e58678fa1d88d9b75b2a310a&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']

# Load data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_df = pickle.load(open('movie.pkl', 'rb'))  # keep as DataFrame

# Title
st.title('Movie Recommender System')

# Recommendation function
def recommend(movie_title):
    movie_index = movies_df[movies_df['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_df.iloc[i[0]]['movie_id']  # fixed indexing
        recommendations.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))  # fixed to use movie_id
    return recommendations, recommended_movies_posters

# Dropdown
option = st.selectbox(
    "Select a movie:",
    movies_df['title'].values
)

# Recommend button
if st.button("Recommend"):
    names, posters = recommend(option)

    cols = st.columns(len(names))  # Create as many columns as needed
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_container_width=True)
            st.caption(name)
