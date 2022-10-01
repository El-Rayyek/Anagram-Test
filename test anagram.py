

def test_anagram(word1,word2):
    count = 0
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                count += 1
                word2.replace(word2[j],'')
                break
            
    if count == len(word1):
        return True
    else:
        return False

word1 = input("Enter First word :")
word2 = input("Enter second word :")

print(test_anagram(word1,word2))
                
        

