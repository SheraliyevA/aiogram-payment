from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


ds_praktikum = Product(
    title="Data Science va Sun'iy intellekt",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Praktikum',
            amount=15000, #150.00$
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-1000, #-10.00$
        ),
    ],
    start_parameter="create_invoice_ds_praktikum",
    photo_url='https://i.imgur.com/vRN7PBT.jpg',
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)

python_book = Product(
    title=f"Pythonda Dasturlash Asoslari ",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=500,#5.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,#1.00$
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRULRbwjy-qMfy8Y4XyPDDImVrTv4TsvSgLZg&s',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)
javasc_book = Product(
    title="JavaScript Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=600,#6.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,#1.00$
        ),
    ],
    start_parameter="create_invoice_javasc_book",
    photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQk0IaRDjBvZC4Ga4GfQPWxacgvFVTF1rlWUw&s',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

htmlcss_book = Product(
    title="HTML va CSS Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=600,#6.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,#1.00$
        ),
    ],
    start_parameter="create_invoice_htmlcss_book",
    photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkUpwTsaFN18gjm8Pibq5Ws5ATQzvjAJjWTg&s',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)
python_web_framework=Product(
    title="Pythonda Web Framework yozish",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="USD",
    prices=[
        LabeledPrice(
            label='Kurs',
            amount=3000,#30.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=100,#1.00$
        ),
    ],
    start_parameter="create_invoice_python_web",
    photo_url='https://skillup-prod.s3.amazonaws.com/media/courses/5da5da9d-d40b-4e5e-9b59-dad728d3dd28/031dee9f-f4a4-48c8-9226-14490704a8ce.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 100),
        LabeledPrice(
            '3 ish kunida yetkazish', 100),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 100),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -100)
                                       ])