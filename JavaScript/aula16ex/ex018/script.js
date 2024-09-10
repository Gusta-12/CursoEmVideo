// let num = document.getElementById('fnum')
// let lista = document.getElementById('flista')
// let res = document.getElementById('res')
// let valores = []

function isNumero(n=0) { // Vai verificar se o dado é um número válido!
    if(Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}

function inLista(n=0, l) { // Vai verificar se o número está no vetor!
    if (l.indexOf(Number(n)) != -1) { // Se o valor NÃO for encontrado na lista
        return true
    } else {
        return false
    }
}

function adicionar() {
    let num = document.getElementById('fnum')
    let lista = document.getElementById('flista')
    let res = document.getElementById('res')

    let valores = []

    if (isNumero(num.value) && !inLista(num.value, valores)) { // 2 funções, verifica se é um número | verifica NÃO se está na lista
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado.`
        lista.appendChild(item)
    } else {
        alert('[ERRO] Valor inválido OU já encontrado na lista!')
    }
    num.value = ''
    num.focus() // volta para area de digitação automaticamente
}
