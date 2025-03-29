from fastapi import FastAPI
from routes.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from routes.routes import router
from pydantic import BaseModel
import joblib

app=FastAPI()
app.mount("/statics", StaticFiles(directory="statics"), name="statics")

app.include_router(router)

clf = joblib.load(r'modelo_emergencias.pkl')
vectorizer = joblib.load(r'vectorizador_tfidf.pkl')
analyzer = joblib.load(r'sentiment_analyzer.pkl')

class Llamada(BaseModel):
    texto_llamada: str

@app.post("/procesar_llamada/")
async def procesar_llamada(llamada: Llamada):
    texto_llamada = llamada.texto_llamada

    X_tfidf = vectorizer.transform([texto_llamada])

    tipo_emergencia = clf.predict(X_tfidf)[0]
    sentimiento = analyzer.polarity_scores(texto_llamada)
    sentimiento_llamada = "Broma" if sentimiento['pos'] < 0 else "Real"

    return {
        "tipo_emergencia": tipo_emergencia,
        "sentimiento_llamada": sentimiento_llamada
    }


