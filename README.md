# Bot de WhatsApp con OpenAI

Este proyecto contiene una configuraci\u00f3n inicial para crear un bot de WhatsApp que use la API de OpenAI para responder mensajes. Incluye un dashboard web sencillo donde se almacenan las conversaciones.

## Requisitos

- Python 3.8+
- Definir la variable de entorno `OPENAI_API_KEY` con tu clave de OpenAI.

## Uso

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el servidor:
   ```bash
   python app.py
   ```
3. Env\u00eda mensajes POST a `/webhook` con el formato `{ "from": "usuario", "message": "hola" }`.
4. Visita `http://localhost:3000/dashboard` para ver las conversaciones almacenadas.

Este c\u00f3digo es una base que se puede ampliar con la integraci\u00f3n real de la API de WhatsApp y un an\u00e1lisis m\u00e1s completo de las conversaciones.
