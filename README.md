# Projeto_Lab

Melhorias no código:

2 Melhorias foram implementadas

1º Melhoria:

	• Implementação da função posicao_inimigo(V1,V2)
		• Com o objetivo de retornar uma posição aleatória dos carros e, também, para a realização dos testes pelo pytest
		• Que recebe dois parâmetros de entrada das posições dos carros inimigos
			Parâmetros:
				V1 → Posição X dos carros
				V2 → Posição Y dos carros

2º Melhoria:

	• Otimização:
		• Quando se inicia o jogo, um conjunto de variáveis que são utilizadas tão somente na Tela de Título são, então, deletadas, 
		e, com isso, não ficam na memória (já que essas variáveis não são mais utilizadas deste ponto do código.
		
Foram realizados os seguites testes


1º Teste de caixa preta:

	• Foram criadas funções do tipo test_ utilizando o assert do pytest
		• As funções criadas tem como objetivo testar a posição dos inimigos, a tela de títalo, as fases do game alḿ do botão especial para passar 			 para próxima fase do game, totalizando 5 testes feitos, onde nenhum erro foi encontrado durante a realização dos testes.

2º Teste de Caixa branca:
	
	• Foram criadas funções do tipo test_suite utilizando o assert do pytest
		• As funções criadas tem como objetivo testar a posição dos inimigos, a tela de títalo, as fases do game aléḿ do botão especial para passar 			 para próxima fase do game, totalizando 5 testes feitos, onde nenhum erro foi encontrado durante a realização dos testes.


Os testes foram realizados em momentos diferentes no código do game a fim de corrigir erros e fazer testes de funcionalidades buscando a melhoria do código e correção de bugs encontrados:
		

