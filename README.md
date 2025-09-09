# 🔍 Escalamiento de Imágenes - Álgebra Lineal

Este proyecto implementa algoritmos de escalamiento de imágenes utilizando conceptos fundamentales de álgebra lineal, específicamente transformaciones lineales aplicadas al procesamiento digital de imágenes.

## 📋 Descripción del Proyecto

El proyecto consiste en una aplicación interactiva desarrollada con Streamlit que permite:

- **Cargar imágenes** en formatos PNG, JPG y JPEG
- **Aplicar transformaciones de escalamiento** usando matrices de transformación lineal
- **Visualizar resultados** con dos métodos de interpolación diferentes
- **Analizar propiedades matemáticas** de las transformaciones aplicadas
- **Demostrar conceptos de álgebra lineal** de forma visual e interactiva

### 🧮 Fundamentos Matemáticos

El escalamiento de imágenes se basa en la aplicación de una **matriz de transformación lineal**:

```
M = [sx  0 ]
    [0  sy]
```

Donde:

- `sx`: Factor de escalamiento en el eje X (horizontal)
- `sy`: Factor de escalamiento en el eje Y (vertical)

Esta transformación cumple con las propiedades de linealidad:

- `T(u + v) = T(u) + T(v)`
- `T(αu) = αT(u)`

## 🗂️ Estructura del Proyecto

```
Proyecto AL/
├── app_streamlit.py          # Aplicación web principal
├── escalamiento.py           # Clase principal con algoritmos de escalamiento
├── test_escalamiento.py      # Script de pruebas y demostraciones
├── requirements.txt          # Dependencias del proyecto
├── images/                   # Carpeta de imágenes
│   └── imagen_prueba.png    # Imagen de prueba generada automáticamente
└── README.md                # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd "Proyecto AL"
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Las dependencias incluyen:

- `numpy>=1.21.0` - Cálculos numéricos y matrices
- `pillow>=9.0.0` - Procesamiento de imágenes
- `matplotlib>=3.5.0` - Visualización y gráficos
- `streamlit>=1.12.0` - Framework para la aplicación web
- `scipy>=1.7.0` - Algoritmos científicos (interpolación)

## 🎮 Cómo Ejecutar la Aplicación

### Aplicación Web Interactiva

```bash
streamlit run app_streamlit.py
```

ó tambien con

```
python -m streamlit run app_streamlit.py
```

Esto abrirá automáticamente tu navegador web en `http://localhost:8501` con la interfaz interactiva.

### Script de Pruebas

```bash
python test_escalamiento.py
```

Este script ejecuta pruebas automáticas y genera visualizaciones de ejemplo.

## 🖥️ Uso de la Aplicación

### Interfaz Web (Streamlit)

1. **Cargar Imagen**: Usa el botón "Sube una imagen" para cargar tu archivo
2. **Configurar Escalamiento**:
   - Ajusta el factor de escala X (0.1 - 5.0)
   - Ajusta el factor de escala Y (0.1 - 5.0)
   - Selecciona el método de interpolación:
     - **Vecino más cercano**: Más rápido, resultado pixelado
     - **Interpolación bilineal**: Mejor calidad, más suave
3. **Aplicar Transformación**: Haz clic en "🔄 Aplicar Escalamiento"
4. **Explorar Resultados**:
   - Compara imagen original vs escalada
   - Ve el análisis matemático detallado
   - Visualiza la transformación geométrica

### Funcionalidades Avanzadas

- **📈 Análisis Matemático**: Muestra la matriz de transformación, determinante y propiedades
- **🎨 Visualización de Transformación**: Representa gráficamente cómo se transforma un cuadrado unitario
- **📊 Métricas**: Información sobre dimensiones, cambio de área y propiedades ortogonales

## 🔧 Componentes Técnicos

### `escalamiento.py`

Clase principal `EscalamientoImagen` con métodos:

- `escalar_manual(sx, sy)`: Implementación manual usando vecino más cercano
- `escalar_interpolacion_bilineal(sx, sy)`: Escalamiento con interpolación suave
- `analizar_propiedades(sx, sy)`: Análisis matemático de la transformación
- `demostracion_visual(sx, sy)`: Visualización comparativa

### `app_streamlit.py`

Interfaz web interactiva que incluye:

- Carga de archivos de imagen
- Controles deslizantes para factores de escala
- Selección de métodos de interpolación
- Visualización en tiempo real
- Análisis matemático expandible

### `test_escalamiento.py`

Script de pruebas que incluye:

- Generación automática de imagen de prueba
- Pruebas con diferentes factores de escala
- Verificación de propiedades matemáticas
- Visualización de resultados

## 📊 Métodos de Interpolación

### 1. Vecino Más Cercano

- **Ventajas**: Rápido, preserva valores originales exactos
- **Desventajas**: Resultado pixelado, especialmente al ampliar
- **Uso recomendado**: Imágenes con bordes definidos, escalamiento rápido

### 2. Interpolación Bilineal

- **Ventajas**: Resultado más suave, mejor calidad visual
- **Desventajas**: Más lento computacionalmente
- **Uso recomendado**: Fotografías, escalamiento de alta calidad

## 🧪 Ejemplos de Uso

### Ejemplo 1: Ampliación Uniforme

```python
escalador = EscalamientoImagen('mi_imagen.jpg')
imagen_escalada = escalador.escalar_manual(2.0, 2.0)  # Doble tamaño
```

### Ejemplo 2: Escalamiento No Uniforme

```python
imagen_escalada = escalador.escalar_manual(3.0, 0.5)  # Más ancho, menos alto
```

### Ejemplo 3: Reducción con Interpolación

```python
imagen_escalada = escalador.escalar_interpolacion_bilineal(0.5, 0.5)  # Mitad del tamaño
```

## 🎯 Conceptos de Álgebra Lineal Demostrados

1. **Transformaciones Lineales**: Aplicación de matrices a vectores de posición
2. **Determinante**: Interpretación como factor de cambio de área
3. **Linealidad**: Verificación de las propiedades fundamentales
4. **Transformaciones Ortogonales**: Cuando sx = sy (preserva ángulos)
5. **Autovalores**: Los factores de escala son los autovalores de la matriz

## 🚨 Limitaciones y Consideraciones

- **Memoria**: Imágenes muy grandes pueden consumir mucha RAM
- **Rendimiento**: La interpolación bilineal es más lenta para imágenes grandes
- **Calidad**: El escalamiento hacia arriba puede introducir artefactos
- **Formato**: Solo soporta imágenes RGB y escala de grises

## 📚 Referencias Teóricas

- Álgebra Lineal: Transformaciones matriciales
- Procesamiento Digital de Imágenes: Interpolación
- Análisis Numérico: Métodos de interpolación
- Geometría Analítica: Transformaciones en el plano

## 📄 Licencia

Este proyecto es de uso educativo y está disponible para fines académicos.

---

_Desarrollado como proyecto educativo para demostrar aplicaciones prácticas de álgebra lineal en procesamiento de imágenes._
