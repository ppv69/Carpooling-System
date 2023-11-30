import streamlit as st
import mysql.connector

st.title('Car Pooling System')
st.subheader('This is just a home page please head over to other pages to perform desired operations')
st.markdown('driver page => http://localhost:8501/driver')
st.markdown('user page => http://localhost:8501/user')
st.markdown('procedures => http://localhost:8501/procedures')
st.markdown('functions => http://localhost:8501/function')
st.markdown('join => http://localhost:8501/join')

def get_db_connection():
    # Database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="carpool"
    )
    return conn