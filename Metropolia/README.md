# Metropolia AI Project

A small coding assignment for applying to work in Metropolia's AI project.

I'm creating a Flask API and a simple React website that allows you to translate from English to Finnish with a local translating LLM.

For diary entries regarding this project, look at the entries from 11.9.2023 and 12.9.2023 at the root of the repository.

## Setup

### Backend

I'm using Python 3.9 to develop this project.

Install dependencies in the backend folder with:

`pip install flask flask-cors torch transformers sentencepiece sacremoses`

Run server.py to launch the app:

`python server.py`

### Frontend

To develop the frontend further, go to the frontend folder and install dependencies with:

`npm install`

Run the app with:

`npm run dev`
