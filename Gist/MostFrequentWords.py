from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_count = Counter(words)
top_three = word_count.most_common(3)
print(top_three, word_count, word_count['eyes'])

for word in words:
    word_count[word] += 1
print(word_count['eyes'])
