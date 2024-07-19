algoritmo "Fibonacci"
var
   t1, t2, t3, cont: inteiro
inicio
      t1 <- 0
      t2 <- 1
      escreva(t1, t2)
      para cont <- 3 ate 15 faca
           t3 <- t1 + t2
           escreva(t3)
           t1 <- t2
           t2 <- t3
      fimpara
fimalgoritmo
