
# *****************************************************************************
# Importing Libraries
# *****************************************************************************
import os, json
import streamlit as st
import pandas as pd
from google.cloud import firestore
from google.oauth2 import service_account

# *****************************************************************************
# Defining Functions
# *****************************************************************************

# Function to load data when the streamlit app starts

@st.cache_data
def loading_data():
  names_ref = list(db.collection(u'movies').stream())
  names_dict = list(map(lambda x: x.to_dict(), names_ref))
  data = pd.DataFrame(names_dict)
  return data

# Function that display the filtered results on the main streamlit space 

def display_results(space, df, Title, flag=True, Message=''):
  if flag:
    space.subheader(Title)
    space.dataframe(df)
  else:
    space.subheader(Title)
    space.write(Message)
  
# *****************************************************************************
# Main
# *****************************************************************************

if __name__=="__main__":
    
  # Defining credentials to connecto the firestore db
  key_dict = json.loads(st.secrets["textkey"])
  creds = service_account.Credentials.from_service_account_info(key_dict)
  # Connecting to the firesore database
  db = firestore.Client(credentials=creds)
  dbNames = db.collection("movies")

  # Displaying the app main title
  st.title('Informacion Sobre Peliculas')
  # Cache loading of firestore data to reduce latency
  data = loading_data()

  # Creating a sidebar space within the streamlit app for a friendly interface
  sidebar = st.sidebar

  # Creating sidebar space to filter movies information from the loaded db
  sidebar.title("Obteniendo Informacion")
  sidebar.write("Parametros para filtrado de datos")
  # Defining variables to store the user filtering parameters for the search
  movie2look = sidebar.text_input("Movie: ")
  movie_search = sidebar.button("Movie Name Search")
  genre2look = sidebar.text_input("Genre: ")
  genre_search = sidebar.button("Genre Search")
  # Obtaining Movies Names informations from the loaded firestore db
  if movie_search:
    Title = f"Resulstados de la busqueda para: {movie2look}"
    if movie2look:
      filtered_df = data[data.name.str.lower().str.contains(movie2look.lower())]
      filtered_df.reset_index(drop=True, inplace=True) 
      search_result = filtered_df.shape[0] 
      display_results(st, filtered_df, f"Se encontraron {search_result} resultados")
    else:
      message = 'Please enter a movie name to look'
      display_results(st, ' ', Title, False, message)
  # Obtaining Movies Genres informations from the loaded firestore db
  if genre_search:
    Title = f"Result for searching movies containing: {genre2look}"
    if genre2look:
      filtered_df = data[data.genre.str.lower().str.contains(genre2look.lower())] 
      filtered_df.reset_index(drop=True, inplace=True) 
      search_result = filtered_df.shape[0] 
      display_results(st, filtered_df, f"Se encontraron {search_result} resultados")
    else:
      message = 'Please enter a genre to look'
      display_results(st, ' ', Title, False, message)

  # Creating sidebar space to add movies information to the loaded db
  sidebar.title("Adding New Movie")
  sidebar.write("Defining Movie")
  # Defining the movie information that will be added to the db
  name = sidebar.text_input("Name: ")
  genre = sidebar.text_input("Genre : ")
  director = sidebar.text_input("Director: ")
  company = sidebar.text_input("Company: ")
  submit = sidebar.button("Add New Movie")
  # Adding new movie to the firestore db
  if submit:
    if name and genre and director and company:
      doc_ref = db.collection("movies").document("name")
      doc_ref.set({
        "name": name,
        "genre": genre,
        "director": director,
        "company": company
      })
      new_row = pd.DataFrame({"name":name, "genre":genre,
                              "director":director,
                              "company":company}, index=[0])

      sidebar.write("New Movie added correctly!")
