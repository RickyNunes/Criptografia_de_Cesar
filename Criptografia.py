op = '0'
key=0
while (op != 3):

    print("                                      ")
    print(" Opções ")
    print("                                      ")
    print("[1] Cifra reversa")
    print("[2] Cifra de Cézar")
    print("[3] Encerrar Programa")
    print("                                      ")


    op = int(input("Escolha a operação: "))
    print("                                      ")

    if(op==1):
        
        print("                                      ")
        print("DEFINIÇÃO DE COMO REVERTER A CIFRA DE CÉZAR")
        print("                                      ")
        print("A Cifra reversa reverte a criptografia de Cézar para a sua forma original. Sendo assim, caso você tenha a chave predeterminada pela pessoa que criptografou a mensagem você poderá descritografar a mensagem, mas a criptografia pode ser quebrada por tentativas, basta que você tente varios números até encontrar o número definido como chave pela pessoa que criptografou a mensagem.")
        print("                                      ")
        print("                                      ")
        Opção1 =input("Digite a palavra ou frase para ser descriptografada pelo método de Cézar: ")
        print("                                      ")
        key2=key
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        translated = ''
        Opção1 = Opção1.upper() 

  
        if key2==key:
            print("Sua chave atual é: ", key2)
            print("                                      ")
            print("Você deseja alterar a sua chave? ")
            print("[1] SIM")
            print("[2] NÃO")
            alterar=int(input("Digite a sua opção: "))
            if alterar==1:
                key2=int(input("Digite um número inteiro para utilizar como chave: "))
                key=key2
            elif alterar==2:
                key2=key
                
                        
        for symbol in Opção1:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) 
                num = num - key
                if num >= len(LETTERS): 
                    num = num - len(LETTERS)
                elif num < 0: 
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num] 
            else: 
                translated = translated + symbol
                
        
        print("                                      ")
        print("                                      ")
        print("A palavra ", Opção1,"ao ser descriptografada com a chave", key2, "ficará: ", translated)
        print("                                      ")
        print("                                      ")

      
    elif(op==2):
        print("                                      ")
        print("DEFINIÇÃO DA CIFRA DE CÉZAR")
        print("                                      ")
        print("Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, A seria substituído por D, B se tornaria E, e assim por diante. O nome do método é em homenagem a Júlio César, que o usou para se comunicar com os seus generais. O processo de criptografia de uma cifra de César é frequentemente incorporado como parte de esquemas mais complexos, como a cifra de Vigenère, e continua tendo aplicações modernas, como no sistema ROT13. Como todas as cifras de substituição monoalfabéticas, a cifra de César é facilmente decifrada e na prática não oferece essencialmente nenhuma segurança na comunicação.")
        print("                                      ")
        print("                                      ")
        print("                                      ")
        Opção2 =input("Digite a palavra ou frase para ser criptografada pelo método de Cézar: ")
        key =int(input("Digite um número inteiro para ser usado como chave: "))

        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        translated = ''
        Opção2 = Opção2.upper() 

        for symbol in Opção2:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) 
                num = num + key
                if num >= len(LETTERS): 
                    num = num - len(LETTERS)
                elif num < 0: 
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else: 
                translated = translated + symbol
        print("                                      ")
        print("                                      ")
        print("A palavra ", Opção2,"ao ser criptografada com a chave", key, "ficará: ", translated)
        print("                                      ")
        print("                                      ")


    else:
        print("")
        print("################################################################")
        print("Programa finalizado. by ~Ricky")
        print("################################################################")
        quit()
