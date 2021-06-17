### Descrição:

Programa em Python para fazer uma "esteganografia", ou seja, esconder um texto dentro de uma imagem (de uma maneira não muito óbvia)

A intenção desse programa é ser um complemento OPCIONAL de um [projeto](https://github.com/danielnowakassis/Experi-ncia-Criativa-PUCPR) de experiência criativa, ele não faz parte diretamente do trabalho, e eu programei isso por opção

Temos 2 programas nesse repositório, o  `mensageiro.py` e o `leitor.py`

Com o `mensageiro.py`, você escolhe uma imagem qualquer, o programa carregará ela e pedirá para o usuário digitar a mensagem que quer. Após alguns segundos (dependendo do tamanho da imagem) uma imagem com o nome `output` será gerada no formato PNG <!--~~desejado (PNG ou JPG)~~ isso infelizmente ta dando erro-->

Para ter acesso aos conteúdos da mensagem, abra o arquivo `leitor.py`, escolha a imagem com a mensagem e o programa mostrará no terminal os conteúdos da mensagem. Se for do agrado do usuário, ele pode salvar os conteúdos da mensagem em um arquivo de texto usando o próprio programa

### Requerimentos:
- Python 3+
- Tkinter (vem pré-instalado com python)
  - Como instalar Tkinter na sua máquina, caso você não possua:
    1. Abra o CMD
    2. Digite `pip install tk`
- PIL (também vem pré-instalado com python)

Para quem for reproduzir esse projeto, recomendo usar a biblioteca Pillow em vez da PIL, PIL é infelizmente uma biblioteca abandonada

Uma melhoria planejada é diminuir o tamanho das mensagens, em vez da mensagem de verdade e toda a memória disponivel, mostrar somente a mensagem
