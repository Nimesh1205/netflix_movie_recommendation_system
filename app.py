import streamlit as st
import pandas as pd
import pickle

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")


selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies["Titles"].values
)

def recommend(movie):
    movie_index = movies[movies["Titles"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].Titles)
    return recommended_movies

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write("### Recommended Movies:")
    for idx, name in enumerate(recommendations, start=1):
        st.write(f"**{idx}.** {name}")        