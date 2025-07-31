from flask import Flask, render_template, request
import csv

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
    
    with open('agendamentos.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nome, servico, data, horario])
    
    return f'Agendamento confirmado para {nome} - {servico} em {data} às {horario}.'

if __name__ == '__main__':
    app.run(debug=True)
