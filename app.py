from flask import Flask, request, jsonify

app = Flask(__name__)

pontos_vacinacao = [
    {"id": 1, "nome": "Posto Eurico Salles",
        "endereco": "Ladeira Artur Lopes Ferreira, Mangabeiras, Maceió, Alagoas- CEP 57031330",
        "longitude": -35.7306284,
        "latitude": -9.6185752},

    {"id": 2, "nome": "Posto Benevides Lins",
        "endereco": "Rua Humberto Melo, Clima Bom, Maceió, Alagoas- CEP 57071005",
        "longitude": -47.2992763,
        "latitude": -22.7017594},

    {"id": 3, "nome": "Posto Barros Lima",
        "endereco": "Avenida Muniz Falcão, Barro Duro, Maceió, Alagoas- CEP 57045000",
        "longitude": -35.7224823,
        "latitude": -9.6201324}
]


@app.route('/pontos-vacinacao', methods=['GET'])
def obter_pontos_vacinacao():
    return jsonify(pontos_vacinacao)


@app.route('/pontos-vacinacao', methods=['POST'])
def adicionar_ponto_vacinacao():
    dados_requisicao = request.json

    nome = dados_requisicao.get("nome")
    endereco = dados_requisicao.get("endereco")
    longitude = dados_requisicao.get("longitude")
    latitude = dados_requisicao.get("latitude")

    if nome and endereco and longitude is not None and latitude is not None:
        novo_ponto = {
            "id": len(pontos_vacinacao) + 1,
            "nome": nome,
            "endereco": endereco,
            "longitude": longitude,
            "latitude": latitude
        }

        pontos_vacinacao.append(novo_ponto)
        return jsonify({"message": "Novo ponto de vacinação adicionado com sucesso."}), 201
    else:
        return jsonify({"error": "Dados inválidos. Certifique-se de fornecer nome, endereco, longitude e latitude."}), 400


if __name__ == '__main__':
    app.run(debug=True)
