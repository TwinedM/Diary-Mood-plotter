import glob
from turtle import pos
from nltk.sentiment import SentimentIntensityAnalyzer

files = glob.glob("./diary/*.txt")
print(files)
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

print(negative_list,positive_list) 