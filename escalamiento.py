import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy import interpolate

class EscalamientoImagen:
    def __init__(self, imagen_path):
        self.imagen = Image.open(imagen_path)
        self.matriz_original = np.array(self.imagen)
        
    def escalar_manual(self, sx, sy, metodo='vecino_mas_cercano'):
        """Escalamiento manual usando álgebra lineal"""
        h, w = self.matriz_original.shape[:2]
        nuevo_h, nuevo_w = int(h * sy), int(w * sx)
        
        # Crear matriz resultante
        if len(self.matriz_original.shape) == 3:  # RGB
            imagen_escalada = np.zeros((nuevo_h, nuevo_w, 3), dtype=np.uint8)
        else:  # Escala de grises
            imagen_escalada = np.zeros((nuevo_h, nuevo_w), dtype=np.uint8)
        
        # Aplicar transformación inversa
        for y_nuevo in range(nuevo_h):
            for x_nuevo in range(nuevo_w):
                # Transformación inversa
                x_original = int(x_nuevo / sx)
                y_original = int(y_nuevo / sy)
                
                # Asegurar que esté dentro de los límites
                if 0 <= x_original < w and 0 <= y_original < h:
                    imagen_escalada[y_nuevo, x_nuevo] = self.matriz_original[y_original, x_original]
        
        return Image.fromarray(imagen_escalada)
    
    def escalar_interpolacion_bilineal(self, sx, sy):
        """Escalamiento con interpolación bilineal (más suave)"""
        h, w = self.matriz_original.shape[:2]
        nuevo_h, nuevo_w = int(h * sy), int(w * sx)
        
        # Crear coordenadas de la nueva imagen
        x_nuevo = np.linspace(0, w-1, nuevo_w)
        y_nuevo = np.linspace(0, h-1, nuevo_h)
        
        # Interpolación bilineal
        if len(self.matriz_original.shape) == 3:
            imagen_escalada = np.zeros((nuevo_h, nuevo_w, 3))
            for canal in range(3):
                f = interpolate.interp2d(np.arange(w), np.arange(h), 
                                       self.matriz_original[:,:,canal], kind='linear')
                imagen_escalada[:,:,canal] = f(x_nuevo, y_nuevo)
        else:
            f = interpolate.interp2d(np.arange(w), np.arange(h), 
                                   self.matriz_original, kind='linear')
            imagen_escalada = f(x_nuevo, y_nuevo)
        
        return Image.fromarray(imagen_escalada.astype(np.uint8))
    
    def analizar_propiedades(self, sx, sy):
        """Análisis matemático de la transformación"""
        print("=== ANÁLISIS MATEMÁTICO DEL ESCALAMIENTO ===")
        print(f"Factores de escala: sx={sx}, sy={sy}")
        print(f"Determinante (cambio de área): {sx * sy}")
        print(f"¿Transformación ortogonal? {sx == sy}")
        print(f"¿Transformación lineal? Sí (cumple T(u+v) = T(u) + T(v))")
        
        # Matriz de transformación
        M = np.array([[sx, 0], [0, sy]])
        print(f"\nMatriz de transformación:\n{M}")
        print(f"Autovalores: {np.linalg.eigvals(M)}")
        
        return M
    
    def demostracion_visual(self, sx, sy):
        """Demostración visual de la transformación"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Mostrar imagen original
        axes[0].imshow(self.matriz_original)
        axes[0].set_title('Imagen Original')
        axes[0].axis('off')
        
        # Mostrar imagen escalada
        img_escalada = self.escalar_manual(sx, sy)
        axes[1].imshow(np.array(img_escalada))
        axes[1].set_title(f'Imagen Escalada (sx={sx}, sy={sy})')
        axes[1].axis('off')
        
        plt.tight_layout()
        plt.show()
        
        return img_escalada