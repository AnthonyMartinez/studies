braille = {
		'O.....': 'a',
		'O.O...': 'b',
		'OO....': 'c',
		'OO.O..': 'd',
		'O..O..': 'e',
		'OOO...': 'f',
		'OOOO..': 'g',
		'O.OO..': 'h',
		'.OO...': 'i',
		'.OOO..': 'j',
		'O...O.': 'k',
		'O.O.O.': 'l',
		'OO..O.': 'm',
		'OO.OO.': 'n',
		'O..OO.': 'o',
		'OOO.O.': 'p',
		'OOOOO.': 'q',
		'O.OOO.': 'r',
		'.OO.O.': 's',
		'.OOOO.': 't',
		'O...OO': 'u',
		'O.O.OO': 'v',
		'.OOO.O': 'w',
		'OO..OO': 'x',
		'OO.OOO': 'y',
		'O..OOO': 'z'
		}
def translate(text):
	result = ""
	for t in text:
		result += braille[t]
	return result

trans = []
words = []
finalwords = []
with open("braille.txt", "r") as f:
	for line in f:
		trans.append(line)

i = 0
for t in trans:
	words.append([])
	for s in t.strip('\n').split(' '):
		words[i].append(s)
	i += 1
for i in range(len(words[0])):
	finalwords.append('')
	for j in range(3):
		finalwords[i] += words[j][i]

print translate(finalwords)
