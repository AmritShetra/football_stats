## Football Stats

An experiment in using Machine Learning to make predictions on a 2017-18 English Premier League dataset based on Fantasy Premier League statistics.

### Metadata
```
name
club
age
position: Position on the pitch
position_cat: 1 for attackers, 2 for midfielders, 3 for defenders, 4 for goalkeepers
market_value: Transfer value from transfermrkt.com as of July 20th, 2017
page_views: Average daily Wikipedia page views from September 1, 2016 to May 1, 2017
fpl_value: Value in FPL as of July 20th, 2017
fpl_sel: % of FPL players who have selected player in their team
fpl_points: FPL points accumulated over the previous season
region: 1 for England, 2 for EU, 3 for Americas, 4 for Rest of World
nationality
new_foreign: Is the player a new signing from a different league in 2017/18 (until July 20th, 2017)
age_cat
club_id
big_club: Whether the player belongs to one of the 'Big 6' clubs
new_signing: Is the player a new signing for 2017/18 (until July 20th, 2017)
```

### Installation
* Make sure you have Python 3 installed before you create a virtual environment and install the required libraries.
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
* Run `jupyter notebook`.
* You can then access the notebook at `localhost:8888` as shown in the terminal window.

### Acknowledgements
Dataset is [taken from Kaggle](https://www.kaggle.com/mauryashubham/english-premier-league-players-dataset).
