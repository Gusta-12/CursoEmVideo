algoritmo "EscolhendoPessoas"
var
   sex, opc : caractere
   idade, cabelo, contM, contF : inteiro
inicio
      contM <- 0
      contF <- 0
      repita
         escreval("========================")
         escreval("   SELETOR DE PESSOAS   ")
         escreval("========================")
         escreva("Qual o sexo? [M/F] ")
         leia(sex)
         escreva("Qual a idade? ")
         leia(idade)
         escreval("Qual a cor do cabelo?")
         escreval("------------------------")
         escreval("[1] Preto")
         escreval("[2] Castanho")
         escreval("[3] Loiro")
         escreval("[4] Ruivo")
         leia(cabelo)
         se (sex = "M") e (idade > 18) e (cabelo = 2) entao
            contM <- contM + 1
         fimse
         se (sex = "F") e (25 <= idade) e (idade <= 30) e (cabelo = 3) entao
            contF <- contF + 1
         fimse
         escreva("Deseja continuar? [S/N] ")
         leia(opc)
         limpatela
      ate (opc = "N")
      escreval("-------------------------------------------------------------")
      escreval("                       RESULTADO FINAL                       ")
      escreval("-------------------------------------------------------------")
      escreval("Total de homens com mais de 18 anos, de cabelos castanhos: ", contM)
      escreval("Total de mulheres entre 25 e 30 anos, de cabelos loiros: ", contF)
      escreval("-------------------------------------------------------------")
fimalgoritmo
