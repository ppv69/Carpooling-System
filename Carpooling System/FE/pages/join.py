import streamlit as st
import pandas as pd
from main import get_db_connection

st.title('This Page is just a bunch of join operations\n')

menu=st.selectbox('Select the join options',['Driver & Trips & Cars', 'User & Trips', 'Feedback & Users', 'Driver & User & Trips'])

if menu == 'Driver & Trips & Cars':
    conn = get_db_connection()
    cursor = conn.cursor()
    st.header('This performs inner join on drivers table, trips table and cars table\n')

    q="select driver_name, trip_name, source, destination, trip_status, schedule, seating_capacity, car_name  from drivers inner join trips on drivers.trip_id=trips.trip_id inner join cars on drivers.car_id=cars.car_id"
    cursor.execute(q)
    res=cursor.fetchall()

    columns = ["Driver Name", "Trip Name", "Source", "Destination", "Trip Status", "Schedule", "Seating Capacity", "Car Name"]
    df = pd.DataFrame(res, columns=columns)

    st.table(df)


    cursor.close()
    conn.close()


elif menu=='User & Trips':
    conn = get_db_connection()
    cursor = conn.cursor()
    st.header('This performs left join on users and trips\n')

    q="select user_name, user_email, trip_name, source, destination, schedule, feedback_id  from users left join trips on users.trip_id=trips.trip_id"

    cursor.execute(q)
    res=cursor.fetchall()

    columns=["User Name", "Email", "Trip Name", "Source", "Destination", "Schedule", "Rating"]
    df=pd.DataFrame(res, columns=columns)

    st.table(df)
    

    cursor.close()
    conn.close()

elif menu=='Driver & User & Trips':
    conn = get_db_connection()
    cursor=conn.cursor()
    st.header("This Performs full join on tables Drivers, Trips and Users\n")

    q="SELECT driver_name, driver_license, driver_email, seating_capacity, trip_name, source, destination, trip_status, schedule, user_name, user_email, feedback_id  FROM drivers LEFT JOIN trips ON drivers.trip_id = trips.trip_id LEFT JOIN users ON users.trip_id = trips.trip_id  UNION   SELECT driver_name, driver_license, driver_email, seating_capacity, trip_name, source, destination, trip_status, schedule, user_name, user_email, feedback_id FROM drivers RIGHT JOIN trips ON drivers.trip_id = trips.trip_id RIGHT JOIN users ON users.trip_id = trips.trip_id"

    cursor.execute(q)
    res=cursor.fetchall()

    columns=["Driver Name", "Driving License", "Driver Email", "Seating Capacity", "Trip Name", "Source", "Destination", "Trip Status", "Schedule", "User Name", "User Email", "Rating" ]
    df=pd.DataFrame(res, columns=columns)

    st.table(df)

    cursor.close()
    conn.close()

elif menu=='Feedback & Users':
    conn = get_db_connection()
    cursor = conn.cursor()
    st.header("This performs right join on Feedbacks table and Users Table\n")

    q="select rating, user_name, user_email, user_password, trip_id  from  feedbacks right join users on users.feedback_id=feedbacks.feedback_id"

    cursor.execute(q)
    res=cursor.fetchall()

    columns=["Ratings", "User Name", "User Email", "User Password", "Trip ID"]

    df=pd.DataFrame(res,columns=columns)

    st.table(df)

    cursor.close()
    conn.close()    