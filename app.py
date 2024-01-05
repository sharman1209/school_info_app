import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# MySQL Database Configuration
db_config = {
    'user': 'root',
    'password': 'TM_edu',
    'host': 'localhost',
    'database': 'list_of_schools',
    'port': '3306'
}

# Create a MySQL connection
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Query to fetch data from MySQL
query = 'SELECT * FROM your_table_name;'
df = pd.read_sql(query, con=engine)

# Streamlit app
st.title("School Information App")

# Create Autocomplete Widget
school_code_autocomplete = st.text_input("Enter school code")

# Autocomplete Suggestions
initial_suggestion = 'Select'
filtered_options = [initial_suggestion] + df['KOD SEKOLAH'].tolist()
selected_option = st.selectbox("Suggestions:", filtered_options)

# Create Search Button
search_button = st.button('Search')

# Create Clear Button
clear_button = st.button('Clear')

# Display Output Result
output_result = st.empty()

# Define Search Function
def search_school():
    school_code = school_code_autocomplete.upper()
    result = df[df['KOD SEKOLAH'] == school_code][['KOD SEKOLAH', 'SENARAI SEKOLAH MALAYSIA', 'SEKOLAH INTERIM', 'SEKOLAH VSAT', 'SEKOLAH HIBRID']]

    if result.empty:
        output_result.text(f"No information found for School Code: {school_code}")
    else:
        # Display the output as a list
        output_result.text(f"Information for School Code {school_code}: ")
        for _, row in result.iterrows():
            output_result.text(f"- School Code: {row['KOD SEKOLAH']}")
            output_result.text(f"  School Name: {row['SENARAI SEKOLAH MALAYSIA']}")
            output_result.text(f"  TM Interim: {row['SEKOLAH INTERIM']}")
            output_result.text(f"  VSAT: {row['SEKOLAH VSAT']}")
            output_result.text(f"  TM Hybrid: {row['SEKOLAH HIBRID']}")
            output_result.text("\n")

# Define Clear Function
def clear_results():
    output_result.empty()
    school_code_autocomplete = ''
    st.selectbox("Suggestions:", [initial_suggestion])

# Check if Search button is clicked
if search_button:
    search_school()

# Check if Clear button is clicked
if clear_button:
    clear_results()
