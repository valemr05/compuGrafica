import matplotlib
matplotlib.use("TkAgg")  # Asegura ventana emergente

import matplotlib.pyplot as plt
import numpy as np
from skimage import io

# Cargar imágenes
Imagen1 = io.imread("C:/Users/valer/Downloads/compuGrafica/img/Imagen1.jpg") / 255.0
Imagen2 = io.imread("C:/Users/valer/Downloads/compuGrafica/img/Imagen2.jpg") / 255.0

# Fusion
Factor = 0.4
SumaImg = Imagen1 * Factor + Imagen2 * (1 - Factor)

# Invertida
ImgInvertida = 1 - Imagen1

# Canales
ImgRed = np.copy(Imagen2)
ImgRed[:,:,1] = 0
ImgRed[:,:,2] = 0

ImgGreen = np.copy(Imagen2)
ImgGreen[:,:,0] = 0
ImgGreen[:,:,2] = 0

ImgBlue = np.copy(Imagen2)
ImgBlue[:,:,0] = 0
ImgBlue[:,:,1] = 0

# Mostrar todas las imágenes en una sola ventana
plt.figure(figsize=(12, 8))

plt.subplot(2,3,1)
plt.imshow(Imagen1)
plt.title("Imagen1")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(SumaImg)
plt.title("Fusion Imagen1 + Imagen2")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(ImgInvertida)
plt.title("Imagen1 Invertida")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(ImgRed)
plt.title("Imagen2 Rojo")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(ImgGreen)
plt.title("Imagen2 Verde")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(ImgBlue)
plt.title("Imagen2 Azul")
plt.axis("off")

plt.tight_layout()
plt.show()