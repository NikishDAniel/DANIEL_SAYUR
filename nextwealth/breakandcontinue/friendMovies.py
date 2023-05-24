############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like

#init variables
movies = input("What movies you like ? ")
#convert movies into a List
moviesList = movies.split()
#FillinMissingCode
commonMovieCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input("What movie you like? ")
    #Check if this movie is in the movie list
    if movie in moviesList:
    #FillinMissingCode
        print(f"You both like {movie}")
        commonMovieCount += 1
    #if present, 
    #check if we reached the max
        if(commonMovieCount >= 3):
            break
    else:
        print ("Try again")

print () #FillinMissingCode - list all the common movies