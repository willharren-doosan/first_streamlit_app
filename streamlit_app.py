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
import requests
fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/watermelon")

#make json readable
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#make it a table
streamlit.dataframe(fruityvice_normalized)
