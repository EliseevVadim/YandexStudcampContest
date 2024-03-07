n = int(input())
array = input()
array = list(map(int, array.split(' ')))

numbers_frequencies = {}

for number in array:
    if number in numbers_frequencies:
        numbers_frequencies[number] += 1
    else:
        numbers_frequencies[number] = 1


sorted_frequencies = sorted(numbers_frequencies.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(sorted_frequencies[0][0])
