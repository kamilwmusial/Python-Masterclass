# with open('Jabberwocky.txt', 'r') as jabber:
#     lines = jabber.readlines()
#
# print(lines) # the output of this produces a list of strings, which can be indexed or sliced:
# print(lines[-1:]) # the output of this returns the credits to the author separately from the rest of the text
# for line in reversed(lines):
#     print(line, end='') # do some processing in reverse order - prints out the text backwards

#
# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()
#
# # print(text)
# for character in reversed(text):
#     print(character, end='') # reverses the entire contencts of the string

# read line method:
with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)
with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break
