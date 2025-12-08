#kafka concepts
#zookeeper server
import pandas as pd

df = pd.read_csv("data/raw/StrmVid/Subscription Cohort Analysis Data Dictionary.csv")

if df.empty():
    print('none')
else:
    print(df.head(3))

def produce_message():
    print("kafka producer initiated")