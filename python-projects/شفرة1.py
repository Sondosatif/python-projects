def multiply(number):
    for x in range(1,11):
        print(f"{number} x {x} = {number*x}")
multiply(6)

name="sondos"
print(name.index("s"))

import string

alphabet=string.ascii_lowercase
word=input("Please type a word :").lower()
encrypted_word=""

for letter in word:
    if letter in alphabet:# نتأكد أن المدخل حرف وليس مسافة أو رقم
# 1. نجد موقع الحرف الأصلي في الأبجدية
       index1=alphabet.index(letter)
 # 2. نضيف 2 ونستخدم % 26 لمنع الخروج عن حدود الأبجدية (مثل حرف z يلتف ليصبح b
       index2=(index1+2)%26
       new_letter=alphabet[index2]
# 3. ندمج الحرف الجديد مع النص باستخدام += بدلاً من append      
       encrypted_word+=(new_letter)
    else:
        # إذا كان هناك مسافة أو رمز، نتركه كما هو دون تشفير
        encrypted_word += letter

print(f"Encrypted word: {encrypted_word}")

    