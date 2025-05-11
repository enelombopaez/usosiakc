# 🤖 CII AutoResponder – Asistente de Devoluciones Inteligente

Este proyecto automatiza el análisis y gestión de correos electrónicos relacionados con devoluciones de productos en **Componentes Intergalácticos Industriales S.A.** (CII), utilizando inteligencia artificial para mejorar la eficiencia y la calidad del servicio al cliente.

---

## 🚀 ¿Qué hace?

- Extrae información clave de correos electrónicos recibidos.
- Clasifica automáticamente las solicitudes según las políticas internas.
- Genera una respuesta educada y formal personalizada.
- Registra los casos tratados en un archivo CSV para seguimiento.

---

## 🔄 Flujo de trabajo

1. **Entrada del correo del cliente**  
   Se proporciona el texto completo del correo recibido.

2. **Análisis automatizado con IA**  
   El sistema extrae:
   - Número de pedido  
   - Nombre y correo del cliente  
   - Motivo de la solicitud  
   - Resultado de evaluación (ACEPTAR, RECHAZAR, REQUIERE REVISIÓN)

3. **Generación de respuesta**  
   Se elabora un mensaje de respuesta personalizado y firmado automáticamente por el agente responsable.

4. **Registro del caso**  
   Los datos analizados se guardan en un archivo CSV (`casos.csv`) con marca temporal para trazabilidad.

---

## 🧠 Motor IA

Este sistema está impulsado por **GPT-4**, proporcionando análisis de texto avanzado y generación contextual de lenguaje natural adaptada al dominio de atención al cliente.

---

## 🛠️ Requisitos

- Python 3.8+
- openai (versión >= 1.0.0)

Instalación rápida:

```bash
pip install openai
```

## Código incluido

El archivo cii_autoresponder.py contiene las funciones necesarias para:

Analizar el correo recibido.

Generar la respuesta.

Guardar los datos en CSV.

Firmar automáticamente la respuesta con el nombre del agente ("Nelson Lombo").

## Posibles mejoras

- Integración con servicios de correo electrónico (Gmail, Outlook).

- Conexión a base de datos de pedidos para validación automática.

- Interfaz web para revisión y control de respuestas.

- Compatibilidad multilingüe.

- Añadir memoria de interacciones previas por cliente.

- Incorporar flujos más complejos con herramientas como LangChain.

## Estructura del proyecto

```bash
cii_autoresponder.py    # Script principal
casos.csv               # Registro de resultados de análisis
README.md               # Este archivo con la explicación del proyecto
```

## Autor

Nelson Lombo 