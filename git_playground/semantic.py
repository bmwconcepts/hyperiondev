#===compulsory task 1====
#imports
import spacy

#set advanced enlgish language model for spacy
nlp = spacy.load("en_core_web_md")


#compares each token to eachother in every combo
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
#Notes: Relative objects such as animal - animal and fruit - fruit rank high.
#- interestingly somewhat relateable objects such as monkey - banana rate higher than unrelatables such as cat - apple

#my example
tokens = nlp('cat bird flap poop ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
#This sample highlights that there is more of a focus on similarity between object types
#i.e. animals instead of relatable actions or word combinations.
#Cat flap is a clear english word and bird flap could be related to the animals movement
#however these score low. 


#Notes for example: when corresponding items such as recipes are compared to the same class,
#the rating average is much higher than when compared to a different set entirely.
#However interestingly the alternate comparisons still rank higher than polar opposites.
#When changed to the basic nlp model, the averages drop susbtantially and the gap between
#identifying recipes vs complaints drops to a much closer margin than the advanced model.