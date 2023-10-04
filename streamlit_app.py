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


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


