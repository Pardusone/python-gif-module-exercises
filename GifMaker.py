from PIL import Image, ImageDraw

def create_frame(x, y, size):
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((x, y, x + size, y + size), fill="black")
    return image

def main():
    # Basit bir kare oluştur ve kaydet
    image = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((100, 100, 150, 150), fill="black")
    image.save("my_square_image.png")

    # Kareleri oluşturacak fonksiyon
    frames = []
    x, y = 50, 50  # Kare için başlangıç konumları
    size = 50      # Kare başlangıç boyutu

    # Kareleri oluştur ve listeye ekle
    for i in range(20):
        frames.append(create_frame(x, y, size))
        x += 10  # X koordinatını değiştir (hareket ettir)
        y += 10  # Y koordinatını değiştir (hareket ettir)
        size += 5  # Kare boyutunu değiştir


    frame_one = frames[0]
    frame_one.save("cicle.gif",format = "GIF",append_images =frames,save_all = True,duration = 100,loop = 0)

