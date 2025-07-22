import streamlit as st
import pandas as pd
from pandas import json_normalize
from st_aggrid import AgGrid
from datetime import datetime

from genres.service import GenreService
from movies.service import MovieService
from actors.service import ActorService


def show_movies():
    movies_service= MovieService()
    movies=movies_service.get_movies()

    if movies:
        st.title("Lista de Filmes")
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            key="movies_grid",
            enable_enterprise_modules=True,
        ),
    else:
        st.warning('Nenhum filme encontrado.')
    st.divider()

    st.title("Cadastrar novo filme")
    title = st.text_input("Titulo do filme")

    release_date= st.date_input(
        label='Data de lançamento',
        max_value = datetime.today(),
        format = 'DD/MM/YYYY'
    )

    genres_service=GenreService()
    genres=genres_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area('Resumo')

    if st.button("Cadastrar"):
        new_movie= movies_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_ids,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadstrar o filme verifique os campos ')