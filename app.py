import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Título de la aplicación
st.header("Análisis de vehículos usados en EE.UU.")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.write("Vista previa de los datos:")
st.dataframe(car_data)

# Casillas de verificación para elegir gráfico
show_hist = st.checkbox("Mostrar histograma de odómetro")
show_scatter = st.checkbox("Mostrar gráfico de dispersión: año vs odómetro")

# Histograma
if show_hist:
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig_hist)

# Gráfico de dispersión
if show_scatter:
    fig_scatter = px.scatter(
    car_data,
    x='model_year',
    y='odometer',
    color='paint_color',  # aquí usas una columna existente
    title='Año vs Odómetro por color'
)
    st.plotly_chart(fig_scatter)

# Mensaje final
st.write("Selecciona las casillas para visualizar los gráficos.")
