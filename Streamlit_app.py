import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.header('Breakfast Favorites')
streamlit.text('\N{bowl with spoon}Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{green salad}Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{chicken}Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
