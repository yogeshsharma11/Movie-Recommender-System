# Movie Recommender System

This is a simple **Movie Recommender System** built using **Streamlit**. It suggests movies based on a selected movie using similarity scores.

## Features
- Select a movie from the dropdown menu.
- Get top 5 similar movies as recommendations.
- Fetch movie posters using **The Movie Database (TMDb) API**.

## Requirements
Make sure you have **Python 3.7+** installed.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure
```
/streamlit-movie-recommender
│── movies.pkl          # Preprocessed movie dataset
│── similarity.pkl      # Precomputed similarity matrix
│── app.py              # Main Streamlit app script
│── README.md           # Project documentation
│── .gitignore          # Files to ignore in git
│── requirements.txt    # List of dependencies
```

## How to Run the Application

```bash
streamlit run app.py
```

This will start a local server, and the application will be accessible in your web browser.

## API Key Setup
The application fetches movie posters using TMDb API. Ensure you have a valid API key and replace it in `app.py`:

```python
url = "https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY"
```



