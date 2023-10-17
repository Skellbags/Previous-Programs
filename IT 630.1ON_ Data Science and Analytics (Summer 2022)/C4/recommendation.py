#
#  recommendation.py
#

from math import sqrt

"""manhattan is not used but provided here just for completeness"""
def manhattan(self, rating1, rating2):
    """Computes the Manhattan distance.
    Both rating1 and rating2 are dictionaries
    for two users/entities"""
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1 #Indiates no ratings in common
        

def minkowski(r, rating1, rating2):
    """Computes the Minkowski distance.
    r is 1 for manhattan distance and 2 for euclidean
    Both rating1 and rating2 are dictionaries
    for two users/entities
    """
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance +=pow(abs(float(rating1[key]) - float(rating2[key])), r)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1/r)
    else:
        return 0 #Indicates no ratings in common

def computeNearestNeighbor(r, username, users):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            distance = minkowski(r, users[user], users[username])
            distances.append((round(distance,3), user))
    # sort based on distance -- closest first
    distances.sort()
    return distances

def recommend(r, username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(r, username, users)[0][1]

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    #print(neighborRatings)
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

