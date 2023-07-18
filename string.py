mystr = "my name is amit"

education = "i am a student of B.Tech"

# make first letter capital
mystr = mystr.capitalize()
print(mystr)

# make all letters capital
mystr = mystr.upper()
print(mystr)

# make all letters small
mystr = mystr.lower()
print(mystr)

# make first letter of each word capital
mystr = mystr.title()
print(mystr)

# find the index of a substring
print(mystr.find("Name"))


# find length of a string
print(len(mystr))

# strip a string

mystr = "   my name is amit   "
print(mystr.strip())
print(mystr.lstrip())
print(mystr.rstrip())


