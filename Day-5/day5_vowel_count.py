text = "education"
count = 0

for ch in text:
    if ch in "aeiou":
        print(ch,"is vowel in text education")
        count = count+1
print("Total vowels:",count)
