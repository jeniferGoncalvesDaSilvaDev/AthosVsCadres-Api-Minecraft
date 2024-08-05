from fastapi import FastAPI
import uvicorn
#estatisticas descritivas das performances de athos e cadres na batalha de construção 
app = FastAPI(title="Minecraft athos vs cadres")
#competição de athos e cadres de suas construção e notas dadas 
athos ={
  "casa":10.0,
  "sala":8.0,
  "robo-gigante":9.0,
  "pizza":7.0,
  "carro":10.0,
  "mobs":9.0,
  "jogos":8.0,
  "parque_diversao":7.0,
  "piscina":10.0
  
}
cadres={
  "casa":7.0,
  "sala":8.0,
  "robo-gigante":6.0,
  "pizza":2.0,
  "carro":6.0,
  "mobs":2.0,
  "jogos":5.0,
  "parque_diversao":3.0,
  "piscina":1.0
}
def media_athos():
  soma=0

  for value in athos.values():
    soma+=value
  media = soma/len(athos)
  return{"media":round(media,2)}
def media_cadres():
  soma=0

  for value in cadres.values():
    soma+=value
  media = soma/len(cadres)
  return{"media":round(media,2)}
def mediana_athos():
  med=0
  lista_athos=list(athos.values())
  lista_athos.sort()
  med=lista_athos[len(lista_athos)//2]
    
  
  return {"mediana":round(med,2)}
def mediana_cadres():
  med=0
  lista_cadres=list(cadres.values())
  lista_cadres.sort()
  med=lista_cadres[len(lista_cadres)//2]
  return {"mediana":round(med,2)}
  
  
  
  
@app.get("/")
def home():
  return {"servidor":"athos vs cadres"}

@app.get("/media")
def media():
  return {"athos":media_athos(),"cadres":media_cadres()}
@app.get("/mediana")
def mediana():
  return {"athos": mediana_athos(),"cadres": mediana_cadres()}
def variancia_athos():
  desvios=0
  dp=0
  for valor in athos.values():
        desvios += ((valor - media_athos()["media"]) ** 2)
  dp=desvios/len(athos)
  return {"desvio_padrao": round(dp**0.5,2)}
def variancia_cadres():
  desvios=0
  dp=0
  for valor in cadres.values():
        desvios += ((valor - media_cadres()["media"]) ** 2)
  dp=desvios/len(cadres)
  return {"desvio_padrao": round(dp**0.5,2)}

@app.get("/variancia")
def variancia():
  return{"athos": variancia_athos(),"cadres":variancia_cadres()}

uvicorn.run(app,host="0.0.0.0",port=8080)

