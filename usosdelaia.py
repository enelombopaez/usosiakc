from openai import OpenAI

# Instancia del cliente OpenAI
# Cosas a mejorar, se podría utilizar una variable de entorno aqui
client = OpenAI(api_key="Add here the key since I should not upload it to the git repo for security reason")  

# Paso 1: Análisis del correo
def analizar_correo(email_texto):
    prompt_analisis = f"""
Eres un asistente de atención al cliente de Componentes Intergalácticos Industriales S.A. 
Analiza el siguiente correo y responde en formato JSON con los siguientes campos:
- "número_pedido"
- "nombre_cliente"
- "email_cliente"
- "motivo"
- "resultado": ACEPTAR, RECHAZAR o REQUIERE REVISIÓN
- "razón"

Correo:
\"\"\"
{email_texto}
\"\"\"
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en atención al cliente y políticas de devoluciones."},
            {"role": "user", "content": prompt_analisis}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# Paso 2: Generar respuesta automática
def generar_respuesta(email_texto):
    prompt_respuesta = f"""
Eres un asistente de atención al cliente. Con base en el siguiente correo, genera una respuesta formal y educada 
según las políticas de Componentes Intergalácticos Industriales S.A.:
- Acepta solo si hay defecto de fabricación, error en suministro o producto incompleto de origen.
- Rechaza si los daños son por transporte no asegurado o mal uso.
- Si la información no es clara, pide más detalles.

Correo del cliente:
\"\"\"
{email_texto}
\"\"\"
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente profesional de atención al cliente."},
            {"role": "user", "content": prompt_respuesta}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

# === Ejemplo de uso ===
if __name__ == "__main__":
    email = """
Asunto: Solicitud de reemplazo por daños en transporte – Pedido #D347-STELLA
Estimado equipo de Componentes Intergalácticos Industriales S.A.,
Me pongo en contacto con ustedes como cliente reciente para comunicar una
incidencia relacionada con el pedido #D347-STELLA, correspondiente a un lote de
condensadores de fluzo modelo FX-88, destinados a un proyecto estratégico de gran
envergadura: la construcción de la Estrella de la Muerte.
Lamentablemente, al recibir el envío, observamos que varios de los condensadores
presentaban daños visibles y no funcionales. Tras revisar el estado del embalaje y
consultar con el piloto de carga, todo indica que la mercancía sufrió una caída
durante el transporte interestelar.
Adjunto imágenes del estado de los condensadores y el albarán de entrega sellado
por nuestro droide de recepción.
Atentamente,
Darth Márquez
Departamento de Ingeniería Imperial
Contacto: dmarquez@imperiumgalactic.net
"""

    print("🔍 Datos extraídos:\n")
    print(analizar_correo(email))

    print("\n✉️ Respuesta generada:\n")
    print(generar_respuesta(email))
