# Hotel_Recommendation_Sysytem_with_Machin_Learning
We all plan trips and the first thing to do when planning a trip is finding a hotel. There are so many websites recommending the best hotel for our trip.  I’m going to build a hotel recommendation system with Machine Learning with Python.

A hotel recommendation system aims to predict which hotel a user is most likely to choose from among all hotels. So to build this type of System which will help the user to book the best. We can do this using cistomer reviews.

For example, suuppose you want to go on a business trip, so the hotel recommendation system should show you the hotel that other cistomers have rated best for business travel. It is therefore also our approach to build a recommendation system based on customer reviews and ratings

##Dataset
Here I am using dataset avaliable on Kaggle.
DATASET (https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe/download?datasetVersionNumber=1)

##Import necessary Python libraries
import nltk
nltk.download('wordnet')
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from ast import literal_eval

##This dataset contain hotel data from 6 countries, namely:
1. Netherlnads
2. United kingdom
3. France
4. Spain
5. Italy
6. Austria


So for simpicity, I will change the name from "United Kingdom" to "UK".
![image](https://user-images.githubusercontent.com/122660441/236448663-81af4326-edfe-46aa-92c7-633ff21b12b6.png)
![image](https://user-images.githubusercontent.com/122660441/236448681-c356e4dc-2b3a-4442-85c2-c7685c3270cb.png)





















