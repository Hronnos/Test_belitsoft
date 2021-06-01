symbols_list = ['a', 'b', 'c', 'c']

def first_rep(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return s[i]

print(first_rep(symbols_list))
