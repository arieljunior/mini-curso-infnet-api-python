from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = [{
    "id": 1,
    "nome": "Bob"
},{
    "id": 2,
    "nome": "João"
}]

@app.route("/clientes", methods=["GET"])
def get_clientes():
    return jsonify(clientes)

@app.route("/cliente/<int:id_cliente>", methods=["GET"])
def get_cliente_por_id(id_cliente):
    cliente = next((cliente for cliente in clientes if cliente['id'] == id_cliente), None)
    if cliente:
        return jsonify(cliente)
    return jsonify({"msg": "Cliente não encontrado"}),404

@app.route("/cliente", methods=["POST"])
def criar_cliente():
    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": request.json['nome']
    }
    clientes.append(novo_cliente)
    return jsonify({"msg": "Cliente criado com sucesso"})

@app.route("/cliente/<int:id_cliente>", methods=["PUT"])
def atualizar_cliente(id_cliente):
    cliente = next((cliente for cliente in clientes if cliente['id'] == id_cliente), None)
    
    if cliente:
        cliente["nome"] = request.json["nome"]
        return jsonify({"msg": "Cliente atualizado com sucesso"})
    return jsonify({"msg": "Cliente não encontrado"}),404

@app.route("/cliente/<int:id_cliente>", methods=["DELETE"])
def deletar_cliente(id_cliente):
    cliente = next((cliente for cliente in clientes if cliente['id'] == id_cliente), None)
    
    if cliente:
        clientes.remove(cliente)
        return jsonify({"msg": "Cliente deletado com sucesso"})
    return jsonify({"msg": "Cliente não encontrado"}),404

if __name__ == "__main__":
    app.run(debug=True, port=8000)






