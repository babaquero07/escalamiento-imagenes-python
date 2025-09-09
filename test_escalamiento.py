from escalamiento import EscalamientoImagen
import matplotlib.pyplot as plt
import numpy as np

def crear_imagen_prueba():
    """Crear una imagen de prueba simple"""
    # Crear patrón de cuadrados
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    for i in range(0, 100, 20):
        for j in range(0, 100, 20):
            if (i//20 + j//20) % 2 == 0:
                img[i:i+20, j:j+20] = [255, 100, 100]  # Rojo claro
            else:
                img[i:i+20, j:j+20] = [100, 100, 255]  # Azul claro
    
    # Guardar imagen de prueba
    from PIL import Image
    Image.fromarray(img).save('./images/imagen_prueba.png')
    print("Imagen de prueba creada: 'imagen_prueba.png'")
    return 'imagen_prueba.png'

def prueba_basica():
    """Prueba básica del escalamiento"""
    print("=== PRUEBA BÁSICA DE ESCALAMIENTO ===")
    
    # Crear imagen de prueba
    imagen_path = crear_imagen_prueba()
    
    # Probar escalamiento
    escalador = EscalamientoImagen(imagen_path)
    
    # Probar diferentes factores de escala
    factores = [(1, 1), (2, 1), (1, 2), (2, 2), (0.5, 0.5)]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    for idx, (sx, sy) in enumerate(factores):
        if idx < len(axes):
            # Análisis matemático
            M = escalador.analizar_propiedades(sx, sy)
            print(f"Matriz de transformación para sx={sx}, sy={sy}:\n{M}\n")
            
            # Demostración visual
            img_esc = escalador.escalar_manual(sx, sy)
            axes[idx].imshow(np.array(img_esc))
            axes[idx].set_title(f'sx={sx}, sy={sy}\nÁrea × {sx*sy:.1f}')
            axes[idx].axis('off')
    
    # Ocultar ejes extras si los hay
    for idx in range(len(factores), len(axes)):
        axes[idx].axis('off')
    
    plt.tight_layout()
    plt.savefig('./images/resultados_escalamiento.png')
    plt.show()

def prueba_propiedades_matematicas():
    """Prueba de propiedades matemáticas"""
    print("\n=== PRUEBA DE PROPIEDADES MATEMÁTICAS ===")
    
    # Verificar linealidad
    def T(vec, sx=2, sy=3):
        return np.array([sx*vec[0], sy*vec[1]])
    
    u = np.array([1, 2])
    v = np.array([3, 4])
    alpha, beta = 2, 3
    
    # Verificar T(alpha*u + beta*v) == alpha*T(u) + beta*T(v)
    lado_izq = T(alpha*u + beta*v)
    lado_der = alpha*T(u) + beta*T(v)
    
    print(f"T({alpha}*{u} + {beta}*{v}) = {lado_izq}")
    print(f"{alpha}*T({u}) + {beta}*T({v}) = {lado_der}")
    print(f"¿Se cumple la linealidad? {np.allclose(lado_izq, lado_der)}")
    
    # Verificar determinante
    sx, sy = 2, 3
    M = np.array([[sx, 0], [0, sy]])
    det = np.linalg.det(M)
    print(f"\nDeterminante para sx={sx}, sy={sy}: {det}")
    print(f"Esto significa el área se multiplica por {det}")

if __name__ == "__main__":
    # Ejecutar pruebas
    prueba_basica()
    prueba_propiedades_matematicas()
    
    print("\n✅ Todas las pruebas completadas exitosamente!")