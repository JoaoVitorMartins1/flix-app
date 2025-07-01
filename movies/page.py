import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

movies = [
    {"id": 1, "name": "VELOZES"},
    {"id": 2, "name": "JUMANJO"},
    {"id": 3, "name": "TESTE2"},
]


def show_movies():
    st.title("Lista de Filmes")

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key="movies_grid",
        enable_enterprise_modules=True,
    ),

    st.divider()

    st.title("Cadastrar novo filme")
    name = st.text_input("Nome do filme")
    if st.button("Cadastrar"):
        st.success(f"Genero {name} cadastrado com sucesso")
