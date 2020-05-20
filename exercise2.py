"""
The following text is encrypted with an ancient encryption method called the `Caesar Cipher`.
Can you restore the original text?
Hints: Upper/lowercase does not matter. Nothing was done to punctuations.

Details of Caesar cipher:
https://en.wikipedia.org/wiki/Caesar_cipher
"""
encrypted_text = "CnwbxaOuxf rb jw nwm-cx-nwm xynw bxdaln yujcoxav oxa vjlqrwn unjawrwp. Rc qjb j lxvyanqnwbren, oungrkun nlxbhbcnv xo cxxub, urkajarnb jwm lxvvdwrch anbxdalnb cqjc uncb anbnjalqnab ydbq cqn bcjcn-xo-cqn-jac rw VU jwm mnenuxynab njbruh kdrum jwm mnyuxh VU yxfnanm jyyurljcrxwb."

#for homework
def decode_caesar(text, key):
    alphabet='abcedfghijklmnopqrstuvwxyz' 
    #validLetters = map(chr, range(97, 123))
    decoded_word=''
    decoded_text=[]
    encrypted =str.lower(text)#.split(' ')
    for i in encrypted:#range(len(encrypted)):
        #letter=encrypted[i]
        if i in alphabet: 
            
            decoded_word+=alphabet[(alphabet.index(i)+key) % 26]

        else:
            decoded_word+=i
    decoded_text.append(decoded_word)
    return decoded_text

print(decode_caesar(encrypted_text,1))   
# TODO
for k in ...:
    text_out = decode_caesar(encrypted_text, k)
    print(text_out)

#list
alphabets = 'abcdefghijklmnopqrstuvwxyz'
list_1 = ['fjsir', 'vnjk', 'eioafnvjf', 'einbvfbj']
list_2 = [3,4,7,1]
final_list = []
for index,original_word in enumerate(list_1):
    new_word = ''
    for letter in original_word:
        if letter in alphabets:
            index_val = alphabets.index(letter) - list_2[index]
            new_word += alphabets[index_val]
    final_list.append(new_word)
    
print(final_list)
        
        for letter in encrypted[i].lower():
        decoded_word += ''.join((chr(97+(ord(letter)-97+key) % 26) ))#for letter in encrypted[i]))
        decoded_word.apend( (chr(97+(ord(letter)-97+key) % 26)for letter in encrypted[i]))

       decided_text.append(decoded_word)
   

#for no space word
#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  
#check the above function 
text = "ATTACKATONCE"
s = 4
print "Text  : " + text 
print "Shift : " + str(s) 
print "Cipher: " + encrypt(text,s) 
#Output:
#Text : ATTACKATONCE
#Shift: 4
#Cipher: EXXEGOEXSRGI




#hack caesar cipher algorithm
#various possibilities, like Brute Force Technique
message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))





