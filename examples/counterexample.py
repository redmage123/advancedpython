#!/usr/bin/python3

from collections import Counter

wordList = ['foo','foo','bar','bar','baz','blech','foo','foo','bar','meh','feh','feh']

wordCount = Counter(wordList)
# Print the count of key values
print (wordCount)
# Print the top two keys
print (wordCount.most_common(2))
