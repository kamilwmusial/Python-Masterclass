def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:] # Return a copy of `string`.


def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix): # suffix '' should not call string [:-0]
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

# remove apostrophy, and other characters:
chars = "'Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]: # process backwards
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
# removing of first and last word using .removeprefix & .removesuffix:

# print('*' * 80)
# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
# toves_removed = first.removesuffix('toves')
# print(toves_removed)

# removing first and last workd using remove prefix and remove suffic functions defined at the top:
print('*' * 80)
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
toves_removed = removesuffix(first, 'toves')
print(toves_removed)