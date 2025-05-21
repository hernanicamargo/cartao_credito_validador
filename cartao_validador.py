from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Função para validar o número do cartão e identificar a bandeira
def validar_cartao(numero):
    bandeiras = {
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "enRoute": r"^(2014|2149)[0-9]{11}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699[0-9]{11}$",
        "HiperCard": r"^(606282|3841)[0-9]{10,13}$",
        "Aura": r"^50[0-9]{14,17}$"
    }

    for bandeira, regex in bandeiras.items():
        if re.match(regex, numero):
            return bandeira
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    bandeira = None
    bandeira_imagem = None
    numero = ""
    bandeiras_imagens = {
        "MasterCard": "https://upload.wikimedia.org/wikipedia/commons/0/04/Mastercard-logo.png",
        "Visa": "https://upload.wikimedia.org/wikipedia/commons/4/41/Visa_Logo.png",
        "American Express": "https://upload.wikimedia.org/wikipedia/commons/3/30/American_Express_logo_%282018%29.svg",
        "Diners Club": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Diners_Club_Logo3.svg",
        "Discover": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Discover_Card_logo.svg",
        "enRoute": "https://upload.wikimedia.org/wikipedia/commons/6/6b/EnRoute_Card_logo.png",
        "JCB": "https://upload.wikimedia.org/wikipedia/commons/0/0b/JCB_logo.svg",
        "Voyager": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Voyager_Card_logo.png",
        "HiperCard": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Hipercard_logo.png",
        "Aura": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Aura_Card_logo.png"
    }

    if request.method == "POST":
        numero = request.form.get("numero")
        if numero:
            numero = numero.replace(" ", "")  # Remove espaços do número do cartão
        bandeira = validar_cartao(numero)
        if bandeira:
            bandeira_imagem = bandeiras_imagens.get(bandeira)

    return render_template("index.html", bandeira=bandeira, bandeira_imagem=bandeira_imagem, numero=numero)

if __name__ == "__main__":
    app.run(debug=True)