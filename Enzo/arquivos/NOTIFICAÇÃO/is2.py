import feedparser
from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE_AQUI")

# 1. Buscar notícias do G1
feed = feedparser.parse("https://g1.globo.com/rss/g1/")

noticias = []
for entry in feed.entries[:5]:
    noticias.append(f"Título: {entry.title}\nResumo: {entry.summary}")

contexto_g1 = "\n\n".join(noticias)

# 2. Sua pergunta
pergunta = "O que está acontecendo no Brasil recentemente?"

# 3. Mandar tudo para o modelo
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente que responde usando apenas as notícias fornecidas do G1."
        },
        {
            "role": "user",
            "content": f"""
Notícias do G1:
{contexto_g1}

Pergunta:
{pergunta}
"""
        }
    ]
)

print(response.choices[0].message.content)