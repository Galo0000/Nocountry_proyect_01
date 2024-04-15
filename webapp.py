import streamlit as st
import base64

# Función para mostrar el dashboard de Power BI
def show_powerbi_dashboard():
    # URL del dashboard de Power BI (reemplaza con tu propio URL)
    powerbi_url = "https://datastudio.google.com/embed/reporting/1uYIXuUFbGwMA8Y8R2JFenPNG3fjuCaGG/page/mpeW"

    # Mostrar el dashboard de Power BI utilizando un iframe
    st.components.iframe(powerbi_url, height=600)

def get_base64(file_path):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    return encoded_string

def set_background(png_file, opacity):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        opacity: {opacity};
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Definir las rutas de las imágenes de fondo y la opacidad
background_image_path = "hosp.jpg"
background_opacity = 0.8

# Establecer el fondo de la página
set_background(background_image_path, background_opacity)

# Barra lateral con opciones de página y idioma
selected_language = st.sidebar.selectbox("Seleccionar Idioma", ("Español", "Inglés"))

# Mostrar el contenido correspondiente al idioma seleccionado
if selected_language == "Español":
    if st.sidebar.button("Portada"):
        st.title("Bienvenido a la Portada")
        st.write("Aquí puedes encontrar información general.")

    if st.sidebar.button("Dashboard"):
        st.title("Dashboard")
        st.write("Aquí puedes ver datos y visualizaciones.")

        # Mostrar el dashboard de Power BI al hacer clic en "Dashboard"
        show_powerbi_dashboard()

    if st.sidebar.button("Predictor"):
        st.title("Predictor")
        st.write("Aquí puedes usar el predictor.")

        # Mostrar cajas de texto para ingresar texto
        st.header("Ingresa la información requerida:")
        input1 = st.text_input("Ingrese texto 1:")
        input2 = st.text_input("Ingrese texto 2:")
        input3 = st.text_input("Ingrese texto 3:")

        # Agregar botón para procesar la entrada
        if st.button("Procesar Entrada"):
            # Aquí puedes realizar la lógica de procesamiento basada en la entrada de texto
            st.write(f"Texto 1: {input1}")
            st.write(f"Texto 2: {input2}")
            st.write(f"Texto 3: {input3}")

    if st.sidebar.button("Contacto"):
        st.title("Contacto")
        st.write("Aquí puedes encontrar información de contacto.")

elif selected_language == "Inglés":
    if st.sidebar.button("Home"):
        st.title("Welcome to the Home Page")
        st.write("Here you can find general information.")

    if st.sidebar.button("Dashboard"):
        st.title("Dashboard")
        st.write("Here you can view data and visualizations.")

        # Mostrar el dashboard de Power BI al hacer clic en "Dashboard"
        show_powerbi_dashboard()

    if st.sidebar.button("Predictor"):
        st.title("Predictor")
        st.write("Here you can use the predictor.")

        # Mostrar cajas de texto para ingresar texto
        st.header("Enter Required Information:")
        input1 = st.text_input("Enter text 1:")
        input2 = st.text_input("Enter text 2:")
        input3 = st.text_input("Enter text 3:")

        # Agregar botón para procesar la entrada
        if st.button("Process Input"):
            # Aquí puedes realizar la lógica de procesamiento basada en la entrada de texto
            st.write(f"Text 1: {input1}")
            st.write(f"Text 2: {input2}")
            st.write(f"Text 3: {input3}")

    if st.sidebar.button("Contact"):
        st.title("Contact")
        st.write("Here you can find contact information.")

