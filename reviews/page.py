import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

reviews = [
    {"id": 1, "stars": 3},
    {"id": 2, "stars": 1},
    {"id": 3, "stars": 4},
]


def show_reviews():
    st.title("Lista de reviews")

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key="reviews_grid",
        enable_enterprise_modules=True,
    ),

    st.divider()

    st.title("Cadastrar novo Review")
    name = st.text_input("Nome do filme")
    if st.button("Cadastrar"):
        st.success(f"Genero {name} cadastrado com sucesso")
