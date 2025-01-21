# Web Applications for Data Science

This repository contains the solution for the *web applications for data science* section final project, for the *Sr Data Science* course developed by the *Tecnologico de Monterrey*, available in the *The Learning Gate* platform. The mentioned section allows students to learn about the use of the open-source *Streamlit* framework and the *Firestore* NoSQL document database for the development and deployment of web apps.

Thus, the final project is about the development and deployment of a web application using the Streamlit framework. This application connects to a Firestore database collection containing information about movies, such as their names, directors, genres and producing companies. Firestore is used due to its friendly use for the creation and consumption of NoSQL databases through mobile and web apps. Moreover, GitHub is used to store the developed code and to connect to Streamlit for its production deployment.

## Instructions

To complete the mentioned final project, the following requirements are fulfilled through the shared code in this repository:

- Analyze the *CSV* file containing the *movies.csv* file, composed of the movies information that will be stored in the Firestore database.
- Create a *Google Colab* notebook containing the implemented solution
- Migrate data contained in the movies.csv file to the Firestore database collection
- Create a streamlit.py code for the development of the streamtlit with the following functions:
    -  Start the app by loading, in the cache memory, the Firestore database collection containing the migrated movies information. This is to create a good experience for the users by reducing latency.
    - Allow the users to search for information about movies by filtering out the loaded movie collection.
    - Implement a functionality that allows users to add information about movies not contained in the loaded database.
- Create a GitHub repository containing the developed code and files
- Deploy the developed web app using the Streamlit framework cloud service by connecting the created GitHub repository to Streamlit through *https://share.streamlit.io*.

## Results

The created Streamlit web application can be consumed through the following link:
- *https://tlgappdeploymentgit-9vz3a7wocnv2pfzvtmdfxq.streamlit.app/*




