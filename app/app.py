from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Conectar ao banco de dados
conn = psycopg2.connect(
    host="db",
    port=5432,
    user="postgres",
    password="password",
    database="mydatabase"
)
cur = conn.cursor()

# Rota para enviar dados ao banco de dados
@app.route('/enviar_dados', methods=['POST'])
def enviar_dados():
    try:
        # Obter a mensagem do corpo da requisição
        mensagem = request.json.get('mensagem')

        # Executar uma consulta para inserir a mensagem no banco de dados
        cur.execute("INSERT INTO dados (mensagem) VALUES (%s)", (mensagem,))
        conn.commit()

        return jsonify({"mensagem": f"Dados '{mensagem}' enviados com sucesso para o banco de dados"})
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
