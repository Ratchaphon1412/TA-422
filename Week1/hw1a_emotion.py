####
#
# วิชา 01422422 ปีการศึกษา 2566 ภาคต้น
# ชื่อ-นามสกุล:
# อีเมล:
# รหัสนิสิต:
#
####
#
# การบ้าน 1A - EMOTION
#
# จงเขียนโค้ดเพื่อนับจำนวนประโยคที่มีความสุข และประโยคที่มีความเศร้า
#
# ตัวอย่างผลลัพธ์
# There are 0 sentences conntaing happy words.
# There are 0 sentences conntaing sad words.
#
####


# จำนวนประโยคอาจมีการเปลี่ยนแปลง และคำบางคำอาจจะสะกดผิด (ห้ามแก้ไข)
sentences = ["I feel so happi when I spend time with my frends",
             "The sadness I feel when I think of you is unbearable",
             "Happyness is all around us, if we choose to see it",
             "I am SO SAD, I don't know how to go on",
             "I am smiling :)",
             "The saddest part about leaving is knowing I won't see you for a while",
             "I AM NOT HAPPY!",
             "I'm feeling sad today, but I know tomorrow will be better",
             "The happiness I feel when I'm with you is indescribable",
             "I cannot stop crying."
             ]

# คำที่สื่อถึงความสุข ลิสต์ของคำอาจมีการเปลี่ยนแปลง (ห้ามแก้ไข)
happy_words = ['happy', 'happi', 'happiness', 'happyness',
               'hapy', 'hapi', 'hapyness', 'hapiness', 'happynes', 'happines']

# คำที่สื่อถึงความเศร้า ลิสต์ของคำอาจมีการเปลี่ยนแปลง (ห้ามแก้ไข)
sad_words = ['sad', 'sadness', 'sadnes']

happy_count = 0
sad_count = 0

"""ใส่ code ของคุณที่นี่"""

for sentence in sentences:
    if any(word in sentence.lower() for word in happy_words):
        happy_count += 1
    elif any(word in sentence.lower() for word in sad_words):
        sad_count += 1
        


""" จบ code ของคุณที่นี่ """



print(f"There are {happy_count} sentences conntaing happy words.")
print(f"There are {sad_count} sentences conntaing sad words.")
