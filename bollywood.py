import random;

def bollywood(count,bolly):
     for i in  range(count): 
        print (bolly[i],end=" ")


movieList =["The Martian","Interstellar","Slumdog Millionaire","Hot Tub Time Machine","Frozen"]
movieLetters = list(random.choice(movieList).lower())
guessLetters=[]
bolly = list("BOLLYWOOD")
count = 9
for i in  movieLetters :
    if i != " ":
        guessLetters.append("_")
    else :
        guessLetters.append(" ")


while(True) :
    bollywood(count,bolly)
    if count == 0:
        print ("Looks like you could not guess the Movie and your lives are over too")
        break
    print("\n\n")
    for i in guessLetters :
        print (i.upper(), end=" ")
    print("\n\n")
    if(guessLetters == movieLetters):
        print ("Successfully Guessed")
        break
    letter=input("Guess the letter:")
    if letter == "quit":
        break
    for i in range(len(movieLetters)) :
        if letter not in movieLetters:
            count= count - 1
            break
        if letter == movieLetters[i] and letter != " ":
            guessLetters[i] = movieLetters[i]
    