import matplotlib
matplotlib.use("TkAgg")  # Asegura ventana emergente

import numpy as np

import matplotlib.pyplot as plt

def unir_4_imagenes(marco_color=(255, 255, 255), nombre_salida="resultado.jpg"):
    grosor = 20
    # Leer imágenes como numpy arrays
    img1 = plt.imread("C:\\Users\\valer\\Downloads\\Sexto semestre\\Computación Grafica\\imagen\\png\\barco.png")
    img2 = plt.imread("C:\\Users\\valer\\Downloads\\Sexto semestre\\Computación Grafica\\imagen\\png\\perro.png")
    img3 = plt.imread("C:\\Users\\valer\\Downloads\\Sexto semestre\\Computación Grafica\\imagen\\png\\mar.png")
    img4 = plt.imread("C:\\Users\\valer\\Downloads\\Sexto semestre\\Computación Grafica\\imagen\\png\\utp.png")

    # Asegurar que todas sean uint8 (0-255)
    if img1.dtype != np.uint8:
        img1 = (img1 * 255).astype(np.uint8)
        img2 = (img2 * 255).astype(np.uint8)
        img3 = (img3 * 255).astype(np.uint8)
        img4 = (img4 * 255).astype(np.uint8)

    # Ajustar a un mismo tamaño
    alto = min(img1.shape[0], img2.shape[0], img3.shape[0], img4.shape[0])
    ancho = min(img1.shape[1], img2.shape[1], img3.shape[1], img4.shape[1])

    def recortar(img):
        return img[:alto, :ancho, :3]  # solo RGB

    img1, img2, img3, img4 = recortar(img1), recortar(img2), recortar(img3), recortar(img4)

    # Crear marcos
    marco_v = np.full((alto, grosor, 3), marco_color, dtype=np.uint8)  # marco vertical
    marco_h = np.full((grosor, (ancho * 2 + grosor), 3), marco_color, dtype=np.uint8)  # marco horizontal

    # Construir filas
    fila1 = np.hstack((img1, marco_v, img2))
    fila2 = np.hstack((img3, marco_v, img4))

    # Unir todo con marco horizontal en medio
    imagen_final = np.vstack((fila1, marco_h, fila2))

    marco_externo = grosor
    h, w, _ = imagen_final.shape
    imagen_con_borde = np.full((h + 2*marco_externo, w + 2*marco_externo, 3), marco_color, dtype=np.uint8)
    imagen_con_borde[marco_externo:-marco_externo, marco_externo:-marco_externo] = imagen_final


    # Guardar imagen
    plt.imsave(nombre_salida, imagen_con_borde)

    return imagen_con_borde

resultado = unir_4_imagenes(
    marco_color=(125, 125, 0),  # verde
    nombre_salida="collage.jpg"
)

plt.imshow(resultado)
plt.axis("off")
plt.show()