def mysplit(strng):
    strng = strng.strip()
    if strng.isspace() or strng == '':
        return []
    
    splits = []

    while strng.find(' ') != -1:
        space_position = strng.find(' ')
        splits.append(strng[0:space_position])
        strng = strng[space_position + 1:]

    splits.append(strng)
    return splits

print(mysplit("Być albo nie być, oto jest pytanie") 
      == "Być albo nie być, oto jest pytanie".split()
      )
print(mysplit("Być albo nie być,oto jest pytanie") 
      == "Być albo nie być,oto jest pytanie".split()
      )
print(mysplit("   ") == "   ".split())
print(mysplit(" abc ") == " abc ".split())
print(mysplit("") == "".split())