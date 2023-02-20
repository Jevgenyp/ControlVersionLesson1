def count_glasnie(word):
    glasnie = set("aeiouyAEIOUY")
    count = 0
    for letter in word:
        if letter in glasnie:
            count += 1
    return count

poem = input("Введите стихотворение Винни-Пуха: ")

phrases = poem.split()

glasnie_count = [count_glasnie(phrase.replace('-', '')) for phrase in phrases]

if len(set(glasnie_count)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")