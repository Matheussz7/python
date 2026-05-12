from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo - Davi Ferreira</title>
            <style>
                /* Estilização Geral */
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f4f7f6;
                    color: #333;
                    line-height: 1.6;
                    margin: 0;
                    padding: 40px 20px;
                    display: flex;
                    justify-content: center;
                }

                /* Container Principal */
                .cv-container {
                    background: #fff;
                    max-width: 700px;
                    width: 100%;
                    padding: 40px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    border-radius: 8px;
                    border-top: 8px solid #2c3e50;
                }

                /* Cabeçalho */
                h1 {
                    color: #2c3e50;
                    margin-bottom: 5px;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }

                h2 {
                    color: #2980b9;
                    border-bottom: 2px solid #ecf0f1;
                    padding-bottom: 5px;
                    margin-top: 30px;
                    font-size: 1.4em;
                }

                /* Listas e Itens */
                ul {
                    list-style: none;
                    padding: 0;
                }

                li {
                    margin-bottom: 10px;
                }

                strong {
                    color: #2c3e50;
                    width: 100px;
                    display: inline-block;
                }

                /* Detalhes da Experiência */
                .experience-item {
                    background: #fdfdfd;
                    padding: 15px;
                    border-left: 4px solid #2980b9;
                    margin-top: 10px;
                }

                /* Responsividade */
                @media (max-width: 600px) {
                    .cv-container { padding: 20px; }
                    strong { display: block; width: auto; }
                }
            </style>
        </head>
        <body>
            <div class="cv-container">
                <h1>Davi Ferreira</h1>
                <p>Estudante de Tecnologia | Aspirante a Desenvolvedor</p>

                <h2>Informações Pessoais</h2>
                <ul>
                    <li><strong>Email:</strong> 22402187@aluno.cotemig.com.br</li>
                    <li><strong>Telefone:</strong> (31) 99526-2217</li>
                    <li><strong>Cidade:</strong> Belo Horizonte - MG</li>
                </ul>

                <h2>Experiência Profissional</h2>
                <div class="experience-item">
                    <ul>
                        <li><strong>Empresa:</strong> Minas Tênis Clube</li>
                        <li><strong>Cargo:</strong> Jovem Aprendiz ADM</li>
                        <li><strong>Período:</strong> Mar 2025 - Nov 2025</li>
                    </ul>
                </div>

                <h2>Formação Acadêmica</h2>
                <ul>
                    <li><strong>Instituição:</strong> Colégio COTEMIG</li>
                    <li><strong>Curso:</strong> Técnico em Informática</li>
                </ul>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
