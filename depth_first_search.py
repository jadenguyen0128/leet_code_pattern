def letter_combinations(digits):
    if len(digit) == 0:
        return []
    letter_map = ["", "", "abc", "def", "ghi", "jkl", 
                   "mno", "pqrs", "tuv", "wxyz"]
    def dfs(digits, letter_map, result, sb, index):
        if len(sb) == len(digits):
            result.append(''.join(sb))
            return
        letters = letter_map[int(digits[index])]
        for letter in letters:
            sb.append(letter)
            dfs(digits, letter_map, result, sb, index + 1)
            sb.pop()

    result = []
    dfs(digits, letter_map, result, [], 0)
    return result
