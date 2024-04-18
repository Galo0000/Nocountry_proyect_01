import streamlit as st
import base64

content = {
        "Español": {
            "Home": {"button":"Portada","title": "", "text": "DiabeRisk combina salud y tecnología para abordar el problema de los reingresos hospitalarios de pacientes diabéticos. Al utilizar el aprendizaje automático en los datos de los pacientes, podemos predecir los reingresos en función de factores clínicos y demográficos. Además, los datos se analizaron con Power BI para identificar tendencias e influencias clave. Nuestro objetivo es mejorar el control de la diabetes y la calidad de vida del paciente reduciendo los reingresos hospitalarios."
                                                                            ,"text1": """
DiabeRisk permite al usuario:

- Predice la probabilidad de que los pacientes diabéticos necesiten ser readmitidos en el hospital, lo que ayuda en la atención preventiva.
- Proporciona a los profesionales de la salud información basada en datos para mejores estrategias de gestión de pacientes.
- Ayuda en la planificación y asignación de recursos dentro de los centros de atención médica al pronosticar las tasas de reingreso de pacientes.
"""},
            "Dashboard": {"button":"Panel","title": "Panel", "text": "Aquí puedes ver datos y visualizaciones."},
            "Predictor": {"button":"Predictor","title": "Predictor", "text": "Aquí puedes usar el predictor."},
            "Contacts": {"button":"Contactos","title": "Contactos", "text": "Aquí puedes encontrar información de contacto."}
        },
        "English": {
            "Home": {"button":"Front Page","title": "", "text": "DiabeRisk combines health and technology to tackle the issue of hospital readmissions in diabetic patients. By using machine learning on patient data we can predict readmissions based on clinical and demographic factors. Additionally, data was analyzed with Power BI to identify key trends and influences. Our goal is to improve diabetes management and patient quality of life by reducing hospital readmissions.",
                                                                                    "text1":"""
DiabeRisk allows the user to:

- Predicts the likelihood of diabetic patients needing to be readmitted to the hospital, aiding in preventive care.
- Provides healthcare professionals with data-driven insights for better patient management strategies.
- Helps in resource planning and allocation within healthcare facilities by forecasting patient readmission rates.
""" },
            "Dashboard": {"button":"Dashboard","title": "Dashboard", "text": "Here you can view data and visualizations."},
            "Predictor": {"button":"Predictor","title": "Predictor", "text": "Here you can use the predictor."},
            "Contacts": {"button":"Contacts","title": "Contacts", "text": "Here you can find contact information."}
                }
    }

contacts = {"guille":{"name":"Guillermo Gallo Garcia",
                    "rol":"Data Science",
                    "linkedin":"https://www.linkedin.com/in/guillermo-patricio-gallo-garcia-0a3bb3bb/",
                    "github":"https://github.com/Galo0000"},
            "adrian":{"name":"Adrian Della Valentina",
                    "rol":"Data Science",
                    "linkedin":"https://www.linkedin.com/in/adrian-della-valentina/",
                    "github":"..."},
            "daniel":{"name":"Daniel Menendez Gomez",
                    "rol":"Data Analyst",
                    "linkedin":"https://www.linkedin.com/in/danielgomz/",
                    "github":"..."},
            "juan":{"name":"Juan Mendoza Lopez",
                    "rol":"ETL Developer",
                    "linkedin":"https://www.linkedin.com/in/guillermo-patricio-gallo-garcia-0a3bb3bb/",
                    "github":"..."},
            "diego":{"name":"Diego Suárez",
                    "rol":"Analista BI",
                    "linkedin":"https://www.linkedin.com/in/diego-suarez-escobar/",
                    "github":"..."}}

def show_powerbi_dashboard():
    powerbi_url = "https://app.fabric.microsoft.com/view?r=eyJrIjoiNDA4ODk3MDAtYTVhZC00ZDUxLTk1ZWMtYTliYWZiOWZjZWNmIiwidCI6IjU0YTc3ZTU4LTliZjktNDc1OC05M2M3LTk0Y2ZkNmYwNTY3YSIsImMiOjZ9"
    st.write(f'<iframe src="{powerbi_url}" width="150%" height="600"></iframe>', unsafe_allow_html=True)

def set_background(png_file, opacity):
    with open(png_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    
    # Definir el estilo CSS para la imagen de fondo
    page_bg_img = f'''
    <style>
    body {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        opacity: {opacity};
    }}
    </style>
    '''

    # Aplicar el estilo CSS directamente al cuerpo (body) de la página
    st.markdown(page_bg_img, unsafe_allow_html=True)


def show_content(selected_language,button):
    
    selected_content = content[selected_language]

    if button == "Front Page" or button == "Portada":
        st.title(selected_content["Home"]["title"])
        # Cargar la imagen desde un archivo local
        image = open("diaberisk.png", "rb")  # Reemplaza con la ruta de tu imagen
        image_bytes = image.read()

        # Mostrar la imagen en Streamlit
        st.image(image_bytes, use_column_width=True)

        st.write(f'<span style="color: black; font-size: 20px; opacity: 1; font-weight: None;">{selected_content["Home"]["text"]}</span>',unsafe_allow_html=True)
        st.write(f'<span style="color: black; font-size: 20px; opacity: 1; font-weight: None;">{selected_content["Home"]["text1"]}</span>',unsafe_allow_html=True)

    elif button == "Dashboard" or button == "Panel":
        st.title(selected_content["Dashboard"]["title"])
        st.write(selected_content["Dashboard"]["text"])

        show_powerbi_dashboard()

    elif button == "Predictor" or button == "Predictor":
        st.title(selected_content["Predictor"]["title"])
        st.write(selected_content["Predictor"]["text"])
        
        # Primer selectbox para seleccionar el género
        genero = st.selectbox("Selecciona el género:", ["Hombre", "Mujer", "Desconocido"])

        # Segundo selectbox para seleccionar el medicamento
        medicamento = st.selectbox("Selecciona un medicamento:", ["Medicamento 1", "Medicamento 2", "Medicamento 3", "Medicamento 4"])

        # Botón para procesar los datos ingresados
        if st.button("Procesar"):
            if genero and medicamento:
                st.success(f"Has seleccionado:\nGénero: {genero}\nMedicamento: {medicamento}")
                # Aquí puedes agregar la lógica de procesamiento basada en las selecciones realizadas
        
        

    elif button == "Contacts" or button == "Contactos":
        st.title(selected_content["Contacts"]["title"])
        st.write(selected_content["Contacts"]["text"])

        for contact_key in contacts.keys():
            contact = contacts[contact_key]

            # Mostrar información del contacto en una tabla o columna
            st.write(f"**Nombre:** {contact['name']}")
            st.write(f"**Rol:** {contact['rol']}")
            st.write(f"**LinkedIn:** [{contact['linkedin']}]({contact['linkedin']})")
            st.write(f"**GitHub:** [{contact['github']}]({contact['github']})")

            # Separador entre contactos
            st.markdown("---")

st.write("inicio")
state = None
background_image_path = "hosp.jpg"
background_opacity = 0.8
set_background(background_image_path, background_opacity)
    
st.sidebar.title("Seleccionar idioma")
selected_language = st.sidebar.selectbox("", ("Español", "English"))

state = selected_language

buttons = [content[selected_language][key]["button"] for key in content[selected_language]]

if selected_language != state:
    for button in buttons:
        if st.sidebar.button(button):
                show_content(selected_language,button)
            
st.write("fin")
#if selected_language == "Dashboard":
#    show_powerbi_dashboard()

#if button == "Predictor" or button == "Predictor":
#    predictor()
