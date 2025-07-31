from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    nome = request.form['nome']
    servico = request.form['servico']
    data = request.form['data']
    horario = request.form['horario']

    with open('agendamentos.csv', 'a') as f:
        f.write(f'{nome},{servico},{data},{horario}\n')

    return f"Agendamento confirmado para {nome}!"

if __name__ == '__main__':
    app.run(debug=True)
