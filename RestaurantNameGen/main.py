import streamlit as st
import langchain_helper 

st.title("Restaurant Name Generator")
# st.write("Generate unique names for your restaurant!")

cusinine = st.sidebar.selectbox(
    "Select a cuisine type",("Italian", "Chinese", "Mexican", "Indian", "American")
    )

if cusinine:
    response = langchain_helper.gen_restaurant_name_and_items(cusinine)

    st.header(response['restaurant_name'].strip())

    menu_items = response['menu_items'].strip().split(",")

    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-",item)
