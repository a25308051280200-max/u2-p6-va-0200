import matplotlib.pyplot as plt 
import numpy as np 
# Alejandra Rivera Valenzuela NC = 0200

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

# Personalizar gráfica
plt.plot( cant_productos,precio,color="pink",marker="o",linestyle="dashed",linewidth=2, markersize=12)
plt.title(" Ventas de walmart 0200")
plt.xlabel("precios")
plt.ylabel("cant prod")
plt.show()

