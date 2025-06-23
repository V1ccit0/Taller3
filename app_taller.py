import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="App Taller SQL", layout="centered")
st.title("Consulta interactiva a MySQL")

@st.cache_resource
def conectar():
    return mysql.connector.connect(
        host="localhost",
        port=3300,
        user="VichoBL",
        password="Vibo2511*",
        database="ANFP"
    )

conn = conectar()
query = st.text_area("Escribe tu consulta SQL", "SELECT * FROM clientes LIMIT 5")

if st.button("Ejecutar Consulta"):
    try:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error al ejecutar la consulta: {e}")
