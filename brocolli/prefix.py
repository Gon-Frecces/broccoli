pack_words = []
while True:
    word = input("Enter word: ")
    if word == '/':
        break
    pack_words.append(word)

# print(pack_words)
shogun = []

for j, word in enumerate(pack_words):
    try:
        for i, character in enumerate(word):
            g = iter(character)
            character = next(g)
            if pack_words[0][i] == pack_words[j + 1][i]:
                character = character.split()
                shogun.extend(character)
                # print(character)
                # print(shogun)

            # else:
            #     print('The words entered do not have common prefixes')
                lab = ''.join(shogun)
                # print(lab)
    except IndexError:
        pass

prefix = shogun[0]
first_letter = prefix
# a = iter(shogun[1:])
try:
    for char in shogun[1:]:
        # k = next(a)
        if char == first_letter:
            break
        else:
            prefix += char
            # continue
        # while prefix == k:
        #     k = next(a)
        #     prefix += k


except StopIteration:
    pass
print(prefix , ' are the common prefixes')

# pf = ''
# for x, k in enumerate(shogun):
#     while str(shogun[0]) != str(shogun[k + 1]):
#         pf += shogun[k + 1]
# print(pf)

# print(words[0])
# prefix '' loop through all the characters(char, index), loop through all the strings if str[index] == char continue
# else return prefix
# prefix = prefix E+ char i = character loop, j = string loop
# IF word[0][i] n char[i] = word[1][i] n char[i] =  word[2][i] n char[i] return prefix
