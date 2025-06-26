import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_completion(message: str) -> str:
    """Genera una respuesta usando la API de OpenAI."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message["content"].strip()


def analyze_conversation(text: str) -> str:
    """Eval\u00faa el tono de la conversaci\u00f3n."""
    prompt = (
        "Califica el siguiente texto del 1 al 5 segun su tono positivo:\n" + text
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"].strip()
