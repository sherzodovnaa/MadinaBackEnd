from telegraph import Telegraph

savol = """
<b>TOP 5 SAVOLLAR:
"1. Ustozlar malakasi qanday?"
"2. Keyinchalik tilni mukammal o'rgana oladimi?"
"3. Boshqa o'quv markazlardan nima farqi bor?"
"4. Nechi yildan beri dars berasizlar?"
"5. Qancha vaqt o'qiydi?</b>

Javobnlarni bilish uchun pastdagi kamandani bosina!
/quiz
"""

quiz="""
1. Oliy ma'lumotli 4-5 yil tajribali
2. Tilni mukammal o'rgana oladi va sertifikat ham beriladi
3. Farqi bu biz o'qituvchilarimiz tajribasi va mukammal dars o'rgatish usuli
4. 5-6 yildan
5. Harakatdan to'xtamasa 1,5-2 yilda til sertifikatini qo'lga kirita oladi
"""

telegraph = Telegraph()
telegraph.create_account(short_name="Madina_kurs_bot")

response = telegraph.create_page(
    title="Top 5 savollar",
    content=[
        {
            "tag":"h3",
            "children":["1. Ustozlar malakasi qanday?"]
        },
        {
            "tag":"p",
            "children":[" 1. Oliy ma'lumotli 4-5 yil tajribali"]
        },
        {
            "tag":"h3",
            "children":["2. Keyinchalik tilni mukammal o'rgana oladimi?"]
        },
        {
            "tag":"p",
            "children":[" 2. Tilni mukammal o'rgana oladi va sertifikat ham beriladi"]
        },
        {
            "tag":"h3",
            "children":["3. Boshqa o'quv markazlardan nima farqi bor?"]
        },
        {
            "tag": "p",
            "children": [" 3. Farqi bu biz o'qituvchilarimiz tajribasi va mukammal dars o'rgatish usuli"]

        },
        {
            "tag":"h3",
            "children":["4. Nechi yildan beri dars berasizlar?"]
        },
        {
            "tag":"p",
            "children":["4. 5-6 yildan"]
        },
        {
            "tag": "h3",
            "children": ["Qancha vaqt o'qiydi?"]
        },
        {
            "tag": "p",
            "children": ["5. Harakatdan to'xtamasa 1,5-2 yilda til sertifikatini qo'lga kirita oladi"]
        },
        {
            "tag": "a",
            "attrs":{"href": "https://t.me"} ,
            "children": ["Bot yaratish"]
        }
    ],
    author_url="https://t.me/",
    author_name="Madina Bot"
)
TELEGRAPH_LINK = f"<a href='{response['url']}'>Eng ko'p so'raladigan savollar.</a>"