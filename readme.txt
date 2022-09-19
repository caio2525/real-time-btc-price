Crie um ambiente virtual python com a versão 3.8 e o ative

   python3.8 -m venv env

   source env/bin/activate

Instale as depedências

   pip install -r requirements.txt


Usage:
  Pode-se executar qualquer um dos arquivos app.py ou app2.py
  O primeiro (app.py) utiliza o connector em python para se conectar a API da Binance.
  O Segundo utiliza apenas websockets.

rode:
  python app.py

ou
  python app2.py
