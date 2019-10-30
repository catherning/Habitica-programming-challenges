# Habitica-programming-challenges
 
## October 

Summary: Compute the scrabble score of a given word.

Link to the challenge:
https://habitica.com/challenges/460f9bb8-86ee-4bd3-ba2e-d747af94d258

### Challenge Description

In the game Scrabble each letter has a value. One completed word gives you a score.
Write a program that takes a word as an imput and outputs the calculated scrabble score.

Values and Letters:
1 - A, E, I, O, U, L, N, R, S, T
2 - D, G
3 - B, C, M, P
4 - F, H, V, W, Y
5 - K
8 - J, X
10 - Q, Z

Example:
The word "cabbage" gives you a score of 14 (c-3, a-1, b-3, b-3, a-1, g-2, e-1)

Extensions:
You can play a double or triple letter
You can play a double or triple word

### Program
The program lets you check for a word with the double or triple letter and word. 

You can accumulate the word multiplicators, so you can have the multiplicators 1, 2, 3, 2\*2=4, 3\*3=9 (not double and triple  at the same time because of the disposition of the board). \
You can mention it with the optional argument "--word_multiplicator 2" for example.

You can also have several letters with a multiplicator. \
For example, **for each letter** with a multiplicator, you add the optional argument "--letter_multiplicator [index] [multiplicator]".

**Example**: for the word "cabbage" with a word multiplicator of 2 and a triple multiplicator for the second letter (a), you call the python script like that
"python october_scrabble.py cabbage --word_multiplicator 2 --letter_multiplicator 1 3"
It gives a score of 2\*(13+3*1)=32 
 
### Future work: 
- check if the word is valid or not
- Take into account that if you have several letters with a multiplicator, the letters have the same multiplicator