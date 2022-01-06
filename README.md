# Wordle-solver

Quick and dirty wordle solver.

This python script helps guess the word that was used to create the wordle. This script assumes that every word in the english language is a valid word. Even though this is not true, if you look the source code for wordle. When you enter a invalid word, wordle will tell you. Just use the next word in the list

This script generates the best first word based on scoring the letters in the word. According to this article that is not the best approch. Instead 
your first two guesses should be used to reduce the amount of possiable letters smaller list. For example. RAISE and PLANT. This script does not 
take this into account. https://notfunatparties.substack.com/p/wordle-solver

Updated version can be found here: https://github.com/funvill/wordle-solver

Play the game here: https://www.powerlanguage.co.uk/wordle/

Word list from: https://github.com/dwyl/english-words

## Running

Update the list of Green, Yellow, Gray letters in the source code.

```python wordle.py```

## Example output

```txt
Find the best first word for wordle!
https://www.powerlanguage.co.uk/wordle/

Green Letters, Know location   ['', 'i', '', 'e', 'r']
Yellow Letters, Wrong location ['r', 'e', 'i', 't']
Gray Letters, Not in word      ['a', 'o', 's', 'm', 'k']

Dictionary word count:     370103
Banned word count:         1 
Words with only 5 letters: 15917

Top 10 letters:
a 52.72 %
e 49.0 % 
s 41.06 % 
o 32.78 % 
r 32.31 % 
i 31.83 % 
l 26.68 % 
t 26.32 %
n 25.4 %
u 21.12 %

Top 10 words score: 
1 areae 37522 points
2 eases 37061 points
3 essee 36469 points
4 areas 36259 points
5 arase 36259 points
6 asses 35798 points
7 sasse 35798 points
8 sessa 35798 points
9 anasa 35752 points
10 asana 35752 points

Words with unique letters: 10172
Top Starting words:
1 arose 37522 points
2 oreas 37061 points
3 serai 36469 points
4 raise 36259 points
5 aesir 36259 points
6 aries 35798 points
7 arise 35798 points
8 alose 35798 points
9 solea 35752 points
10 osela 35752 points

Words that match the green letters, count: 94
1 airer 31541 points
2 riser 29686 points
3 aider 29210 points
4 aimer 28893 points
5 eider 28618 points
6 aiger 28370 points
7 eimer 28301 points
8 oiler 27472 points
9 sider 27355 points
10 tirer 27339 points

Words that match Yellow and Gray letters, count: 12
1 tirer 27339 points
2 liter 26443 points
3 tiler 26443 points
4 titer 26386 points
5 niter 26240 points
6 diter 25008 points
7 ticer 24941 points
8 citer 24941 points
9 tiber 24286 points
10 biter 24286 points

Your next guess should be: tirer

```
