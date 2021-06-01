symbols_list = ['a', 'b', 'c', 'c']

def first_rep(s):
    try:
        for i in range(len(s) - 1):
            assert s[i] == str(s[i])
            if s[i] == s[i + 1]:
                return s[i]
    except AssertionError:
           return 'Это не строка!'

print(first_rep(symbols_list))