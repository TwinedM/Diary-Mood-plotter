import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import matplotlib.pyplot as plt
import re
import pandas as pd
# fininsh this with matplotlib itself

files = glob.glob("./diary/*.txt")
analyser = SentimentIntensityAnalyzer()
scores = []


for obj in files:
    with open(obj,"r",encoding = 'utf-8',errors='ignore') as file:
        data = file.read()
        score = analyser.polarity_scores(data)
        scores.append(score)


negative_list = []
positive_list = []
for days in scores:
    negative_list.append(days['neg'])
    positive_list.append(days['pos'])

dates = []
for file in files:
    for date in files:
        match = re.findall(r"\d{4}-\d{2}-\d{2}", date)
        dates.append(match)

date_2 = dates[:6]
date_2 = str(date_2)
date_2 = pd.to_datetime(date_2)
DF = pd.DataFrame()
DF['value'] = date_2
DF = DF.set_index(negative_list)
plt.plot(DF)
plt.gcf().autofmt_xdate()
plt.show()

#webapp part 
#st.title("Diary Tone")
#st.header("Positivity",divider="gray")