words = ' to perform the task of sorting the words in a string by their length'.split()
wordlens = [(len(word), word) for word in words]
wordlens.sort()
print (' '.join(w for (_, w) in wordlens))

dots = '_'
my_str = dots.join(['1', '2', '3', str(5)])
print(my_str)

my_str = dots.join('abcd')
print(my_str)


a = "п р о с т о жопа".split( maxsplit = 10)
print(a)

b = '+'
s = b.join(["1", "2", "3", "4", "9", "55"])
print(s)











#c = a.join(a)


