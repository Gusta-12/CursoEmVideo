algoritmo "ListagemDaTurma"
var
   nome: vetor[1..4] de Caractere
   n1: vetor[1..4] de Real
   n2: vetor[1..4] de Real
   m: vetor[1..4] de Real
   SM, MT: Real
   i, tot: Inteiro
inicio
      Para i <- 1 ate 4 faca
           EscrevaL("ALUNO: ", i)
           Escreva("Nome: ")
           Leia(nome[i])
           Escreva("N1: ")
           Leia(n1[i])
           Escreva("N2: ")
           Leia(n2[i])
           EscrevaL("-------")
           m[i] <- (n1[i] + n2[i]) / 2
           SM <- SM + m[i]
      FimPara
      MT <- SM/4
      LimpaTela
      EscrevaL("LISTAGEM DE ALUNOS")
      EscrevaL("------------------")
      Para i <- 1 ate 4 faca
           EscrevaL(nome[i]:14, m[i]:4:1)
           Se (m[i] > MT) entao
              tot <- tot + 1
           FimSe
      FimPara
      EscrevaL("Ao todo temos", tot, " alunos acima da m�dia da turma, que �: ", MT:4:1)
fimalgoritmo
