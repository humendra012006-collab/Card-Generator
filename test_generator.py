from PIL import Image, ImageOps
from PIL import ImageDraw, ImageFont

template = Image.open(r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Card template\ID_Card02.png")
draw = ImageDraw.Draw(template)
font = ImageFont.truetype("arial.ttf", 24)


def draw_text(x,y,content):
    print(f"-->DT-->{content}")
    draw.text(
        (x, y),
        f"{content}",
        fill="black",
        font=font
    )
def content_writer(x,y,content_text):
    print(f"##CW###{content_text}")
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

content_writer(520,240,"Rahul shingh")
content_writer(520,290,"Ankit kumar sharma")
content_writer(520,342,"8989898989")
content_writer(520,393,"House no 53 Laksmi Nagar Mangodi Walo ki potato Bagichi Brahampuri testing sample card jaipur")

photo_path = r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Photos\20.jpg"
photo = Image.open(photo_path)
photo = ImageOps.fit(photo, (236,278))
template.paste(photo,(57,116))


template.save("test.png")

print("COMPLETED")