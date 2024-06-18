def crypt(text,step):
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

plain_text="reu efn kyvp riv ljzex dp kirjytre jf zk nzcc sv wlcc wrjkvi...jdy nyp dv?"
step_count=17
encryption= crypt(plain_text,step_count)
decryption = crypt(plain_text,-step_count)
print(encryption)
print(decryption)
        

         



