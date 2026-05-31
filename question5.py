def is_anagram(s1,s2):
    if len(s1) !=len(s2):
        return False
    
    count={}
    for ch in s1:
        count[ch]=count.get(ch,0)+1
    for ch in s2:    
        if ch not in count:
            return False
        count[ch]-=1
    for value in count.values():
        if value !=0:
            return False
    return True    
s1=input("Enter the 1st string:")
s2=input("Enter the 2nd string:")

if is_anagram(s1,s2):
    print("These are Anagrams.")
else:
    print("These are not Anagrams.")    