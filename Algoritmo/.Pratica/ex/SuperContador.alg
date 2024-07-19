algoritmo "SuperContador"
var
   esc, cont: inteiro
inicio
repita
      escreval("=================")
      escreval("|    M e n u    |")
      escreval("=================")
      escreval("| [1] De 1 a 10 |")
      escreval("| [2] De 10 a 1 |")
      escreval("| [3] Sair      |")
      escreval("=================")
      leia(esc)
      escolha esc
              caso 1
                   cont <- 0
                   repita
                         cont <- cont + 1
                         escreva(cont, "...")
                   ate (cont = 10)
                   escreval
              caso 2
                   cont <- 11
                   repita
                         cont <- cont - 1
                         escreva(cont, "...")
                   ate (cont = 1)
                   escreval
      fimescolha
ate(esc = 3)
escreva("saindo...")
fimalgoritmo
