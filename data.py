movie_ratings_dashboard = {'name': 'Movie Ratings Dashboard','skills': ['Python / Flask / Pandas','HTML / CSS / Bootstrap','Data Parsing (local JSON)','Javascript','Plotly.js','DOM Manipulation (D3.js)','Machine Learning (sklearn, Logistic Regression, train-test-split)'],'github': 'https://github.com/blancacarretero/movie-recommendation-engine','app_link': 'https://movie-ratings-dashboard.herokuapp.com/','description': f"This dashboard was created as a way to explore the <a href=\"https://grouplens.org/datasets/movielens/\" target=\"_blank\">MovieLens</a> movie ratings dataset. This was a group project where we set out to glean insights about users' movie preferences. I was responsible for coding the backend of the Flask app and deploying the finalized app to Heroku.",'image': 'static/projects/thumbnails/movieRatingsDB2.png'
}

python_api = {
    'name': 'Python API Weather Analysis',
    'skills': [
        'Python / Pandas',
        'Data Retrieval (API)',
        'Matplotlib.pyplot',
        'HTML / CSS / Bootstrap'
    ],
    'github': 'https://github.com/tylerhill122/python-api-challenge',
    'app_link': 'https://tylerhill122.github.io/Web-Design-Challenge/',
    'description': 'The purpose of this project is to display our ability to use APIs to gather and plot data using Python/Pandas. We were tasked with randomly generating >500 coordinates with their corresponding latitudes and longitudes, then to grab the nearest city to these coordinates, accounting for and removing any duplicates. From there we placed those city names into OpenWeatherMap\'s "Current Weather Data" API to grab the following pertinent information: latitude and longitude, temperature, humiditiy, cloudiness, and wind speed. From this information a Pandas DataFrame was created and exported as an external .csv file. We were tasked with creating four plots for the initial data: Temperature vs. Latitude Humidity vs. Latitude Cloudiness vs. Latitude Wind speed vs Latitude Regression lines and values were also calculated, plotting the regression line.',
    'image': 'static/projects/thumbnails/APIWeather.png'
}

bellybutton = {
    'name': 'Bellybutton Biodiversity Dashboard',
    'skills': [
        'HTML / CSS / Bootstrap',
        'Data Parsing (local JSON)',
        'Javascript',
        'Plotly.js',
        'DOM Manipulation (D3.js)'
    ],
    'github': 'https://github.com/tylerhill122/bb-biodiversity',
    'app_link': 'https://tylerhill122.github.io/bb-biodiversity/',
    'description': f'<p>In this assignment, we will build an interactive dashboard to explore the <a href=\"http://robdunnlab.com/projects/belly-button-biodiversity/\" target=\"_blank\">Belly Button Biodiversity dataset</a>, which catalogs the microbes that colonize human navels.</p><p>The dataset reveals that a small handful of microbial species (also called operational taxonomic units, or OTUs, in the study) were present in more than 70% of people, while the rest were relatively rare.</p>Methods:<ol><li>Use D3.js library to read in samples.json file</li><li>Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in each individual.</li><li>Create a bubble chart to display each OTU and their representation.</li><li>Display the sample metadata, i.e., an individual\'s demographic information.</li><li>Display each key-value pair from the metadata JSON object somewhere on the page.</li><li>Update all the plots when a new sample is selected.</li><li>Deploy your app to a free static page hosting service, such as GitHub Pages.</li></ol><p><img src="static/images/bb-demo.png"></p><p><img src="static/images/bb-hbar.png"></p>',
    'image': 'static/projects/thumbnails/bbBiodiversity.png'
}

projects = {
    'movie_ratings_dashboard': movie_ratings_dashboard,
    'python_api': python_api,
    'bellybutton': bellybutton,
}

def get(project):
    return projects[project]