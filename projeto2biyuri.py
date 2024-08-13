#Introdução a Programação
#Yuri Teixeira, Info1M
res = acerto = 0
gabarito = ''
letras = 'abcd'
while res != 4:
    print('Digite 1 para o trivia de matemática,\n2 para o trivia de biologia,\n3 para o trivia de programação\n4 para sair e\n5 para os créditos.')
    res = int(input())
    #Recebe a escolha do quiz
    if res < 1 or res > 5:
        print('Resposta inválida.')
        continue
    #SAÍDA DO PROGRAMA
    elif res == 4:
        print('Você escolheu \033[1;31msair\033[m do trivia.')
        print('Volte novamente! =^)')
        break
    #CRÉDITOS
    elif res == 5:
        print('='*43)
        print('Criador: Yuri Teixeira, da turma de info1m.\nData de criação: 12/08/24\nAproveite o quiz! =D')
        print('='*43)
        continue
    #MATEMÁTICA
    elif res == 1:
        acerto = 0
        print('\033[1;32mEntrando\033m no trivia de matemática...')
        print('Qual dessas opções apresenta o teorema de pitágoras?')
        print(' a) b^2 - 4×a×c\n', 'b) b×h / 2\n', 'c) C×I×T \n', 'd) a^2 + b^2 = c^2')
        gabarito = input().lower()
        #Caso a resposta não esteja na lista de letras, será tida como inválida, requerindo-a continuamente.
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        #Define a resposta correta.
        if gabarito == 'd':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        #Checa se a resposta está dentro das opções válidas e, caso não bater com a resposta certa, será tida como errada.
        elif gabarito != 'd' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Qual dos números abaixo \033[1;33mNÃO\033[m é primo?')
        print(' a) 5\n', 'b) 2\n', 'c) 6\n', 'd) 7')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'c':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'c' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Qual o valor de 1/3 de 603?')
        print(' a) 201\n', 'b) 402\n', 'c) 104\n', 'd) 301.5')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'a':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'a' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Маrсеlа gаnhа R$30,00 dе mеѕаdа. Еlа еѕtá есоnоmіzаndо R$12,00 роr mêѕ раrа соmрrаr um vіdео-gаmе dе R$180,00. Еm quаntоѕ mеѕеѕ еlа tеrá МАІЅ dо quе о dіnhеіrо ѕufісіеntе раrа соmрrаr о vіdео-gаmе?')
        print(' a) 15\n', 'b) 16\n', 'c) 12\n', 'd) 13')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'b':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'a' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        acertoPor100 = (acerto / 4) * 100
        #Pega o número de acertos, divide pelo número de questões e multiplica por 100 para obter a porcentagem de acertos.
        print('FIM!')
        print(f'Você acertou {acertoPor100}% do trivia!')
        #A estrutrura do programa periste a mesma pelos outros temas.
    #BIOLOGIA
    elif res == 2:
        acerto = 0
        print('\033[1;32mEntrando\033[m no trivia de biologia...')
        print('Em qual órgão o sistema muscular atua com movimentos involuntários?')
        print(' a) Cérebro\n', 'b) Rins\n', 'c) Artérias\n', 'd) Coração')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'd':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'd' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Quais são as classificações dos tecidos do corpo?')
        print(' a) Esquelético, liso e cardíaco\n', 'b) Frouxo, denso, pavimentoso e cilíndrico\n', 'c) Pseudoestratificado, simples, adiposo e esquelético\n', 'd) Epitelial, conjuntivo, muscular e nervoso')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'd':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'd' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Qual função possui o núcleo de uma célula?')
        print(' a) Armazenar material genético\n', 'b) As demais alternativas estão corretas\n', 'c) Controlar atividades hormonais\n', 'd) Absorver nutrientes para o funcionamento da célula')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'a':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'a' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Para regular a composição química do sangue, onde as substâncias tóxicas são eliminadas?')
        print(' a) Na troca de gases por respiração\n', 'b) Na urina\n', 'c) Nas fezes\n', 'd) No suor')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'b':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'b' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        acertoPor100 = (acerto / 4) * 100
        print('FIM!')
        print(f'Você acertou {acertoPor100}% do trivia!')
    #PROGRAMAÇÃO
    elif res == 3:
        acerto = 0
        print('\033[1;32mEntrando\033[m no trivia de programação...')
        print('Qual das opções \033[1;33mNÃO\033[m apresenta um pilar da programação?')
        print(' a) Algoritmo\n', 'b) Abstração\n', 'c) Instrução\n', 'd) Decomposição')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'c':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'c' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Qual figura em um fluxograma representa uma decisão?')
        print(' a) Quadrado\n', 'b) Losango\n', 'c) Triângulo\n', 'd) Retângulo')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'b':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'b' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Qual das opções abaixo não é desejável ao escrever um algoritmo?')
        print(' a) Clareza\n', 'b) Objetividade\n', 'c) Reconhecimento de padrões\n', 'd) Ambiguidade')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'd':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'd' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        print('Qual abaixo não é uma forma de representação de algoritmos?')
        print(' a) Infográfico\n', 'b) Linguagem natural\n', 'c) Pseudocódigo\n', 'd) Fluxograma')
        gabarito = input().lower()
        while gabarito not in letras:
            print('Resposta \033[1;33mINVÁLIDA\033[m!')
            gabarito = input(' ').lower()
        if gabarito == 'a':
            print('Resposta \033[1;32mCERTA\033[m!')
            acerto += 1
        elif gabarito != 'a' and gabarito in letras:
            print('Resposta \033[1;31mERRADA\033[m!')
        acertoPor100 = (acerto / 4) * 100
        print('FIM!')
        print(f'Você acertou {acertoPor100}% do trivia!')
        
