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

mars = {
    'name': 'Mars Web Scraping App',
    'skills': [
        'HTML / CSS / Bootstrap',
        'Python / Flask / Pandas',
        'Javascript',
        'API Requests',
        'Data Parsing (local JSON)',
        'Web Scraping using Splinter, BeautifulSoup'
    ],
    'github': 'https://github.com/tylerhill122/web-scraping-challenge',
    'app_link': 'https://daily-mars-scraper.herokuapp.com/',
    'description': '<p>This Python-Flask app was created to demonstrate web-scraping ability by creating a web-scraping Python script to scrape information from multiple Mars-related websites. The python script employs BeautifulSoup and Splinter to visit the websites and automatically collect and display relevant information, as well as collecting images to display within the app. The information is then placed into a MongoDB database which is accessed in order to display the results. The app can be modified to run daily, checking for latest news and placing the results into a database to track the results over time. The scraping functionality has been removed from the app due to lack of resources necessary for full functionality.</p><p>The follwing websites are used in the collecting of this information:</p><ul><li><a href="https://redplanetscience.com">redplanetscience.com</a></li><li><a href="https://spaceimages-mars.com">spaceimages-mars.com</a></li><li><a href="https://galaxyfacts-mars.com">galaxyfacts-mars.com</a></li><li><a href="https://marshemispheres.com">marshemispheres.com</a></li></ul>',
    'image': 'static/projects/thumbnails/mars.png'
}

leaflet = {
    'name': 'USGS Earthquake Data with Leaflet',
    'skills': [
        'HTML / CSS / Bootstrap',
        'Data Retrieval (USGS Earthquake API)',
        'Javascript',
        'Leaflet.js',
        'D3.js',
    ],
    'github': 'https://github.com/tylerhill122/leaflet-usgs',
    'app_link': 'https://tylerhill122.github.io/leaflet-usgs/',
    'description': '<p>The United States Geological Survey, or USGS for short, is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment, and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes.</p>',
    'image': 'static/projects/thumbnails/leaflet.png'
}

projects = {
    'movie_ratings_dashboard': movie_ratings_dashboard,
    'python_api': python_api,
    'bellybutton': bellybutton,
    'mars': mars,
    'leaftlet': leaflet
}

def get(project):
    return projects[project]