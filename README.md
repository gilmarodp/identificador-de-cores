# Identificador de Cores
O Identificador de Cores é um projeto pessoal para aplicar os conhecimentos adquiridos nos estudos de Visão Computacional.

## Dependências do projeto:
|Biblioteca| Versão |
|--|--|
| cycler | 0.10.0 |
| imutils | 0.5.4 |
| kiwisolver | 1.3.1 |
| matplotlib | 3.4.2 |
| numpy | 1.20.3 |
| opencv-python | 4.5.2.54 |
| Pillow | 8.2.0 |
| pyparsing | 2.4.7 |
| python-dateutil | 2.8.1 |
| six | 1.16.0 |

## Instalando as Dependências
Antes de qualquer coisa você terá que clonar este repositório utilizando o `git` ou baixando o `.zip` direto do repositório.

    git clone https://github.com/gilmarodp/identificador-de-cores.git

Logo após a clonagem do repositório na sua máquina, basta entrar na pasta do projeto:

	cd identificador-de-cores

Entre os arquivos do projeto, deixei um arquivo especial para o python, o `requirements.txt` que é o responsável por guardar todas as bibliotecas que o projeto depende, então para instalar todas elas basta executar o seguinte comando no seu prompt de comando ou terminal:

    pip install -r requirements.txt

Você só vai precisar a instalação de todas as dependências e daí vai conseguir utilizar tranquilamente o projeto.

## Utilizando o Sistema
Primeiramente você vai executar o arquivo principal, o `main.py`:
	
	python main.py

Quando executado o comando, o projeto vai retornar as câmeras disponíveis em seu dispositivo, você irá selecionar o ID da câmera, se algum dos ID's não funcionar, pressione a tecla `Q` para sair e tente outro ID de câmera disponível.
	
	Você possui 2 dispositivos disponíveis.
		
		[ 0 ] -> Câmera 0
		[ 1 ] -> Câmera 1
		 
	>: _
Ao selecionar o ID, irá abrir uma janela no seu sistema operacional e daí você já pode usar :D.
