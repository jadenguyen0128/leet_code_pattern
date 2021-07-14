# depth first search
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# inspired by kenny's tutorial: https://www.youtube.com/watch?v=nNGSZdx6F3M&t=305s

# similar problems with letter combinations from phone number
# generate parentheses
# permutation
# combination sum
# subsets


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
