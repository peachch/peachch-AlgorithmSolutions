def letterCombinations(digits):

    def trackback(index):
        if index == len(digits):
            res.append("".join(combination))
            return
        for letter in num_words[digits[index]] :
            combination.append(letter)
            trackback(index+1)
            combination.pop()

    num_words = {"2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]}

    if digits == "":
        return []
    res = []
    combination = []
    trackback(0)
    return res



digits = "34"
print(letterCombinations(digits))
