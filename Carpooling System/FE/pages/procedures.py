import streamlit as st
from main import get_db_connection
import pandas as pd


def app():
    st.title('Welcome to the Procedures Page')
    
    menu = st.selectbox('Select your option', ['User Procedures','Driver Procedures','Trip Procedures', 'Feedback Procedures'])
    if menu=='User Procedures':
         choice = st.selectbox('Operations', ['Book a Trip','Cancel a Trip'])
         if choice == 'Book a Trip':
            book_trip()
         elif choice == 'Cancel a Trip':
            cancel_trip()


    if menu=='Driver Procedures':
         choice = st.selectbox('Procedures', ['Add a Trip','Remove a Trip','Add a Car', 'Remove a Car', 'Set Status to Complete'])
         if choice == 'Add a Trip':
            host_trip()
         elif choice == 'Remove a Trip':
            delete_trips()
         elif choice == 'Add a Car':
            diver_car_add()
         elif choice == 'Remove a Car':
            driver_car_rm()
         elif choice == 'Set Status to Complete':
             driver_car_set()

    if menu=='Trip Procedures':
         choice = st.selectbox('Procedures', ['Add a Car', 'Remove a Car'])
         if choice == 'Add a Car':
            trip_car_add()
         elif choice == 'Remove a Car':
            trip_car_rm()

    if menu=='Feedback Procedures':
         choice = st.selectbox('Procedures', ['Give a Feedback', 'Remove a given Feedback'])
         if choice == 'Give a Feedback':
            feedback_add()
         elif choice == 'Remove a given Feedback':
            feedback_rm()



def book_trip():
    conn = get_db_connection()
    cursor = conn.cursor()

    u_id = st.text_input('User ID')
    t_id = st.text_input('Trip ID')

    if st.button('Book Trip'):
        insert_query = "call add_user_trip(%s,%s);"
        insert_values = (u_id, t_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Trip booked successfully!')

    cursor.close()
    conn.close()

def cancel_trip():
    conn = get_db_connection()
    cursor = conn.cursor()

    u_id = st.text_input('User ID')
    t_id = st.text_input('Trip ID')

    if st.button('Cancel Trip'):
        insert_query = "call rm_user_trip(%s,%s);"
        insert_values = (u_id, t_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Trip cancelled successfully!')

    cursor.close()
    conn.close()


def feedback_add():
    conn = get_db_connection()
    cursor = conn.cursor()

    t_id=st.text_input('Trip ID')
    u_id = st.text_input('User ID')
    f_id = st.text_input('Feedback value (1-5)')

    if st.button('Submit Feedback'):
        insert_query = "call add_user_feedback(%s,%s,%s);"
        insert_values = (t_id, u_id, f_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Feedback Submitted!')

    cursor.close()
    conn.close()

def feedback_rm():
    conn = get_db_connection()
    cursor = conn.cursor()

    u_id = st.text_input('User ID')
    f_id = st.text_input('Feedback value')

    if st.button('Undo Feedback'):
        insert_query = "call rm_user_feedback(%s,%s);"
        insert_values = (u_id, f_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Feedback Removed!')

    cursor.close()
    conn.close()

def host_trip():
    conn = get_db_connection()
    cursor = conn.cursor()

    d_id = st.text_input('Driver ID')
    t_id = st.text_input('Trip ID')

    if st.button('Host Trip'):
        insert_query = "call add_driver_trip(%s,%s);"
        insert_values = (d_id, t_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Trip hosted successfully!')

    cursor.close()
    conn.close()

def delete_trips():
    conn = get_db_connection()
    cursor = conn.cursor()

    d_id = st.text_input('Driver ID')
    t_id = st.text_input('Trip ID')

    if st.button('Undo Trip Hosting'):
        insert_query = "call rm_driver_trip(%s,%s);"
        insert_values = (d_id, t_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Trip unhosted successfully!')

    cursor.close()
    conn.close()

def diver_car_add():
    conn = get_db_connection()
    cursor = conn.cursor()

    d_id = st.text_input('Driver ID')
    c_id = st.text_input('Car ID')

    if st.button('Register Your Car'):
        insert_query = "call add_driver_car(%s,%s);"
        insert_values = (d_id, c_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Car registered successfully!')

    cursor.close()
    conn.close()    

def driver_car_rm():
    conn = get_db_connection()
    cursor = conn.cursor()

    d_id = st.text_input('Driver ID')
    c_id = st.text_input('Car ID')

    if st.button('De-Register Your Car'):
        insert_query = "call rm_driver_car(%s,%s);"
        insert_values = (d_id, c_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Car de-registered successfully!')

    cursor.close()
    conn.close() 

def driver_car_set():
    conn = get_db_connection()
    cursor = conn.cursor()    

    t_id=st.text_input('Trip ID')

    if st.button('Update Status'):
        insert_query = "call trip_complete(%s);"
        insert_values = (t_id,)

        cursor.execute(insert_query, (insert_values))
        conn.commit()
        st.success('Trip Status updated successfully!')        

    cursor.close()
    conn.close() 
    
def trip_car_add():
    conn = get_db_connection()
    cursor = conn.cursor()

    t_id = st.text_input('Trip ID')
    c_id = st.text_input('Car ID')

    if st.button('associate car'):
        insert_query = "call add_trip_car(%s,%s);"
        insert_values = (t_id, c_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Car associated to the trip successfully!')  
    cursor.close()
    conn.close() 

def trip_car_rm():
    conn = get_db_connection()
    cursor = conn.cursor()

    t_id = st.text_input('Trip ID')
    c_id = st.text_input('Car ID')

    if st.button('Remove'):
        insert_query = "call rm_trip_car(%s,%s);"
        insert_values = (t_id, c_id)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Car is no lobger associated to the trip')  
    cursor.close()
    conn.close() 


# Run the app
app()
