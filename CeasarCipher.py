def crypt(text,step):
    """
    Encrypts or decrypts a given string using a Caesar cipher.

    Args:
        text (string): The string to be encrypted or decrypted.
        step (int): The number of positions each character in the string should be shifted.

    Returns:
        string: The encrypted or decrypted string.
    """

    res_text=""

    for i in text:

        if i.isalpha():
            if i.isupper():
                res_text += chr((ord(i) + step - 65) % 26+65)
            else:
                res_text += chr((ord(i) + step - 97) % 26+97)
        else:
            res_text+=i
    return res_text

plain_text="Yz, Kyzj zj Erdirkyr"
step_count=17
encryption= crypt(plain_text,step_count)
decryption = crypt(plain_text,-step_count)
print(encryption)
print(decryption)
        

         



