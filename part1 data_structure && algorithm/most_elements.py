# 怎样找出一个序列中出现次数最多的元素？

# collections.Counter类就是专门为这类问题而设计的，
# 甚至与一个有用的 most_common()方法直接给了你答案

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
morewords = [
    'look', 'into'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
# [('eyes', 8), ('the', 5), ('look', 4)]

# Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。 
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。比如：
word_counts['not']
# 1
word_counts['eyes']
# 8

# word_counts.update(morewords) 可以更新新的计数
# Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。比如：
a = Counter(words)
b = Counter(morewords)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
# "you're": 1, "don't": 1, 'under': 1, 'not': 1})
# b
# Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
# 'my': 1, 'why': 1})
# Combine counts
c = a + b
# c
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
# 'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
# 'looking': 1, 'are': 1, 'under': 1, 'you': 1})
# Subtract counts
d = a - b

print(d)
# d
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
# "you're": 1, "don't": 1, 'under': 1})
