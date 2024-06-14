from itertools import permutations
def solve_cryptarithmetic(word1, word2, result):
    letters = set(word1 + word2 + result)
    if len(letters) > 10:
        return None  
    for perm in permutations('0123456789', len(letters)):
        mapping = {letter: digit for letter, digit in zip(letters, perm)}
        if mapping[word1[0]] == '0' or mapping[word2[0]] == '0' or mapping[result[0]] == '0':
            continue
        num1 = int(''.join(mapping[letter] for letter in word1))
        num2 = int(''.join(mapping[letter] for letter in word2))
        res = int(''.join(mapping[letter] for letter in result))
        if num1 + num2 == res:
            return mapping
    return None  
def main():
    word1 = input("Enter the first word: ").upper()
    word2 = input("Enter the second word: ").upper()
    result = input("Enter the result word: ").upper() 
    solution = solve_cryptarithmetic(word1, word2,  result)
    if solution:
        print("Solution found:")
        for letter in sorted(solution.keys()):
            print(f"{letter}: {solution[letter]}")
    else:
        print("No solution found")
if __name__ == "__main__":
    main()
