'''

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .


'''

def minion_game(string):
    # your code goes here
    vow = "AEIOU"
    slen = len(string)
    tsub = int(slen * (slen + 1) / 2)
    k = sum(slen - i for i in range(slen) if string[i] in vow)   
    s = tsub - k

    if s > k: print(f"Stuart {s}")
    elif s < k: print(f"Kevin {k}")
    else: print("Draw")

