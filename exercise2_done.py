"""
The following text is encrypted with an ancient encryption method called the `Caesar Cipher`.
Can you restore the original text?
Hints: Upper/lowercase does not matter. Nothing was done to punctuations.

Details of Caesar cipher:
https://en.wikipedia.org/wiki/Caesar_cipher
"""
encrypted_text = "CnwbxaOuxf rb jw nwm-cx-nwm xynw bxdaln yujcoxav oxa vjlqrwn unjawrwp. Rc qjb j lxvyanqnwbren, oungrkun nlxbhbcnv xo cxxub, urkajarnb jwm lxvvdwrch anbxdalnb cqjc uncb anbnjalqnab ydbq cqn bcjcn-xo-cqn-jac rw VU jwm mnenuxynab njbruh kdrum jwm mnyuxh VU yxfnanm jyyurljcrxwb."


def decode_caesar(text, key):
    alphabet = 'abcedfghijklmnopqrstuvwxyz'
    decoded_word = ''
    decoded_text = []
    encrypted = str.lower(text)  # .split(' ')
    for i in encrypted:  # range(len(encrypted)):
        # letter=encrypted[i]
        if i in alphabet:
            decoded_word += alphabet[(alphabet.index(i) + key) % 26]
        else:
            decoded_word += i
    decoded_text.append(decoded_word)
    return decoded_text


# print(decode_caesar(encrypted_text,1))

for k in range(1):
    text_out = decode_caesar(encrypted_text, k)
    print(text_out)
