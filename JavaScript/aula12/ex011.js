let idade = 15
console.log(`Você tem ${idade} anos.`)
if (idade >= 18 && idade < 65) {
    console.log('Voto obrigatório!')
} else if (idade >= 16 || idade >= 65) {
    console.log('Voto opcional!')
} else {
    console.log('Não vota!')
}