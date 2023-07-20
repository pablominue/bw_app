import pandas as pd
import requests
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import logging

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import requests
import json

class BWApi:
    """
    API To connect to your Biwenger League
    """
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        self.base_url = 'https://biwenger.as.com/api/v2'
        self.token = None
        self.ids = json.loads(
            open(
                './bw/Biwenger/biwenger.json' 
                ).read()
        )

    def refresh_token(self) -> None:
        data = {"email": self.email,
                "password": self.password}
        url = self.base_url + '/auth/login'
        response = requests.post(
            url,
            data=data
        )
        self.token = json.loads(response.text).get('token')
        self.headers = {'Authorization': 'Bearer ' + self.token}
        self.headers.update(self.ids)
    
    def try_with_token(fun):
        def inner(self, *args, **kwargs):
            try:
                fun(self, *args, **kwargs)
            except:
                self.refresh_token()
                fun(self, *args, **kwargs)
        return inner

    @try_with_token
    def __post(self, endpoint, params = None):
        response = requests.get(
            self.base_url + endpoint, params=params, headers=self.headers
        ).json()
        return response
    
    @try_with_token
    def get(self, endpoint, params = None):
        response = requests.get(
            self.base_url + endpoint, params=params, headers=self.headers
        ).json()
        return response
    def get_team(self):
        team = self.get(endpoint="/user?fields=*,lineup(type,playersID),players(*,fitness,team,owner),market(*,-userID),offers,-trophies",
                        params=self.ids)
        return team.get('data').get('lineup')

    def get_market(self):
        self.headers.update(self.ids)
        mrkt = self.get(endpoint = "/competitions/la-liga/market?interval=day&includeValues=true&x-leaguehead", params = self.ids)
        return mrkt


class Data:

    def __init__(self):
        logging.debug('Retrieving data from Biwenger...')
        r = requests.get(
            "https://cf.biwenger.com/api/v2/competitions/la-liga/data?lang=en&score=1").json()

        self.raw_data = []
        self.teams = {'Almería', 'Athletic', 'Atlético', 'Barcelona', 'Betis', 'Cádiz', 'Celta', 'Elche', 'Espanyol',
                      'Getafe', 'Girona', 'Mallorca', 'Osasuna', 'Rayo', 'Real Madrid', 'Real Sociedad', 'Sevilla',
                      'Valencia', 'Valladolid', 'Villarreal'}

        self.teams = pd.read_csv('bw/Biwenger/teams.csv')

        for k, v in r['data']['players'].items():
            self.raw_data.append(v)

        self.data = pd.DataFrame(self.raw_data)
        logging.debug('Data Loaded')
        logging.debug('Creating Model...')
        X = self.data.loc[:, ['points']].values

        y = self.data.loc[:, 'price'].values

        poly = PolynomialFeatures(degree=2,
                                  include_bias=False)
        X_poly = poly.fit_transform(X.reshape(-1, 1))
        model2 = LinearRegression()
        model2.fit(X_poly, y)

        var = model2.predict(X_poly) - y
        maximum = max(var)
        minimum = min(var)

        self.data = self.data.assign(profitability=2 * ((var - minimum) / (maximum - minimum)) - 1)
        logging.debug('Data Ready for use')
        # best_profitability = self.data.sort_values(by = 'profitability',ascending = False)
        # count = 1
        # for i in best_profitability.head(10)['name'].values:
        #    print("{}: {}".format(count,i))
        #    count += 1


class Player:

    def __init__(self, data: Data, name: str):
        positions = ['goalkeeper',
                     'defender',
                     'midfielder',
                     'striker']
        name = name.lower()
        data.data['name'] = data.data['name'].apply(
            lambda x: str(x).lower()
        )
        self.player_data = data.data.loc[data.data['name'] == name]
        if len(self.player_data) == 0:
            raise Exception("Player not Found")
        self.value = int(self.player_data['price'])
        self.value_var = int(self.player_data['priceIncrement'])
        self.position = positions[int(self.player_data['position'])]
        self.profitability = float(self.player_data['profitability'])
        

class Team:
    def __init__(self):
        self.players = []


class Pack:
    def __init__(self, type_: str, data: pd.DataFrame):
        self.data = data
        self.type = type_.lower()
        if self.type not in ['gold', 'silver', 'bronze']:
            raise Exception(f"Input 'type' must be one of these: 'gold', 'silver', 'bronze'. Provided was {type_}")

        if self.type == 'gold':
            self.range = [10000000, 30000000]
            self.price = 15000000

        if self.type == 'silver':
            self.range = [5000000, 10000000]
            self.price = 8000000

        if self.type == 'bronze':
            self.range = [0, 5000000]
            self.price = 1000000

    def profit_chance(self):
        total = len(
            self.data.loc[(self.data['price'] >= self.range[0]) & (self.data['price'] <= self.range[1])])
        above = len(
            self.data.loc[(self.data['price'] >= self.price) & (self.data['price'] <= self.range[1])])

        profit = str((above / total) * 100)[:5] + " %"

        return profit
