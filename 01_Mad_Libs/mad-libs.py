
#siguiendo trabajo de 12 different Python project tutorials.by Kylie Ying.
#https://www.youtube.com/watch?v=8ext9G7xspg&t=100s&ab_channel=freeCodeCamp.org
#----------
#formas de concatenación string
#Hay tres formas.
##Supongamos que queremos crear un string que diga "suscribe to ______"
#youtuber = "Santiago Bertorello" #variable	

#print("suscribe to " + youtuber)
#print("suscribe to {}".format(youtuber))
#print(f"suscribe to {youtuber}")

adj = input("Adjetive: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person: ")

madlib = f"Computer programing is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hidrated and {verb2} like you are {famous_person}!"

print(madlib)
