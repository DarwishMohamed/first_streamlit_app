import streamlit as st


streamlit.title("My Parents New Healthy Diner")

streamlit.subheader('Breakfast menu')

streamlit.write('Omega 3 & Blueberry Oatemal') 

streamlit.write('Kale, Spinach & Rocket Smoothie') 

streamlit.write('Hard-Boiled Free-Range Egg')

import pandas as pd


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the table on the page
st.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index))

# If you want to do something with the selected fruits, you can use the `selected_fruits` variable.

