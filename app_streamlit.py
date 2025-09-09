import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from escalamiento import EscalamientoImagen

def main():
    st.set_page_config(page_title="Escalamiento de Imágenes", layout="wide")
    
    st.title("🔍 Escalamiento de Imágenes - Álgebra Lineal")
    st.markdown("### Transformaciones lineales aplicadas al procesamiento de imágenes")
    
    # Subir imagen
    uploaded_file = st.file_uploader("Sube una imagen", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        try:
            # Crear instancia del escalador
            escalador = EscalamientoImagen(uploaded_file)
            
            st.success("✅ Imagen cargada exitosamente!")
            
            # Mostrar información de la imagen
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Ancho original", escalador.matriz_original.shape[1])
            with col2:
                st.metric("Alto original", escalador.matriz_original.shape[0])
            with col3:
                st.metric("Canales", escalador.matriz_original.shape[2] if len(escalador.matriz_original.shape) == 3 else 1)
            
            # Controles de escalamiento
            st.subheader("🎚️ Configuración de Escalamiento")
            col1, col2 = st.columns(2)
            with col1:
                sx = st.slider("Factor de escala X", 0.1, 5.0, 1.0, 0.1, 
                              help="Factor de escalamiento en el eje horizontal")
            with col2:
                sy = st.slider("Factor de escala Y", 0.1, 5.0, 1.0, 0.1,
                              help="Factor de escalamiento en el eje vertical")
            
            metodo = st.selectbox("Método de interpolación", 
                                ['Vecino más cercano', 'Interpolación bilineal'],
                                help="Vecino más cercano: más rápido. Bilineal: mejor calidad")
            
            # Aplicar escalamiento
            if st.button("🔄 Aplicar Escalamiento", type="primary"):
                with st.spinner("Procesando imagen..."):
                    if metodo == 'Vecino más cercano':
                        imagen_escalada = escalador.escalar_manual(sx, sy)
                    else:
                        imagen_escalada = escalador.escalar_interpolacion_bilineal(sx, sy)
                
                # Mostrar resultados
                st.subheader("📊 Resultados")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.image(escalador.imagen, 
                            caption=f"Original: {escalador.matriz_original.shape[1]}×{escalador.matriz_original.shape[0]}",
                            use_column_width=True)
                
                with col2:
                    nuevo_tamano = imagen_escalada.size
                    st.image(imagen_escalada, 
                            caption=f"Escalada: {nuevo_tamano[0]}×{nuevo_tamano[1]} (sx={sx}, sy={sy})",
                            use_column_width=True)
                
                # Análisis matemático
                if st.expander("📈 Ver Análisis Matemático"):
                    M = escalador.analizar_propiedades(sx, sy)
                    
                    st.write("**Matriz de Transformación:**")
                    st.latex(fr"""M = \begin{{bmatrix}} {sx} & 0 \\ 0 & {sy} \end{{bmatrix}}""")
                    
                    st.write("**Propiedades:**")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Determinante", f"{sx * sy:.2f}")
                    with col2:
                        st.metric("¿Ortogonal?", "Sí" if sx == sy else "No")
                    with col3:
                        st.metric("Cambio de área", f"×{sx * sy:.1f}")
                
                # Visualización de la transformación
                if st.expander("🎨 Visualización de la Transformación"):
                    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
                    
                    # Cuadrado unitario original
                    square = np.array([[0,0], [1,0], [1,1], [0,1], [0,0]])
                    ax[0].plot(square[:,0], square[:,1], 'b-', linewidth=3)
                    ax[0].set_title('Cuadrado Unitario Original')
                    ax[0].set_xlim(-0.5, max(sx, sy)+0.5)
                    ax[0].set_ylim(-0.5, max(sx, sy)+0.5)
                    ax[0].grid(True, alpha=0.3)
                    ax[0].set_aspect('equal')
                    
                    # Cuadrado transformado
                    M = np.array([[sx, 0], [0, sy]])
                    square_transformed = square @ M.T
                    ax[1].plot(square_transformed[:,0], square_transformed[:,1], 'r-', linewidth=3)
                    ax[1].set_title(f'Transformado (sx={sx}, sy={sy})')
                    ax[1].set_xlim(-0.5, max(sx, sy)+0.5)
                    ax[1].set_ylim(-0.5, max(sx, sy)+0.5)
                    ax[1].grid(True, alpha=0.3)
                    ax[1].set_aspect('equal')
                    
                    st.pyplot(fig)
        
        except Exception as e:
            st.error(f"Error al procesar la imagen: {str(e)}")
    
    else:
        st.info("👆 Por favor, sube una imagen para comenzar")
        st.markdown("""
        ### 📝 Instrucciones:
        1. Sube una imagen usando el botón arriba
        2. Ajusta los factores de escala X e Y
        3. Selecciona el método de interpolación
        4. Haz clic en 'Aplicar Escalamiento'
        5. Explora el análisis matemático
        """)

if __name__ == "__main__":
    main()