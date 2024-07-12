from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from loader import dp, bot
from data.products import python_book, ds_praktikum, FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING, \
javasc_book,python_web_framework,htmlcss_book
from keyboards.inline.product_keys import build_keyboard


@dp.message_handler(Command("python"))
async def show_invoices(message: types.Message):
    caption = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n\n"
    caption += "Ushbu kitob bugungi kunda dasturlash asoslariga oid o’zbek tilidagi mukammal tuzilgan qo’llanmalardan biridir.\n\n"
    caption += "Qo’lingizdagi kitobning o’ziga xos jihati shundaki, uning har bir bo’limi uchun tayyorlangan qo'shimcha onlayn"
    caption += "materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg’ulotlar va vazifalarning kodlari e’tiboringizga havola etilgan.\n\n"
    caption += "O’quvchilar bu materiallarni maxsus QR kod yordamida o’z komputerlariga yuklab olib, ulardan unumli foydalanishi mumkin.\n\n"
    caption += "Narxi: <b>50000 so'm</b>"
    await message.answer_photo(photo="https://i.imgur.com/0IvPPun.jpg",
                               caption=caption, reply_markup=build_keyboard("python"))

@dp.message_handler(Command("javasc"))
async def show_invoices(message: types.Message):
    caption = "<b>JavaScript Dasturlash Asoslari</b> kitobi.\n\n"
    caption += "Ushbu kitob bugungi kunda dasturlash asoslariga oid o’zbek tilidagi mukammal tuzilgan qo’llanmalardan biridir.\n\n"
    caption += "Qo’lingizdagi kitobning o’ziga xos jihati shundaki, uning har bir bo’limi uchun tayyorlangan qo'shimcha onlayn"
    caption += "materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg’ulotlar va vazifalarning kodlari e’tiboringizga havola etilgan.\n\n"
    caption += "O’quvchilar bu materiallarni maxsus QR kod yordamida o’z komputerlariga yuklab olib, ulardan unumli foydalanishi mumkin.\n\n"
    caption += "Narxi: <b>65000 so'm</b>"
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQk0IaRDjBvZC4Ga4GfQPWxacgvFVTF1rlWUw&s",
                               caption=caption, reply_markup=build_keyboard("javasc"))

@dp.message_handler(Command("htmlcss"))
async def show_invoices(message: types.Message):
    caption = "<b>HTML va CSS Dasturlash Asoslari</b> kitobi.\n\n"
    caption += "Ushbu kitob bugungi kunda dasturlash asoslariga oid o’zbek tilidagi mukammal tuzilgan qo’llanmalardan biridir.\n\n"
    caption += "Qo’lingizdagi kitobning o’ziga xos jihati shundaki, uning har bir bo’limi uchun tayyorlangan qo'shimcha onlayn"
    caption += "materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg’ulotlar va vazifalarning kodlari e’tiboringizga havola etilgan.\n\n"
    caption += "O’quvchilar bu materiallarni maxsus QR kod yordamida o’z komputerlariga yuklab olib, ulardan unumli foydalanishi mumkin.\n\n"
    caption += "Narxi: <b>65000 so'm</b>"
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkUpwTsaFN18gjm8Pibq5Ws5ATQzvjAJjWTg&s",
                               caption=caption, reply_markup=build_keyboard("htmlcss"))

@dp.message_handler(Command("data"))
async def show_invoices(message: types.Message):
    caption = "<b>Data Science va Sun'iy Intellekt</b> praktikum.\n\n"
    caption += "6 oyda eng zamonaviy kasb egasi bo'ling.\n\n"
    caption += "Kurs tarkibi:\n"
    caption += "✅ Python Dasturlash Asoslar (4 hafta)\n"
    caption += "✅ Data Sciencega kirish va DS metodologiyasi (2 hafta)\n"
    caption += "✅ Maʻlumotlar tahlili (Data Analysis) (4 hafta)\n"
    caption += "✅ Maʻlumotlarga ishlov berish (4 hafta)\n"
    caption += "✅ Vizualizasiya (2 hafta)\n"
    caption += "✅ Machine Learning (6 hafta)\n"
    caption += "✅ Deep Learning (4 hafta)\n"
    caption += "✅ Natural Language Processing (4 hafta)\n\n"
    caption += "Narxi: <b>1.5mln so'm</b>"

    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoiHNdY72DRg4I_9CF8hplFNLIeQo_MPkdcw&shttps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoiHNdY72DRg4I_9CF8hplFNLIeQo_MPkdcw&s",
        caption=caption, reply_markup=build_keyboard("data"))


@dp.message_handler(Command("pythonfr"))
async def show_invoices(message: types.Message):
    caption = "<b>O'zingizning Python veb-ramkangizni yaratish</b>.\n\n"
    caption += "Ush kursda siz Flask, Django va boshqa Python-ga samarali web frameworklar qanday ishlab chiqarishni ko'rish uchun o'zingizni Python web framework qanday ishlab chiqarishni o'rganasiz.\n\n"
    caption += "Kurs tarkibi:\n"
    caption += "✅ Python Dasturlash Asoslar\n"
    caption += '✅Eng muhimi, dasturchi sifatida siz boshqa dasturchilar uchun nimadir yaratasiz\n ✅Bu sizning kundalik ishingizda narsangizdan biroz farq qilishi mumkin va shunday qilib ko\'p narsalarni o\'rganasiz.\n✅Eng muhimi, dasturchi sifatida siz boshqa dasturchilar uchun nimadir yaratasiz, bu sizning kundalik ishingizda narsangizdan biroz farq qilishi mumkin va shunday qilib ko\'p narsalarni o\'rganasiz.\n\n'
    text = "<a href='https://skillup.uz/courses/building-your-own-python-web-framework'>Python</a>"
    caption += f"Kursni ko'rish {text}\n"
    caption += "Narxi: <b>300 ming so'm</b>"

    await message.answer_photo(
        photo="https://skillup-prod.s3.amazonaws.com/media/courses/5da5da9d-d40b-4e5e-9b59-dad728d3dd28/8eadb308-7fa8-4d56-988e-8ebe8d6b1aac.jpeg",
        caption=caption, reply_markup=build_keyboard("pythonfr"))


@dp.message_handler(Command("books"))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_book.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **javasc_book.generate_invoice(),
                           payload="123457")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **htmlcss_book.generate_invoice(),
                           payload='1234567')

@dp.message_handler(Command("kurslar"))
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="123457")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_web_framework.generate_invoice(),
                           payload="123457")


@dp.callback_query_handler(text="product:python")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_book.generate_invoice(),
                           payload="payload:python")
    await call.answer()


@dp.callback_query_handler(text="product:praktikum")
async def praktikum_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="payload:praktikum")
    await call.answer()


@dp.callback_query_handler(text="product:pythonfr")
async def python_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_web_framework.generate_invoice(),
                           payload="payload:pythonfr")
    await call.answer()

@dp.callback_query_handler(text="product:javasc")
async def javascript_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **javasc_book.generate_invoice(),
                           payload="payload:javasc")
    await call.answer()

@dp.callback_query_handler(text="product:htmlcss")
async def htmlandcss_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **htmlcss_book.generate_invoice(),
                           payload="payload:htmlcss")
    await call.answer()

@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")
