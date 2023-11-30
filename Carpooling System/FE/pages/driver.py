import streamlit as st
from main import get_db_connection
import pandas as pd

# Initialize session state
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
#     st.session_state.result = ''

def app():
    st.title('Welcome to the Driver Page')
    
    menu = st.selectbox('Select your option', ['Driver Operations','Car Operations','Trip Operations'])
    if menu=='Driver Operations':
         choice = st.selectbox('Operations', ['Create Driver','View Drivers','Update Driver', 'Delete Driver'])
         if choice == 'Create Driver':
            create_driver()
         elif choice == 'View Drivers':
            read_drivers()
         elif choice == 'Update Driver':
            update_driver()
         elif choice == 'Delete Driver':
            delete_driver()
    if menu=='Car Operations':
        choice = st.selectbox('Select your option', ['Create a Car','View Cars', 'Update a Car', 'Delete a Car'])
        if choice == 'Create a Car':
            create_car()
        elif choice == 'View Cars':
            read_cars()
        elif choice == 'Update a Car':
            update_car()
        elif choice == 'Delete a Car':
            delete_car()
    if menu=='Trip Operations':
        choice = st.selectbox('Select your option', ['Create a Trip','View Trips', 'Update a Trip','Delete a Trip'])
        if choice == 'Create a Trip':
            create_trip()
        elif choice == 'View Trips':
            read_trips()
        elif choice == 'Update a Trip':
            update_trip()
        elif choice == 'Delete a Trip':
            create_car()
    # if choice == 'Login':
    #     login_section()
    

# def login_section():
#     conn = get_db_connection()
#     cursor = conn.cursor()

#     d_email = st.text_input('Email')
#     d_password = st.text_input('Password', type='password')

#     if st.button('Login'):
#         query = "SELECT * FROM drivers WHERE driver_email = %s AND driver_password = %s"
#         cursor.execute(query, (d_email, d_password))
#         result = cursor.fetchone()

#         if result:
#             st.session_state.logged_in = True
#             st.session_state.driver_data = result
#             driver_id, driver_name, driver_license, driver_email, driver_password, car_id, trip_id = result
#             st.success(f'Login successful! Welcome, {driver_name} ({driver_email})')
#             next()
#         else:
#             st.error('Invalid email or password')

#     cursor.close()
#     conn.close()

def create_driver():
    conn = get_db_connection()
    cursor = conn.cursor()

    d_name = st.text_input('Name')
    d_license = st.text_input('Driving License')
    d_email = st.text_input('Email')
    d_password = st.text_input('Password', type='password')

    if st.button('Create Account'):
        insert_query = "INSERT INTO drivers (driver_name, driver_license, driver_email, driver_password) VALUES (%s, %s, %s, %s)"
        insert_values = (d_name, d_license, d_email, d_password)

        cursor.execute(insert_query, insert_values)
        conn.commit()
        st.success('Driver created successfully!')

    cursor.close()
    conn.close()

def read_drivers():
    conn = get_db_connection()
    cursor = conn.cursor()
    query="select * from drivers"
    cursor.execute(query)
    view = cursor.fetchall()
    conn.commit()
    st.title("Drivers")
    st.table(pd.DataFrame(view, columns=["driver_id", "driver_name", "driver_licnese","driver_email","driver_password", "car_id", "trip_id"]))    
    cursor.close()
    conn.close()

def update_driver():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Prompt for driver ID
    driver_id = st.text_input('Driver ID:')

    # Select column to update
    update = st.selectbox('Update What', ['driver_name', 'driver_license', 'driver_email', 'driver_password', 'car_id', 'trip_id'])

    # Construct update query based on selected column
    if update == 'driver_name':
        new_name = st.text_input('New Name')
        query = f"UPDATE drivers SET driver_name = '{new_name}' WHERE driver_id = {driver_id}"
    elif update == 'driver_license':
        new_license = st.text_input('New License')
        query = f"UPDATE drivers SET driver_license = '{new_license}' WHERE driver_id = {driver_id}"
    elif update == 'driver_email':
        new_email = st.text_input('New Email')
        query = f"UPDATE drivers SET driver_email = '{new_email}' WHERE driver_id = {driver_id}"
    elif update == 'driver_password':
        new_password = st.text_input('New Password')
        query = f"UPDATE drivers SET driver_password = '{new_password}' WHERE driver_id = {driver_id}"
    elif update == 'car_id':
        new_car_id = st.text_input('New Car ID')
        query = f"UPDATE drivers SET car_id = {new_car_id} WHERE driver_id = {driver_id}"
    elif update == 'trip_id':
        new_trip_id = st.text_input('New Trip ID')
        query = f"UPDATE drivers SET trip_id = {new_trip_id} WHERE driver_id = {driver_id}"

    # Execute update query
    if st.button('Update'):
        cursor.execute(query)
        conn.commit()
        st.success('Driver information updated successfully.')
    conn.close()

def delete_driver():
    conn = get_db_connection()
    cursor = conn.cursor()
    driver_id = st.text_input('Driver ID:')
    d=f"delete from drivers where driver_id={driver_id}"
    if st.button('Delete'):
        cursor.execute(d)
        conn.commit()
        st.success('Driver information deleted successfully.')
    cursor.close()
    conn.close()



def create_car():
    conn = get_db_connection()
    cursor = conn.cursor()
    car_name = st.text_input('Car Name')
    car_documents = st.text_input('Car Documents')
    car_type = st.text_input('Car Type')
    car_colour = st.text_input('Car Colour')
    if st.button('Create Car'):
        query="INSERT INTO cars (Car_name, Car_documents, Car_type, Car_colour) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (car_name, car_documents ,car_type, car_colour))
        conn.commit()
        st.success('Car created successfully!')

    cursor.close()
    conn.close()

def read_cars():
    conn = get_db_connection()
    cursor = conn.cursor()
    query="select * from cars"
    cursor.execute(query)
    view = cursor.fetchall()
    conn.commit()
    st.title("Cars")
    st.table(pd.DataFrame(view, columns=["car_id", "car_name","car_documents", "car_type", "car_colour"]))    
    cursor.close()
    conn.close()

def update_car():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Prompt for driver ID
    car_id = st.text_input('Car ID:')

    # Select column to update
    update = st.selectbox('Update What', ["car_name","car_documents", "car_type", "car_colour"])

    # Construct update query based on selected column
    if update == 'car_name':
        new_name = st.text_input('New Name')
        query = f"UPDATE cars SET car_name = '{new_name}' WHERE car_id = {car_id}"
    elif update == 'car_documents':
        new_document = st.text_input('New Documents')
        query = f"UPDATE cars SET car_documents = '{new_document}' WHERE car_id = {car_id}"
    elif update == 'car_type':
        new_type = st.text_input('New Car Type')
        query = f"UPDATE cars SET car_type = '{new_type}' WHERE car_id = {car_id}"
    elif update == 'car_colour':
        new_colour = st.text_input('New Colour')
        query = f"UPDATE cars SET car_colour = '{new_colour}' WHERE car_id = {car_id}"
    # Execute update query
    if st.button('Update'):
        cursor.execute(query)
        conn.commit()
        st.success('Car information updated successfully.')
    conn.close()

def delete_car():
    conn = get_db_connection()
    cursor = conn.cursor()
    car_id = st.text_input('Car ID:')
    d=f"delete from cars where car_id={car_id}"
    if st.button('Delete'):
        cursor.execute(d)
        conn.commit()
        st.success('Car information deleted successfully.')
    cursor.close()
    conn.close()

def create_trip():
    conn = get_db_connection()
    cursor = conn.cursor()

    st.subheader("Create a Trip")
    trip_name = st.text_input('Trip Name')
    trip_source = st.text_input('Source')
    trip_destination = st.text_input('Destination')
    trip_schedule = st.text_input('Schedule')
    trip_capacity = st.text_input('Seating Capacity')
    trip_car = st.text_input('Car id')
    if st.button('Create Trip'):
        q = ("INSERT INTO trips (trip_name, source, destination, schedule, seating_capacity, car_id) VALUES (%s, %s, %s, %s, %s, %s)")
        a = (trip_name, trip_source, trip_destination, trip_schedule, trip_capacity, trip_car)
        cursor.execute(q, a)
        conn.commit()
        st.success('Trip created successfully!')

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

def update_trip():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Prompt for driver ID
    trip_id = st.text_input('Trip ID:')

    # Select column to update
    update = st.selectbox('Update What', ['trip_name', 'source', 'destination', 'trip_status', 'schedule', 'seating_capacity', 'car_id'])

    # Construct update query based on selected column
    if update == 'trip_name':
        new_name = st.text_input('New Name')
        query = f"UPDATE trips SET trip_name = '{new_name}' WHERE trip_id = {trip_id}"

    elif update == 'source':
        new_source = st.text_input('New source')
        query = f"UPDATE trips SET source = '{new_source}' WHERE trip_id = {trip_id}"

    elif update == 'destination':
        new_destination = st.text_input('New destination')
        query = f"UPDATE trips SET destination = '{new_destination}' WHERE trip_id = {trip_id}"

    elif update == 'trip_status':
        new_trip_status= st.text_input('New trip_status')
        query = f"UPDATE trips SET trip_status = '{new_trip_status}' WHERE trip_id = {trip_id}"

    elif update == 'schedule':
        new_schedule= st.text_input('New schedule')
        query = f"UPDATE trips SET schedule = '{new_schedule}' WHERE trip_id = {trip_id}"

    elif update == 'seating_capacity':
        new_seating_capacity= st.text_input('New seating_capacity')
        query = f"UPDATE trips SET seating_capacity = '{new_seating_capacity}' WHERE trip_id = {trip_id}"

    elif update == 'car_id':
        new_car_id= st.text_input('New car_id')
        query = f"UPDATE trips SET car_id = '{new_car_id}' WHERE trip_id = {trip_id}"

    # Execute update query
    if st.button('Update'):
        cursor.execute(query)
        conn.commit()
        st.success('Trip information updated successfully.')
    conn.close()

# Run the app
app()
