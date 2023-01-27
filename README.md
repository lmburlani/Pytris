# Pytris: O Jogo de Tetris em Python

Este é um jogo de Tetris simples escrito em Python usando a biblioteca Pygame. Ele inclui as peças I, J, L, O, S, T e Z e permite que o jogador as mova e gire. O objetivo do jogo é organizar as peças para preencher completamente as linhas no tabuleiro de jogo.
Como jogar

    Use as setas para mover a peça atual para a esquerda, direita ou baixo.
    Use a tecla 'cima' para girar a peça.
    Pressione 'p' para pausar o jogo.
    Pressione 'r' para reiniciar o jogo.
    Pressione 'q' para sair do jogo.

Lógica do script

O script começa inicializando o Pygame e criando uma janela do jogo. Em seguida, ele define as variáveis ​​necessárias, como as dimensões da janela, as cores das peças e as formas das peças.

Em seguida, o script entra em um loop principal do jogo. Neste loop, ele gera peças aleatoriamente e as faz cair automaticamente. O jogador pode mover e girar as peças usando as teclas de seta. Quando uma linha é completamente preenchida, ela é removida e as linhas acima descem. O jogo termina quando a peça atual atinge o topo da tela.

Finalmente, o script finaliza o Pygame e encerra o jogo.
Como executar o jogo

Para executar o jogo, você precisará ter o Python e o Pygame instalados em seu computador. Em seguida, basta executar o arquivo pytris.py usando o seguinte comando no terminal:

python pytris.py

Divirta-se jogando Py-tris!
