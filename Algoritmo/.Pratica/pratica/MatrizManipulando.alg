algoritmo "semnome"
var
m: vetor[1..4, 1..4] de Inteiro
l, c, sDP, p2L, mai3C: Inteiro
inicio
p2L <- 1
Para l <- 1 ate 4 faca
     Para c <- 1 ate 4 faca
          Escreva("Digite o valor da posi��o [", l, ",", c, "]: ")
          Leia(m[l,c])
          Se (l = c) entao
             sDP <- sDP + m[l,c]
          FimSe
     FimPara
FimPara

Para l <- 1 ate 4 faca
     Para c <- 1 ate 4 faca
          Escreva(m[l,c]:4)
     FimPara
     EscrevaL()
FimPara

Para c <- 1 ate 4 faca
     p2L <- p2L * m[2,c]
FimPara

Para l <- 1 ate 4 faca
     Se (m[l,3] > mai3C) entao
        mai3C <- m[l,3]
     FimSe
FimPara

EscrevaL()
EscrevaL("A soma dos valores da Diagonal Pincipal:", sDP)
EscrevaL("O produto dos valores da Segunda Linha:", p2L)
EscrevaL("O maior valor da terceira Coluna:", mai3C)
fimalgoritmo
