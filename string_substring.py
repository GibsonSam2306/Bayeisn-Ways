string = input("input: ")
substring = input("pattern: ")

string_lower = string.lower()
substring_lower = substring.lower()

len_string = len(string_lower)
len_substring = len(substring_lower)

count = 0

for i in range(len_string - len_substring + 1):
    if string_lower[i:i + len_substring] == substring_lower:
        count += 1

print("output:", count)
