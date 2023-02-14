#===compulsory task 2===
#Rates a movie description for similarities against others then displays the best related choice

#Imports
import spacy

#Set spacy language model to english advanced
nlp = spacy.load('en_core_web_md')

#Set comparison move description & tokenise it
planet_hulk = "Will he save the world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


#Define similarity checking function that returns dictionary of keys (ratings) and values (movie description)
def similar_finder(description):
    comparisons = {}
    with open("movies.txt", "r") as movies_file:
        movie_list = movies_file.readlines()
        #tokenise each movie description
        for movie in movie_list:
            movie = nlp(movie)
            description = nlp(description)
            #compare each movie to planet hulk
            movie_sim = description.similarity(movie)
            #add description and rating to k,v dictionary
            comparisons[movie_sim] = (movie)
    return(comparisons)

#find the maximum rating (as a key in the dictionary)
match_dict = similar_finder(planet_hulk)
best_match = max(match_dict, key=float)
#Display the best matched movie description & rating
output = f"Best match: {match_dict[best_match]}"
output += f"Rating: {int((round(best_match, 2)*100))}%"
print(output)