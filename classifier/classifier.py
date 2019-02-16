from textblob.classifiers import NaiveBayesClassifier
import random

data = []

risk_sentences = open("risk_sentences.txt").read().split("\n")
non_risk = open("non_risk.txt").read().split("\n")

for i in risk_sentences:
    data.append((i,"risk"))

for i in non_risk:
    data.append((i,"non"))

random.shuffle(data) 
train_percentage = 0.75
train = data[:round(train_percentage*len(data))]
test = data[len(train):]

cl = NaiveBayesClassifier(train)
print(c1.accuracy(test))


