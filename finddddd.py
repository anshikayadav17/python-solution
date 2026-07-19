s = input("Enter String: ")

for ch in set(s):
    print(ch, "=", s.count(ch))
