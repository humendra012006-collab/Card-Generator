import pandas as pd
from PIL import Image, ImageOps
from PIL import ImageDraw, ImageFont


def draw_text(x,y,content):
    draw.text(
        (x, y),
        f"{content}",
        fill="black",
        font=font
    )
def content_writer(x,y,content_text):
    flag = True
    count = 0
    word_count = 0
    content_text = content_text.split()
    for word in content_text:
        word_count += 1
        if len(word) + count <= 25:
            count += len(word)
        else:
            flag = False
            draw_text(x,y," ".join(content_text[0:word_count]))
            content_writer(x,y+34," ".join(content_text[word_count:]))
            break
    if flag:
        draw_text(x, y," ".join(content_text))


students = pd.read_excel(r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Card data\Gurukul Institute.xlsx")

for _, student in students.iterrows():
    template = Image.open(r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Card template\ID_Card02.png")
    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype("arial.ttf", 24)

    content_writer(520,240,f"{student["Name"]}")
    content_writer(520,290,f"{student["Father"]}")
    content_writer(520,342,f"{student["Contact"]}")
    content_writer(520,393,f"{student["Address"]}")

    photo_path = rf"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Photos\{student["Roll"]}"
    try:
        photo = Image.open(photo_path + ".jpg")
    except:
        try:
            photo = Image.open(photo_path + ".jpeg")
        except:
            try:
                photo = Image.open(photo_path + ".png")
            except:
                photo = Image.open(r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Photos\Person.png")

    photo = ImageOps.fit(photo, (236,278))
    template.paste(photo,(57,116))

    template.save(rf"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Final_cards\{student["Roll"]}.png")

print("COMPLETED")