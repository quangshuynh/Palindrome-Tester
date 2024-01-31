from replit import clear

print("Welcome to the Palindrome Tester\nA palindrome is a word or a phrase that reads the same backward as forward. Ex. hannah or racecar\n\(Capitalization and Punctuation should be ignored)")

# Gets input 
word = input("Please input your word: "); 

new_word = "";
# Empty list
letter_list = [] 

# Analyzes letter of word
for i in range(0 , len(word), 1): 
	letter = word[i]
	letter_list.append(letter) 

for i in range(len(letter_list), 0, -1): 
	new_word =  new_word + letter_list[i - 1] 

# Checks if palindrome or not
if(word == new_word): 
	print(word + " is a palindrome!") 
else:
  print(word + " is not a palindrome.")