import streamlit 


streamlit.title("My Parents New Healthy Diner")

streamlit.subheader('Breakfast menu')

streamlit.write('Omega 3 & Blueberry Oatemal') 

streamlit.write('Kale, Spinach & Rocket Smoothie') 

streamlit.write('Hard-Boiled Free-Range Egg')

import pandas 
import streamlit 


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header('Build Your Own Fruit Smoothie')

 
# Lets put a pick list here so tehy can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on the page
streamlit.dataframe(my_fruit_list)


streamlit.header("Fruityvice Fruit Advice!")


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output the screen as table
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)
