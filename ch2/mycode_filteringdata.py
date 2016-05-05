#
#  mycode_filteringdata.py
#
#  My Code file for the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#  Forrest Zhang
#  2016-5-4
#  v1

from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(rating1, rating2):
	distance = 0
	commeRating = False	#用于识别rating1、rating2是否有相同项

	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key]-rating2[key])	
			commeRating = True	#如果有一个相同项，就将标志字段置为True
		else:
			continue

	if commeRating:
		return distance
	else:
		return -1	#表示没有共同项

#---TDD---
#print(manhattan(users['Hailey'], users['Jordyn']))

def computeNearestNeighbor(username, users):

	nearestNeighbor = []

	for eachUser in users:
		if eachUser != username:
			distance = manhattan(users[eachUser], users[username])
			nearestNeighbor.append((distance, eachUser))

	nearestNeighbor.sort()	#原地排序
	return nearestNeighbor

#print(computeNearestNeighbor('Hailey', users))

def recommend(username, users):
	
	nearest = computeNearestNeighbor(username, users)[0][1]
	recommendations = []

	neighborRatings = users[nearest]
	userRatings = users[username]

	for artist in neighborRatings:
		if not artist in userRatings:
			recommendations.append((artist, neighborRatings[artist]))

	return sorted(recommendations, key = lambda artistTuple: artistTuple[1], reverse = True)	#产生新列表排序
	'?不理解artistTuple的来源'

print(recommend('Hailey', users))