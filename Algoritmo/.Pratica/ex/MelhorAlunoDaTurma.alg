algoritmo "MelhorAlunoDaTurma"
var
   nome, nomem : caractere
   aluno, cont : inteiro
   nota, nm : real
inicio
   cont <- 1
   escreval("-----------------------")
   escreval(" Escola Santa Paciencia")
   escreval("-----------------------")
   escreva("Quantos alunos a turma tem? ")
   leia(aluno)
   escreval("-----------------------")
   enquanto ( cont <= aluno) faca
      escreval("ALUNO", cont)
      cont <- cont + 1
      escreva("Nome do aluno: ")
      leia(nome)
      escreva("Nota de ", nome, ": ")
      leia(nota)
      escreval("-----------------------")
      se (nota > nm) entao
         nm <- nota
         nomem <- nome
      fimse
   fimenquanto
   escreva("O melhor aproveitamento foi de ", nomem, " com a nota ", nm:)
fimalgoritmo
