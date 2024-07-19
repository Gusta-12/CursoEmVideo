algoritmo "semnome"
var
m: vetor[1..4, 1..4] de Inteiro
i, j: Inteiro
inicio
Para i <- 1 ate 4 faca
     Para j <- 1 ate 4 faca
          Se (i = j) entao
             m[i,j] <- 1
          SeNao
             m[i,j] <- 0
          FimSe
     FimPara
FimPara
Para i <- 1 ate 4 faca
     Para j <- 1 ate 4 faca
          Escreva(m[i,j]:2)
     FimPara
     EscrevaL()
FimPara
fimalgoritmo
