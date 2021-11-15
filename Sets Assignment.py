sets = []
count=0
entry =""
print("Enter words ('stop to end):")
while entry.lower()!="stop":
    entry= input()
    if entry.lower() != "stop":
        sets.append(entry.lower())
wordSet = set(sets)
wordList = list(wordSet)
print(str(len(wordList)) + " unique words were entered: ")
print(wordSet)
