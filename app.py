import streamlit as st
import pickle
import pandas as pd
import requests

# Load movie data and similarity data
movies_df = pickle.load(open('movies.pkl', 'rb'))  
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = movies_df['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you like best?',
    movies_list)

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY".format(movie_id)
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except (requests.RequestException, KeyError) as e:
        st.warning(f"Couldn't fetch poster for movie ID {movie_id}")
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

def recommend(selected_movie_name):
    try:
        movie_index = movies_df[movies_df['title'].str.lower() == selected_movie_name.lower()].index[0]  
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  

        recommended_movies = []
        recommended_movies_poster = []
        
        for i in movies_list:
            movie_title = movies_df.iloc[i[0]]['title']
            recommended_movies.append(movie_title)
            movie_id = movies_df.iloc[i[0]]['id']
            poster_url = fetch_poster(movie_id)
            recommended_movies_poster.append(poster_url)

        return recommended_movies, recommended_movies_poster
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return [], []

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    
    if recommended_movie_names and recommended_movie_posters:
        # Using the current columns API instead of beta_columns
        cols = st.columns(5)
        
        for idx, (col, name, poster) in enumerate(zip(cols, recommended_movie_names, recommended_movie_posters)):
            with col:
                st.text(name)
                st.image(poster)