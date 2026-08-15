import string

alphabet=string.ascii_lowercase
word=input("Please type a word :").lower()
orginal_word=""


for letter in word:
    if letter in alphabet:# نتأكد أن المدخل حرف وليس مسافة أو رقم
# 1. نجد موقع الحرف الأصلي في الأبجدية
       index1=alphabet.index(letter)
 # 2. نضيف 2 ونستخدم % 26 لمنع الخروج عن حدود الأبجدية (مثل حرف z يلتف ليصبح b
       index2=(index1-2)%26
       new_letter=alphabet[index2]
# 3. ندمج الحرف الجديد مع النص باستخدام += بدلاً من append      
       orginal_word+=(new_letter)
    else:
        # إذا كان هناك مسافة أو رمز، نتركه كما هو دون تشفير
        orginal_word += letter

print(f"Encrypted word: {orginal_word}")