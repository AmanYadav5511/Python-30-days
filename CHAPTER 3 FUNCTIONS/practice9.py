def count_vowels(word):
    count = 0
    for letter in word:
        if letter in 'aeiou':
            count = count + 1
    return count
print(count_vowels('education'))