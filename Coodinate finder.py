import matplotlib.pyplot as plt
from PIL import Image

img = Image.open(r"C:\Users\humen\OneDrive\Desktop\Coding\ID Card Generator\Card template\ID_Card01.png")

fig, ax = plt.subplots()
ax.imshow(img)

def onclick(event):
    print(f"X={int(event.xdata)}, Y={int(event.ydata)}")

fig.canvas.mpl_connect("button_press_event", onclick)

plt.show()
