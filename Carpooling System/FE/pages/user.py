import streamlit as st
from main import get_db_connection
import pandas as pd


def app():
    st.title('Welcome to the User Page')
    
    menu = st.selectbox('Select your option', ['User Operations','Trip Operations','Feedback Operations'])
    if menu=='User Operations':
         choice = st.selectbox('Operations', ['Create User','View User','Update User', 'Delete User'])
         if choice == 'Create User':
            create_user()
         elif choice == 'View User':
            read_users()
         elif choice == 'Update User':
            update_user()
         elif choice == 'Delete User':
            delete_user()

    if menu=='Trip Operations':
        st.subheader('Here, you will only be able to view trips\n')
        st.subheader('To join a trip or cancel a trip , head over to procedures\n')
        st.markdown('link => http://localhost:8501/procedures')
        read_trips()

    if menu=='Feedback Operations':
        st.subheader('Here, you will only be able to view Feedbacks\n')
        st.subheader('To perform Feedback Operations , head over to procedures\n')
        st.markdown('link => http://localhost:8501/procedures')
        read_feedbacks()
    #     choice = st.selectbox('Select your option', ['Create a Trip','View Trips', 'Update a Trip','Delete a Trip'])
    #     if choice == 'Create a Trip':
    #         create_trip()
    #     elif choice == 'View Trips':
    #         read_trips()
    #     elif choice == 'Update a Trip':
    #         update_trip()
    #     elif choice == 'Delete a Trip':
    #         create_car()
    # if choice == 'Login':
    #     login_section()
    



def create_user():
    conn = get_db_connection()
    cursor = conn.cursor()

    u_name = st.text_input('Name')
    u_email = st.text_input('Email')
    u_password = st.text_input('Password', type='password')



    if st.button('Create Account'):
        insert_query = "INSERT INTO users (user_name, user_email, user_password) VALUES (%s, %s, %s)"
        insert_values = (u_name, u_email, u_password)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('User created successfully!')

    st.subheader('To join a trip or cancel a trip and give/remove feedbacks , head over to procedures\n')
    st.markdown('link => http://localhost:8501/procedures')

    cursor.close()
    conn.close()

def read_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    query="select * from users"
    cursor.execute(query)
    view = cursor.fetchall()
    conn.commit()
    st.title("Users")
    st.table(pd.DataFrame(view, columns=["user_id", "user_name", "user_email","user_password", "trip_id", "feedback_id"]))    
    cursor.close()
    conn.close()

def update_user():
    conn = get_db_connection()
    cursor = conn.cursor()


    user_id = st.text_input('User ID:')

    # Select column to update
    update = st.selectbox('Update What', ['user_name', 'user_email', 'user_password', 'trip_id', 'feedback_id'])

    # Construct update query based on selected column
    if update == 'user_name':
        new_name = st.text_input('New Name')
        query = f"UPDATE users SET user_name = '{new_name}' WHERE user_id = {user_id}"

    elif update == 'user_email':
        new_email = st.text_input('New Email')
        query = f"UPDATE users SET user_email = '{new_email}' WHERE user_id = {user_id}"

    elif update == 'user_password':
        new_user_password = st.text_input('New user_password')
        query = f"UPDATE users SET user_password = '{new_user_password}' WHERE user_id = {user_id}"

    elif update == 'trip_id':
        new_trip_id = st.text_input('New trip_id')
        query = f"UPDATE users SET trip_id = '{new_trip_id}' WHERE user_id = {user_id}"

    elif update == 'feedback_id':
        new_feedback_id = st.text_input('New feedback_id')
        query = f"UPDATE users SET feedback_id = '{new_feedback_id}' WHERE user_id = {user_id}"

    # Execute update query
    if st.button('Update'):
        cursor.execute(query)
        conn.commit()
        st.success('User information updated successfully.')
    conn.close()

def delete_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    user_id = st.text_input('User ID:')
    d=f"delete from users where user_id={user_id}"
    if st.button('Delete'):
        cursor.execute(d)
        conn.commit()
        st.success('User information deleted successfully.')
    cursor.close()
    conn.close()




def read_trips():
    conn = get_db_connection()
    cursor = conn.cursor()
    query="select * from trips"
    cursor.execute(query)
    view = cursor.fetchall()
    conn.commit()
    st.title("Trips")
    st.table(pd.DataFrame(view, columns=["trip_id", "tri_name", "source","destination","trip_status", "schedule", "seating_capacity", "car_id"]))    
    cursor.close()
    conn.close()

def read_feedbacks():
    conn = get_db_connection()
    cursor = conn.cursor()
    query="select * from feedbacks"
    cursor.execute(query)
    view = cursor.fetchall()
    conn.commit()
    st.title("Feedback Values")
    st.table(pd.DataFrame(view, columns=["feedback_id", "rating"]))    
    cursor.close()
    conn.close()

# Run the app
app()
