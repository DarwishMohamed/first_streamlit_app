import streamlit 
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents New Healthy Diner")
streamlit.subheader('Breakfast menu')
streamlit.write('Omega 3 & Blueberry Oatmeal') 
streamlit.write('Kale, Spinach & Rocket Smoothie') 
streamlit.write('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header('Build Your Own Fruit Smoothie')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('the user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)

second_fruit_choice = streamlit.text_input('Enter another fruit for more information:', 'Apple')
streamlit.write('The user also entered', second_fruit_choice)

# Commented to prevent repeat additions
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO fruit_load_list (FRUIT_NAME) VALUES (%s)", (new_fruit,))
        return "Thanks for adding " + new_fruit

# Commenting out to prevent multiple insertions
# fruits_to_add = ["jackfruit", "papaya", "guava", "kiwi"]
# for fruit in fruits_to_add:
#     insert_row_snowflake(fruit)

def remove_rows_snowflake(fruit_name):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("DELETE FROM fruit_load_list WHERE FRUIT_NAME = %s", (fruit_name,))

remove_rows_snowflake('test')
remove_rows_snowflake('from streamlit')

if streamlit.button('Get Fruit List'):
    my_cnv = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
