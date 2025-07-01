import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

actors = [
    {"id": 1, "name": "Stalone"},
    {"id": 2, "name": "The rock"},
    {"id": 3, "name": "Vin DIesel"},
]


def show_actors():
    st.title("Lista de Atores/Atrizes")

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key="actors_grid",
        enable_enterprise_modules=True,
    ),

    st.divider()

    st.title("Cadastrar novo Ator")
    name = st.text_input("Nome do ator")
    if st.button("Cadastrar"):
        st.success(f"Atior {name} cadastrado com sucesso")
