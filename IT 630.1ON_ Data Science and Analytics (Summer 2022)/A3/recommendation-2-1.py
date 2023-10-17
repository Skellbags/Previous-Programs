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
        

def pearson(r, rating1, rating2):
    """Computes the Pearson's correlation coefficient.
    r is 1 for manhattan distance and 2 for euclidean
    Both rating1 and rating2 are dictionaries
    for two users/entities
    
    Note: I wasn't able to get the logic down 100% however,
    I belive I'm very close to the final result. Previously
    when I had done A3, this was my haulting point that I 
    couldn't debug past(Which also resulted in me not submitting
    the assignment).
    """
    commonRatings = False
    xS = sum(rating1.values()) / len(rating1)
    yS = sum(rating2.values()) / len(rating2)
    top=0
    botx=0
    boty=0
    bot=0
    for key in rating1:
        if key in rating2:
            top += ((rating1[key] - xS)*(rating2[key] - yS))
            botx += (rating1[key]-xS)**2.0
            boty += (rating2[key]-yS)**2.0
            commonRatings = True

    if commonRatings:
        bot= sqrt(botx) * sqrt(boty)
        return round((top/bot),2)
    else:
        return 0 #Indicates no ratings in common


def cosineCoeffecient(r, rating1, rating2):
    """Computes the Cosine coefficient.
    r is 1 for manhattan distance and 2 for euclidean
    Both rating1 and rating2 are dictionaries
    for two users/entities
    """
    #print("Simone:",rating1.values(), "\notheruser:",rating2.values())
    distance = 0
    commonRatings = False
    top=0
    botx=0
    boty=0
    for key in rating1:
        if key in rating2:
            top += rating1[key] * rating2[key]
            botx += pow(rating1[key], 2)
            boty += pow(rating2[key], 2)
            commonRatings = True
    bot = sqrt(botx) * sqrt(boty)
    distance = top/bot
    if commonRatings:
        return round(distance,3)
    else:
        return 0 #Indicates no ratings in common


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
            distance +=pow(abs(rating1[key] - rating2[key]), r)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1/r)
    else:
        return 0 #Indicates no ratings in common

def computeNearestNeighbor(r, username, users, pear=0, coeff=0):
    """creates a sorted list of users based on their distance to username"""
    if ((pear==0) and (coeff==0)):
        distances = []
        for user in users:
            if user != username:
                distance = minkowski(r, users[user], users[username])
                distances.append((distance, user))
        # sort based on distance -- closest first
        distances.sort()
        return distances
    elif(pear==1):
        distances = []
        for user in users:
            if user != username:
                distance = pearson(r, users[username], users[user])
                distances.append((distance, user))
        # sort based on distance -- closest first
        distances.sort(reverse=True)
        return distances
    elif(coeff==1):
        distances = []
        for user in users:
            if user != username:
                distance = cosineCoeffecient(r,users[username], users[user])
                distances.append((distance, user))
        # sort based on distance -- closest first
        distances.sort(reverse=True)
        return distances

def recommend(r, username, users, pear=0, coeff=0):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(r, username, users, pear, coeff)[0][1]

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

