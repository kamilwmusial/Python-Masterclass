with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
        






# Introduction to opening files with python:

# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.strip())
#     # print(line.strip(), end='')  # this function combine with end='', will remove the new line character from
#     # the end of the string producing one single long line of text
#     # print(line, end='')
#     # print(len(line))
# jabber.close()
