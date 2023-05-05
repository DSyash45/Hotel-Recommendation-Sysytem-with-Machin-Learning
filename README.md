# Hotel_Recommendation_System_with_Machin_Learning
We all plan trips and the first thing to do when planning a trip is finding a hotel. There are so many websites recommending the best hotel for our trip.  I’m going to build a hotel recommendation system with Machine Learning with Python.

A hotel recommendation system aims to predict which hotel a user is most likely to choose from among all hotels. So to build this type of System which will help the user to book the best. We can do this using cistomer reviews.

For example, suuppose you want to go on a business trip, so the hotel recommendation system should show you the hotel that other cistomers have rated best for business travel. It is therefore also our approach to build a recommendation system based on customer reviews and ratings

## Dataset
Here I am using dataset avaliable on Kaggle.
DATASET (https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe/download?datasetVersionNumber=1)

## Import necessary Python libraries
![image](https://user-images.githubusercontent.com/122660441/236449791-85a375ad-ca80-4286-b4fc-a339d7c72576.png)
![image](https://user-images.githubusercontent.com/122660441/236449646-67d68da4-bded-451a-8cc6-ec59b075a936.png)


## This dataset contain hotel data from 6 countries, namely:
1. Netherlnads
2. United kingdom
3. France
4. Spain
5. Italy
6. Austria


So for simpicity, I will change the name from "United Kingdom" to "UK".
I can also see that there is no column as “Country” to specify the destination of the hotel but in the “Hotel_Address” column the last word mentioned is the name of the country. So I will extract the names of the countries from that column and store the name in a new column:
![image](https://user-images.githubusercontent.com/122660441/236450125-1c07f8fe-51d3-4703-aa96-617431e58c8e.png)


Also I will drop the unnecessary columns that we don't need fro further analysis.

![image](https://user-images.githubusercontent.com/122660441/236450686-39dafd60-19b9-40b0-a096-d0465fed4f88.png)

### Now I will create a function to convert the strings of list into a normal list and then apply it to the “Tags” column in the dataset:

![image](https://user-images.githubusercontent.com/122660441/236451075-3946b91d-e4c1-4cbd-af81-703d88ab43d3.png)
                                     
![image](https://user-images.githubusercontent.com/122660441/236453348-05057b76-0849-4056-87db-5b0f0ea6e3a1.png)



## Let's define a function to recommend the names of hotels according to the location and description provided by the user.
### I am using Natural Language Processing 
Here aim is not just to recommend the name but also rank it according to the user ratings.

![image](https://user-images.githubusercontent.com/122660441/236451776-2bc29d39-3fde-4f77-8031-19732d3d979d.png)

## Let's See How It Works
call fuction and provide "country" name listed above and describe the perpose of trip.

##recommend_hotel('Italy', 'I am going for a business trip')
                  
![image](https://user-images.githubusercontent.com/122660441/236453441-f96a6fea-b417-437f-8058-36ada1cac4f4.png)

Here we get  top 5 hotels name and address.

