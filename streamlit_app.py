import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#allow user to pick fruit
selected_fruit = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruit]
#dispaly the table
streamlit.dataframe(my_fruit_list)

# Lesson 9
streamlit.header('Fruityvice Fruit Advice!')
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a valid fruit to get more information!")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

streamlit.header("The fruit table contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
        return my_cur.fetchall()
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
#allow user to add fruit to list

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + new_fruit + "')")
        return 'Thanks for adding in '+ fruit_addition + "!"
    
fruit_addition = streamlit.text_input('What fruit should we add?')
if streamlit.button('Add a Fruit to our list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(fruit_addition)
    streamlit.text(back_from_function)
