import streamlit as st
import pandas as pd
from pandas import json_normalize
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime

def show_actors():
    actors_service=ActorService()
    actors=actors_service.get_actors()

    if actors:
        st.title("Lista de Atores/Atrizes")
        actors_df=pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            key="actors_grid",
            enable_enterprise_modules=True,
        ),
    else:
        st.warning('Nenhum actor cadastrado')
    st.divider()

    st.title("Cadastrar novo Ator")
    name = st.text_input("Nome do ator")
    birthday= st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown=['BRAZIL', 'USA']
    nationality= st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )



    if st.button("Cadastrar"):
        new_actor=actors_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality
        )

        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao criar ator/atriz , verifique os campos.')
