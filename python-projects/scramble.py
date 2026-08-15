import random

word = ["office", "word", "dad"]
random_word = random.choice(word)  # يختار كلمة عشوائية مثلاً: "office"

# تصحيح الخطأ: نحول الكلمة لقائمة حروف مباشرة ونخزنها في متغير
char_list = list(random_word)

random.shuffle(char_list)  # نخلط قائمة الحروف في مكانها

# ندمج الحروف المخلوطة مجدداً لتصبح نصاً واحداً
word_shuffle = "".join(char_list)

print(f"The scrambled word is: {word_shuffle}") # سيطبع مثلاً: ffoice

# تحديد عدد المحاولات المتاحة للمستخدم
attempts = 3
while attempts>0:
      guessed=input('Please guess the right word').lower()

      if guessed == random_word:
        print(f"🎉 Right guess! The word was indeed: {random_word}")
        break  # نخرج من الحلقة فوراً لأن الإجابة صحيحة
      else:
        attempts -= 1  # نخصم محاولة واحدة
      if attempts > 0:
            print("❌ Wrong guess! Try again.")
      else:
            print(f"💀 Game Over! The correct word was: {random_word}")

