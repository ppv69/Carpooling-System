import streamlit as st
import pandas as pd
from main import get_db_connection
def app():
    conn = get_db_connection()
    cursor = conn.cursor()
    st.header('This function will provide the average rating of a trip\n')
    trip_id=st.text_input('Enter the Trip ID')
    if st.button('Get average'):
        q="select get_average_trip_rating (%s)"
        cursor.execute(q,(trip_id,))


        res=cursor.fetchall()
        columns = ["Average Rating"]  
        df = pd.DataFrame(res, columns=columns)

        st.write("Result:")
        st.write(df)

    cursor.close()
    conn.close()
app()