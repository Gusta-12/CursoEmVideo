/*
let num = [5, 8, 4]

num[3] = 6
num.push(7)

console.log(`${num}`)
console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro valor é ${num[0]}`)

console.log(`Vetor em ordem do menor para o maior: ${num.sort()}`)
*/


let num = [5, 8, 2, 9, 3, 1]
console.log(num)
num.sort()

/*
for (let c = 0; c < num.length; c++) {
    console.log(`Valor da ${c + 1}ª posição: ${num[c]}`)
}
*/
/*
for (let c in num){
    if (Number(c) == 0){
        console.log(typeof c)
    }
    console.log(`Valor da ${Number(c) + 1}ª posição: ${num[c]}`)
}
*/

console.log(num)
console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro valor do vetor é: ${num[0]}`)
let pos = num.indexOf(4)
if (pos == -1) {
    console.log('O valor não foi encontrado!')
} else {
    console.log(`O valor está na posição: ${pos}`)
}
