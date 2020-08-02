import pandas as pd
from pytrends.request import TrendReq
import argparse

import numpy as np

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


parser = argparse.ArgumentParser(description='Argparser for data preprocessing')

parser.add_argument('--kw', default = [], type = list, metavar = 'KW', 
                    help = 'Lista das keywords a serem analisadas na trend')
parser.add_argument('--me', default = '3', type = str, metavar = 'M', 
                    help = 'Meses de análise das trends')

args = parser.parse_args()


pytrend = TrendReq(hl='BR', tz = 360)

results = pd.DataFrame()
scores = []

me = args.me

for k in args.kw:
  pytrend.build_payload(
      kw_list=[k],
      cat=0,
      timeframe=f'today {me}-m',
      geo='BR',
      gprop='')
  data = pytrend.interest_over_time().reset_index()
  scores.append(np.mean(moving_average(data[k].diff(1).fillna(0).values, n = 5)))

  results[k] = data[k]

ordered = pd.DataFrame({'produto': args.kw, 'score':scores})
ordered.to_csv("local_ordered.csv", index = False)