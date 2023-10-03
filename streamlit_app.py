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
streamlit.dataframe(my_fruit_list) 


# lets puck a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)


# Lets put a pick list here so tehy can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

