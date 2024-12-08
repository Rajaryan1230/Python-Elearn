name = str(input('What is your name? '))
print('Your name has', len(name), 'characters')


first = input('Write your first name: ')
second = input('Write your last name: ')
fullname = (first +" "+ second)
print('Your full name is' , fullname)


favani = input('What is your favorite animal? ')
print(favani.upper())
print(favani.lower())


day = input('What is the day of the week? ')
char = input('Pick any one letter in that day of the week: ')
print("The amount of times that character appears is", day.count(char))


og = input('Write any statment: ')
replaced = input('Write a word that should be replaced with another in the statment: ')
newword = input('Write the word that will replace it: ')
print(og.replace(replaced, newword))


num1 = input('Write anything that you would like: ')
starts = input('Write a word and I will check if your statment starts with that word: ')
ends = input('Write another word and I will check if your statment ends with that word: ')
print(num1.startswith(starts))
print(num1.endswith(ends))


stringentered = input('Write the biggest word you know: ')
print('I will check how many times a certain letter appears in', stringentered)
character = input('What do you want the letter to be : ')
print(stringentered.count(character), 'is how many times', character, 'appeared in your word')


school = input('What school do you go to: ')
print(school.title())


subject = input('What is your favorite subject in school in random caps and no caps order: ')
print(subject.swapcase())
