introString= input("enter your introduction:")
characterCount=0
wordCount=1
for I in introString:
    characterCount=characterCount+1
    if(I==' '):
        wordCount=wordCount+1
print("no. of words ")   
print(wordCount)     
print("no. of characters")
print(characterCount)