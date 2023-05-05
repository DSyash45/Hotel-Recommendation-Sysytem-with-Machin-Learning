

#Hotel_Recommendation_System_with_Machine_Learning

#Libraries

import nltk
nltk.download('wordnet')
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from ast import literal_eval

#Import Data
data = pd.read_csv(r"E:\MY TAB\Data Science\iNeuron Project\Hotel_Reviews.csv")
data.head()
data.columns

#Replacing "United Kingdom" with "UK"
data['Hotel_Address'] = data['Hotel_Address'].str.replace("United Kingdom","UK")

#Now split the adress and pick the last word in the address to identify the country 
data["countries"] = data.Hotel_Address.apply(lambda x : x.split(' ')[-1])
print(data.countries.unique())

#Now drop the unnecessary columns that we don’t need for the task of
# creating a hotel recommendation system

data.drop(['Additional_Number_of_Scoring',
           'Review_Date','Reviewer_Nationality',
           'Negative_Review','Review_Total_Negative_Word_Counts',
           'Total_Number_of_Reviews','Positive_Review',
           'Review_Total_Positive_Word_Counts','Total_Number_of_Reviews_Reviewer_Has_Given',
           'Reviewer_Score','days_since_review','lat','lng'],axis=1,inplace=True)

data.columns
data.head()

#Now will create a function to convert the strings of list
# into a normal list and then apply it to the “Tags” column
# in the dataset:
    
def impute(column):
    column = column[0]
    if (type(column) != list):
        return "".join(literal_eval(column))
    else:
        return column
    
data["Tags"] = data[["Tags"]].apply(impute, axis = 1)

data.head()

#lowercase "Tags" & "countries"

data['countries'] = data['countries'].str.lower()
data['Tags'] = data['Tags'].str.lower()

#Hotel_Recommendation_Function

def recommend_hotel(location,description):
    description = description.lower()
    word_tokenize(description)
    stop_words = stopwords.words('english')
    lemm = WordNetLemmatizer()
    filtered = {word for word in description if not word in stop_words}
    filtered_set = set()
    for fs in filtered:
        filtered_set.add(lemm.lemmatize(fs))
    
    country = data[data['countries']==location.lower()]
    country = country.set_index(np.arange(country.shape[0]))
    list = []; list2 = []; cos = []
    
    for i in range(country.shape[0]):
        temp_token = word_tokenize(country['Tags'][i])
        temp_set = [word for word in temp_token if not word in stop_words]
        temp2_set = set()
        for s in temp_set:
            temp2_set.add(lemm.lemmatize(s))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    country['similarity'] = cos
    country = country.sort_values(by='similarity', ascending = False)
    country.drop_duplicates(subset='Hotel_Name', keep='first',inplace= True)
    country.reset_index(inplace=True)
    return country[["Hotel_Name","Average_Score","Hotel_Address"]].head()


#Call function

recommend_hotel('Italy', 'I am going for a business trip')
recommend_hotel('UK', 'I am going for holiday trip')
















