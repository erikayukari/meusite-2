import csv
import pandas as pd
from GoogleNews import GoogleNews
from flask import Flask 

def noticias():
    googlenews.set_lang('pt-br')
    googlenews.get_news("Mogi das Cruzes")
    resultado = googlenews.result()
    df = pd.DataFrame(resultado)
    return df

app = Flask(__name__)
@app.route("/")
def hello_word():
    return """<h1>Olá mundo!</h1> 
    <p><b>Esse é meu primeiro site</b>!</p>
    <a href="/sobre">Sobre esse site</a>
    <a href="/raspador_noticias">Raspador de Notícias</a>
    """

@app.route("/sobre")
def sobre():
    return """<h1>Sobre</h1> 
    
    <a href="/">Página inicial</a>
    
    <p> Esse site foi criado por <b>Jamile Santana </b>.</p>"""

@app.route("/raspador_noticias")
def raspador_noticias():
    noticias_mogi = noticias()
    return f"""<h1>Raspador de notícias</h1> 
    
    <a href="/">Página inicial</a>
    <a href="/sobre">Sobre esse site</a>
    
    <p> Notícias de destaque em Mogi:{noticias_mogi["link"]} </b>.</p>""" 



