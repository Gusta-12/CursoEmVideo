algoritmo "Valores"
var
   c, num, soma, nulo, par, divi: inteiro
   media: real
inicio
      para c <- 1 ate 5 faca
           escreva("Digite o", c, "� valor: ")
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
      escreval("A soma entre os valores �:", soma)
      escreval("A m�dia entre os valores �:", media)
      escreval("Valores divisiveis por cinco:", divi)
      escreval("Valores nulos:", nulo)
      escreval("Soma dos valores pares:", par)
fimalgoritmo
