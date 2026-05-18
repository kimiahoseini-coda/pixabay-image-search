
import streamlit as st
import requests

API_KEY = "55920427-af66f2667d2f66f49f1f51031"

st.title("Pixabay Image Search")

search = st.text_input("Search Images")

category = st.selectbox(
    "Category",
    [
        "backgrounds",
        "fashion",
        "nature",
        "science",
        "education",
        "people",
        "animals",
        "travel"
    ]
)

colors = st.selectbox(
    "Color",
    [
        "all",
        "grayscale",
        "transparent",
        "red",
        "orange",
        "yellow",
        "green",
        "turquoise",
        "blue",
        "lilac",
        "pink",
        "white",
        "gray",
        "black",
        "brown"
    ]
)

safe_search = st.checkbox("Safe Search", value=True)

if st.button("Search"):

    url = f"https://pixabay.com/api/?key={API_KEY}&q={search}&category={category}&colors={colors}&safesearch={safe_search}"

    response = requests.get(url)

    data = response.json()

    for image in data["hits"]:

        st.image(
            image["webformatURL"],
            width=300
        )




























































