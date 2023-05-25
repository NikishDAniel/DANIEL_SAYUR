############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like


# friend number diaplay
print("Friend 1: ")
movies = input("What movies you like ? ")
moviesList = movies.split()         # converting the input into list
commonMovieCount = 0

# looping until there is a break occurs
while (True) :
    print("Friend 2: ")
    #asking input from the second friend
    movie = input("What movie you like? ")
    #Check if this movie is in the movie list
    if movie in moviesList:
        print(f"You both like {movie}")
        commonMovieCount += 1
        #checking if we reach the limit
        if(commonMovieCount >= 3):
            break
    else:
        print ("Try again")


'''
output  1 --
Friend 1: 
What movies you like ? kgf kgf2 avengers shazam vaarisu beast
Friend 2: 
What movie you like? kgf
You both like kgf    
Friend 2: 
What movie you like? 3
Try again
Friend 2: 
What movie you like? kgf2
You both like kgf2   
Friend 2: 
What movie you like? kee
Try again
Friend 2: 
What movie you like? vaarisu
You both like vaarisu
'''



'''
output 2 --
Friend 1: 
What movies you like ?  kgf kgf2 avengers shazam vaarisu beast
Friend 2: 
What movie you like? kgf
You both like kgf    
Friend 2: 
What movie you like? kgf2
You both like kgf2   
Friend 2: 
What movie you like? beast
You both like beast

'''