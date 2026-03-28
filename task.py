combinations =  {"2" : ['a', 'b', 'c'],
                "3" : ['d', 'e', 'f'], 
                "4" : ['g', 'h', 'i'],
                "5" : ['j', 'k', 'l'], 
                "6" : ['m', 'n', 'o'], 
                "7" : ['p', 'q', 'r', 's'], 
                "8" : ['t', 'u', 'v'], 
                "9" : ['w', 'x', 'y', 'z']}

def LetterCombinations(digits):

    if digits == "":
        return []
    
    if len(digits) > 4:
        raise ValueError("Input too long")
    
    for d in digits:
        if d not in combinations:
            raise ValueError("Invalid digit")
    
    result = [""]
    
    for digit in digits:
        letters = combinations[digit]
        result = [x + y for x in result for y in letters]
        
    return sorted(result)


# examples

#print(LetterCombinations(""))
#print(LetterCombinations("2"))
#print(LetterCombinations("45"))
#print(LetterCombinations("565"))