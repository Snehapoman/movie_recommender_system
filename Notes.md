# ***Movie Recommender System Project***

# 

##### Types Of recommender system

##### &nbsp;

* content based (tags)
* collaboration filtering (recommend on bases of user similarity 
* hybrid (contain of both) 





##### Project flow



data

1\. data preprocessing

2\. model

3\. website

4\. deploy



columns to keep in final dataset

genres

id

keywords

title

overview

cast crew



###### Text vectorization 



convert text into vector, so to recommend the movie on closed vector 

for which, will use **bags of words** 

during ,vectorization will not consider the stop words ,and perform vectorization on other words 





Every movie is the vector, so we need to calculate distance of each movie from other 

if distance is large then similarity is less , we will calculate cosine angle (if angle is 0 then it is some angle if it is larger then it's high dissimilarity) because as we work with high dim data Euclidean distance is not a reliable measure -- for that there is function cosine similarity makes thing easy 





###### Main function



we will sorted the similarity part in which we will sort the distance one of the movie with other in which we will sort the distance so that we will get the top similar movies in starting of the search .......so will fetch top 5 movies and then we will show them



we need to kept the index still so we will call enumerate function for it 



