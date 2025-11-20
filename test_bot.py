from telebot import TeleBot, types
import time 
bot = TeleBot("8018899255:AAFrcLGtFjWYdQHcI7fJqQjPMzltbjyFPeQ")

@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,f"""Salom!Bu bot yordamida siz IT sohasida o'z bilimingzni sinab ko'rishingiz mumkin🙂""")
    Ball = 0
    True1 = 0
    bot.send_message(message.chat.id, """API nima?
        A) Foydalanuvchi bilan botni bog'lovchi ko'prik.
        B) Botni ishlashi uchun yordam beruvchi parol.
        C) Botdan foydalanishimiz uchun yordam beruvchi bot.""")
    time.sleep(999999)
    if message.text == "A":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        Ball += 10
        True1 += 1        
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Dasturlashda kodlar qaysi tilga yaqin tilda yoziladi?
        A) Dasturlash tilida.
        B) Ingliz tilida.
        C) O'zbek tilida.""")
    time.sleep(999999)
    if message.text == "B":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0  
    bot.send_message(message.chat.id, """2 lik sanoq sistemasi qaysi sonlardan iborat?
    A) 1,2.
    B) 2
    C) 0,1.""")
    time.sleep(999999)
    if message.text == "C":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Dasturchi kim?
        A) Dasturlar yasovchi mutaxasis. U kodlar to'g'ri yoki noto'g'ri yozilganini tekshiradi.
        B) Dasturlar xavfsizligi va boshqa ma'lumotlarini ko'rib chiqib ularni tekshiradi.
        C) Dasturlar yasovchi mutaxasis.U kodlar yozadi va foydali narsalar yasaydi.""")
    time.sleep(999999)
    if message.text == "C":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Ko'plab dasturchilar qaysi ilovada kod yozishadi?
        A) Obsidiyan.
        B) Visual Studio Code.
        C) Blender.""")
    time.sleep(999999)
    if message.text == "B":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Terminalni ochish uchun qaysi buyruq ishlatiladi?      
        A) cmd.
        B) cls.
        C) sudo.""")
    time.sleep(999999)
    if message.text == "A":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Bilim nima qilinadi?
        A) Bilim  o'rganiladi.
        B) Bilim yuqadi.
        C) Bilim olinadi.""")
    time.sleep(999999)
    if message.text == "B":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Har bir dasturchini kompyuterida bo'lishi kerak bo'lgan ilova
        A) Instagramm
        B) Obsidiyan
        C) Visual Studio Code""")
    time.sleep(999999)
    if message.text == "C":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Hacker kim?
        A) Buzuvchi
        B) Egallovchi
        C) Yozuvchi""")
    time.sleep(999999)
    if message.text == "A":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, """Botni yaratish va tahrirlash uchun bizga nima kerak
        A) Telegram botni o'zi
        B) BotFather
        C) BotMother""")
    time.sleep(999999)
    if message.text == "B":
        bot.send_message(message.chat.id, "To'g'ri ✅")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
    else:
        bot.send_message(message.chat.id, "Noto'g'ri ❌")
        if Ball > 0:
            Ball -= 10
        else:
            Ball -= 0
        if True1 > 0:
            True1 -= 1
        else:
            True1 -= 0
        bot.send_message(message.chat.id, f"""To'g'ri javoblar: {True1}/10 \nTo'g'ri javoblarning foizlari: {Ball}%/100%""")

print("A")
bot.infinity_polling()