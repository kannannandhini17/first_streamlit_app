import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('🥣 My parents new healthy diner')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("Please select the fruit for information.")
   else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
      
except URLError as e:
  streamlit.error()

##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
##streamlit.text(fruityvice_response)


##streamlit.header('Fruityvice Fruit Juice')

##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


##fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
##streamlit.dataframe(fruityvice_normalized)

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


streamlit.text("the fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()
        
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


##my_cur.execute("SELECT * FROM fruit_load_list")
##my_data_rows = my_cur.fetchall()
##streamlit.header("The fruit load list contains:")
##streamlit.dataframe(my_data_rows)
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('jackfruit + Papaya + guawa + kiwi')")
        return "thanks for adding" + new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
if streamlit.button('Add a fruit into a list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

#streamlit.write('Thanks for adding ', add_my_fruit)
##my_cur.execute("insert into fruit_load_list values ('from streamlit')")

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

      
streamlit.write('The user entered ', fruit_choice)
