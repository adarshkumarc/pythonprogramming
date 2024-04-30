number_of_words = 0
with open(r'SampleFile.txt', 'r') as file:
    data = file.read()
    words = data.split()
    number_of_words += len(words)
print(number_of_words)
