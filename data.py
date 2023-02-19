movie_ratings_dashboard = {
    'name': 'Movie Ratings Dashboard',
    'skills': [
        'Python / Flask / Pandas',
        'HTML / CSS / Bootstrap',
        'Data Parsing (local JSON)',
        'Javascript',
        'Plotly.js',
        'DOM Manipulation (D3.js)',
        'Machine Learning (sklearn, Logistic Regression, train-test-split)'
    ],
    'github': 'https://github.com/blancacarretero/movie-recommendation-engine',
    'app_link': 'https://movie-ratings-dashboard.herokuapp.com/',
    'description': f"This dashboard was created as a way to explore the <a href=\"https://grouplens.org/datasets/movielens/\" target=\"_blank\">MovieLens</a> movie ratings dataset. This was a group project where we set out to glean insights about users' movie preferences. I was responsible for coding the backend of the Flask app and deploying the finalized app to Heroku.",
}

projects = {
    'movie_ratings_dashboard': movie_ratings_dashboard
}

def get(project):
    return projects[project]