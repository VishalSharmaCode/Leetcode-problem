def longestPrefix(strs):
    if not strs:
        return ''
    for i in range(len(strs[0])):
        char = strs[0][i]
        print("char:>", char)
        for other in strs[1:]:
            print("other:>", other)
            print("other[i]:>", other[i])
            if i >= len(other) or other[i] != char:
                return strs[0][:i]
    return strs[0]

strs = ["flower","flow","flight"]

print("longestPrefix(strs):>", longestPrefix(strs))