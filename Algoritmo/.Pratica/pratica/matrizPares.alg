algoritmo "semnome"
var
m: vetor[1..3, 1..3] de Inteiro
l, c: Inteiro
inicio
Para l <- 1 ate 3 faca
   Para c <- 1 ate 3 faca
      Escreva("Digite o valor da posição [", l, ",", c, "]: ")
      Leia(m[l,c])
   FimPara
FimPara
EscrevaL("--------------------------------------")
EscrevaL("MATRIZ:")
EscrevaL()
Para l <- 1 ate 3 faca
   Para c <- 1 ate 3 faca
      Se(m[l,c] % 2 = 0) entao
         Escreva("{", m[l, c]:2, "}")
      SeNao
         Escreva(m[l,c]:4)
      FimSe
      FimPara
      EscrevaL()
   FimPara

   EscrevaL("--------------------------------------")
fimalgoritmo
