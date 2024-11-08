from collections import Counter
string = input("Enter a String : ")
char_count = Counter(string)

for char,count in char_count.items():
    print(f"{char} : {count}")
