import streamlit as st
import plotly.express as px
from movies.service import MovieService

def show_home():
    movie_service = MovieService()
    movie_stats= movie_service.get_movie_stats()

    st.title('Estatisticas de filme  ')

    if len(movie_stats['movies_by_genere']) > 0:
        st.subheader('Filmes por genero')
        fig=px.pie(
            movie_stats['movies_by_genere'],
            values='count',
            names='genre__name',
            title='Filmes por genero'
        )
        st.plotly_chart(fig)

    st.subheader('Total de filmes cadastrados')
    st.write(movie_stats['total_movies'])

    st.subheader('Total de avaliaçoes cadastradas ')
    st.write(movie_stats['total_reviews'])

    st.subheader('Media de estrelas nas avaliações')
    st.write(movie_stats['averege_stars'])
