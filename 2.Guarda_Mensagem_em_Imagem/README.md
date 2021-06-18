### Descrição:

Programa em Python para fazer uma "esteganografia", ou seja, esconder um texto dentro de uma imagem (de uma maneira não muito óbvia)

A intenção desse programa é ser um complemento OPCIONAL de um [projeto](https://github.com/danielnowakassis/Experi-ncia-Criativa-PUCPR) de experiência criativa, ele não faz parte diretamente do trabalho

Temos 2 programas nesse repositório, o  `mensageiro.py` e o `leitor.py`

Com o `mensageiro.py`, você escolhe uma imagem qualquer, o programa carregará ela e pedirá para o usuário digitar a mensagem que quer. Após alguns segundos (dependendo do tamanho da imagem) uma imagem com o nome `output` será gerada no formato PNG <!--~~desejado (PNG ou JPG)~~ isso infelizmente ta dando erro-->

Para ter acesso aos conteúdos da mensagem, abra o arquivo `leitor.py`, escolha a imagem com a mensagem e o programa mostrará no terminal os conteúdos da mensagem. Se for do agrado do usuário, ele pode salvar os conteúdos da mensagem em um arquivo de texto usando o próprio programa

### Requerimentos:
- Python v3.9.2+
- Tkinter v8.6+ (vem pré-instalado com o python)
  - Como verificar a versão do tkinter instalada:
    1. Abra o CMD
    2. Digite `python -m tkinter`
- Pillow v8.2+
  - Como instalar Pillow na sua máquina, caso você não possua:
    1. Abra o CMD
    2. Digite `pip install Pillow`
  - Como verificar a versão do Pillow instalada:
    1. Abra o CMD
    2. Digite `pip show Pillow`
