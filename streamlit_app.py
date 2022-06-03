import streamlit
import pandas
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
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user picked', fruit_choice)
import requests
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+ fruit_choice)

#make json readable
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#make it a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit table contains:")
streamlit.text(my_data_row)
