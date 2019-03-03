from collections import Counter
from linear_algebra import distance
from statistics import mean
import math, random
import matplotlib.pyplot as plt
from data import cities


def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest


def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""

 
    by_distance = sorted(labeled_points,
                         key=lambda point_label: distance(point_label[0], new_point))
    

    
    k_nearest_labels = [label for _, label in by_distance[:k]]

   
    return majority_vote(k_nearest_labels)



def predict_preferred_language_by_city(k_values, cities):
    for j in k_values:
        num_correct=0
        for i in cities:
            #print(i[0],i[1])
            val = knn_classify(j,cities,i[0])
            #print(val)
            if(val==i[1]):
                num_correct+=1
        print(j, "neighbor[s]:", num_correct, "correct out of", len(cities))
    
def skl(k_values,cities):
    for j in k_values:
        X_array=[]
        Y_array=[]
        num_correct=0
        for i in cities:
            X_array.append(i[0])
            Y_array.append(i[1])
        from sklearn.neighbors import KNeighborsClassifier
        neigh = KNeighborsClassifier(n_neighbors=j)
        neigh.fit(X_array, Y_array)
        for i in cities:
            if(neigh.predict([i[0]])==i[1]):
                num_correct+=1
        print(j, "neighbor[s]:", num_correct, "correct out of", len(cities))
if __name__ == "__main__":
    k_values = [1, 3, 5, 7]
    print("K Neigbour analysis using Our KNN Classification")
    predict_preferred_language_by_city(k_values, cities)
    print("K Neigbour analysis using SKlearn KNN Classification")
    skl(k_values,cities)
