
def test_anagram(word1,word2):
    word1 = list(word1)
    word2 = list(word2)
    dict1 = dict()
    dict2 = dict()
    for i in range(len(word1)):
        if word1[i] == " ":
            continue
        dict1[word1[i]] = dict1.get(word1[i],0) +1
        dict2[word2[i]] = dict2.get(word2[i],0) +1
    flag = False
    for j in dict1.keys():
        if j in dict2:
            if dict1[j] == dict2[j]:
                flag = True
            else:
                flag = False
                break

    return flag
        

while True:
        
    word1 = input("Enter First word :")
    word2 = input("Enter Second word :")

    if len(word1) != len(word2):
        print("Please enter the same count of letters at two words")
        continue
    
    print(f"The anagram test is {test_anagram(word1,word2)}")
    quest = input("Do you want another one? (y/n)")
    if quest.lower() == 'n':
        break
