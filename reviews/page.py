import streamlit as st
import pandas as pd
from pandas import json_normalize
from st_aggrid import AgGrid
from datetime import datetime
from reviews.service import ReviewService
from movies.service import MovieService



def show_reviews():

    st.title("Lista de reviews")
    review_service= ReviewService()
    reviews=review_service.get_reviews()
    if reviews:
        st.write('LISTA DE REVIEWS')
        reviews_df=pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key="reviews_grid",
            enable_enterprise_modules=True,
        ),
    else:
        st.warning('Nenhuma avaliação encontrada')

    st.divider()

    st.title("Cadastrar novo Review")
    movie_service=MovieService()
    movies=movie_service.get_movies()
    movie_titles = {movie['title']: movie['id']for movie in movies}
    selected_movie_title=st.selectbox('Filme',list(movie_titles.keys()))

    stars=st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )
    comment = st.text_area('Comentario')

    if st.button('Cadastrar'):
        new_review=review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar avaliação verifique os campos ')