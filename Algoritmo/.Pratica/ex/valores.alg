algoritmo "Valores"
var
   c, num, soma, nulo, par, divi: inteiro
   media: real
inicio
      para c <- 1 ate 5 faca
           escreva("Digite o", c, "º valor: ")
           leia(num)
           soma <- soma + num
           se (num % 5 = 0) entao
              divi <- divi + 1
           fimse
           se (num = 0) entao
              nulo <- nulo + 1
           fimse
           se (num % 2 = 0) entao
              par <- par + num
           fimse
      fimpara
      media <- soma / 5
      escreval("A soma entre os valores é:", soma)
      escreval("A média entre os valores é:", media)
      escreval("Valores divisiveis por cinco:", divi)
      escreval("Valores nulos:", nulo)
      escreval("Soma dos valores pares:", par)
fimalgoritmo
