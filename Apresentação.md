<div align="center">
  <img src="https://img.shields.io/github/languages/top/eric-zanchettin/inadimplentes_bcb-api" />
  <img src="https://img.shields.io/github/license/eric-zanchettin/inadimplentes_bcb-api" />
</div>

<h1>🎲 Inadimplentes BCB - API</h1>
<p>Este é um projeto utilizado para adquirir os dados de inadimplentes regionais - por UF - do Banco Central do Brasil 
por meio de um serviço de API disponibilizada pelos mesmos. O próprio código irá identificar qual foi a última atualização 
do Banco Central, referente aos dados de Inadimplentes, e irá gerar um relatório Excel que poderá ser salvo pelo usuário 
no diretório que o mesmo escolher.</p>

<h1>👨🏼‍💻 Tecnologias</h1>
<p>A linguagem principal utilizada neste projeto fora Python, do qual utilizou dos seguintes frameworks:</p>
<ul>
  <li><b>requests</b>: Capaz de trazer os dados da API do BCB por meio da request.GET;</li>
  <li><b>pandas</b>: Utilizado para gerar o dataframe que será salvo numa planilha;</li>
  <li><b>openpyxl</b>: Como dependência do pandas, é usado como a engine para salvar a planilha .xlsx;</li>
  <li><b>Tkinter</b>: Usado para perguntar ao usuário aonde armazenar os dados obtidos.</li>
</ul>

<h1>🚀 Instalação</h1>
<p>Para fazer uso do projeto, pode-se clonar o mesmo com git:</p>
```git
git clone https://github.com/eric-zanchettin/inadimplentes_bcb-api.git
```
<p>Após isso, no ambiente Python, utilize:</p>
```bash
pip install requests
pip install pandas
pip install openpyxl
```
<p>Depois de configurado, basta rodar o .\main.py</p>
<h1>Licença</h1>
<a href="https://choosealicense.com/licenses/mit/">MIT</a>
