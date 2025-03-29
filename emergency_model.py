import joblib

clf = joblib.load(r'modelo_emergencias.pkl')
vectorizer = joblib.load(r'vectorizador_tfidf.pkl')
analyzer = joblib.load(r'sentiment_analyzer.pkl')
preprocess = joblib.load(r'preprocess_function.pkl')

def procesar_llamada(texto_llamada):
    texto_limpio = preprocess(texto_llamada)
  
    # Transformar el texto limpio usando el vectorizador TF-IDF
    X_tfidf = vectorizer.transform([texto_limpio])

    # Predecir el tipo de emergencia
    tipo_emergencia = clf.predict(X_tfidf)[0]

    # Analizar Patrones de estado emocional en la llamada
    sentimiento = analyzer.polarity_scores(texto_llamada)
    sentimiento_llamada = "Broma" if sentimiento['pos'] < 0 else "Real"

    return tipo_emergencia, sentimiento_llamada

if __name__ == "__main__":
    ejemplo_texto = "Hay un incendio en mi casa, necesitamos ayuda urgente."
    resultado = procesar_llamada(ejemplo_texto)
    print(f"Tipo de emergencia: {resultado[0]} - Llamada: {resultado[1]}")
