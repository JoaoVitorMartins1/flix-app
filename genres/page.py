import streamlit as st
import pandas as pd
from pandas import json_normalize
from st_aggrid import AgGrid
from genres.service import GenreService

def show_genres():
    genre_service= GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write("Lista de generos")
        genres_df =json_normalize(genres)
        AgGrid(
            data=genres_df,
            key="genres_grid",
            enable_enterprise_modules=True,
        ),
    else:
        st.warning("NENHUM GENERO CADASTRADO")

    st.divider()

    st.title("Cadastrar novo genero")
    name = st.text_input("Nome do genero")
    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(name=name)
        st.write("RESPOSTA DA API:", new_genre)

        if new_genre and "error" not in new_genre:
            st.success("Gênero cadastrado com sucesso!")
            st.rerun()
        else:
            st.error("ERRO AO CADASTRAR, VERIFIQUE OS CAMPOS")