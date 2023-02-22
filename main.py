from PIL import Image #Para cargar las imagenes
from PIL import ImageDraw #para dibujar
from PIL import ImageOps #Reescalado
from PIL import ImageFont #Fuentes
dir_rec = "./recursos/" #carpeta de recursos
dir_pro = "./productos/" #carpeta de productos

def producto(ruta, nombre, precio):
    #Crea una imagen del producto con su precio...
    print(f"Procesando: {nombre}")

    #Background
    image = Image.open(dir_rec + "background.png")
    draw = ImageDraw.Draw(image)


    #Producto
    pd = Image.open(ruta)
    #Rescalado de la imagen del producto
    #resize = pd.resize((850,430), Image.LANCZOS)
    pd = ImageOps.contain(pd, (950, 500), Image.LANCZOS)

    #centramos el producto
    ancho, alto = pd.size
    if nombre == "Xbox One":
        image.paste(pd, (950//2-ancho//2+60, 500//2-ancho//2+350), pd)
    else:
        image.paste(pd, (950// 2 - ancho // 2 + 60, 500 // 2 - ancho // 2 + 500), pd)

    #Escribimos precio y titulo #500, 900
    fuente = ImageFont.truetype(dir_rec + "Blues Smile.ttf", size=100, encoding="UTF-8")
    precio = precio + " Gs"
    ancho, alto = draw.textsize(precio, font=fuente)
    draw.text((550-ancho//2, 900-alto//2), precio, font=fuente, fill= "black") #fill = (0,0,0) para pintar RGB color
    #Titulo
    titulo = nombre + " Nueva!"
    fuente = ImageFont.truetype(dir_rec + "Blues Smile.ttf", size=70, encoding="UTF-8")
    ancho, alto = draw.textsize(precio, font=fuente)
    if nombre == "Xbox One":
        draw.text((450-ancho//2, 120-alto//2), titulo, font=fuente, fill="black")
    else:
        draw.text((380 - ancho // 2, 120 - alto // 2), titulo, font=fuente, fill="black")
    #guardamos la imagen del producto
    image.save(f"{nombre}.jpg")
    print("Success")
    return 0

if __name__ == "__main__":
    #Datos del producto
    titulo = "Playstation 4"
    dir_im = dir_pro + "PS4.png"
    precio = "1.500.000"

    titulo2 = "Xbox One"
    dir_im2 = dir_pro + "XBOX.png"
    precio2 = "1.200.000"

    #Llamamos la funcion
    producto(dir_im2, titulo2, precio2)