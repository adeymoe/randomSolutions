"""def two_sort(array):
    array.sort()
    print(array[2])

two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"])"""

def two_sort(array):
    # your code here
    array.sort()
    word = list(array[0])
    newWord = []
    for i,n in enumerate(word):
        newWord.append(n)
        if i != len(word)-1:
            newWord.append("***")

    finalWord = "".join(newWord)
    return(finalWord)
        

    

two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"])