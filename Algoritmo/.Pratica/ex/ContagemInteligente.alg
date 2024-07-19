algoritmo "ContagemInteligente"
var
   inic, fim : inteiro
inicio
   escreval("CONTAGEM INTELIGENTE")
   escreval("--------------------")
   escreva("Inicio: ")
   leia(inic)
   escreva("Fim: ")
   leia(fim)
   escreval("--------------------")
   escreval("  C O N T A N D O   ")
   escreval("--------------------")
   se (inic >= fim) entao
      enquanto (inic >= fim) faca
         escreva(inic, "...")
         inic <- inic - 1
      fimenquanto
   senao
      enquanto (inic <= fim) faca
         escreva(inic, "...")
         inic <- inic + 1
      fimenquanto
   fimse
fimalgoritmo
