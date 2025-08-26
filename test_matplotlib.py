import matplotlib
matplotlib.use("TkAgg")  # Forzar ventana emergente (puedes cambiar por "Qt5Agg")

import matplotlib.pyplot as plt
import numpy as np

# Crear una imagen 100x100 con solo el canal rojo
img = np.zeros((100, 100, 3))
img[:, :, 0] = 1  # Canal rojo en 1

plt.imshow(img)
plt.title("Prueba Ventana Matplotlib")
plt.axis("off")

plt.show()
