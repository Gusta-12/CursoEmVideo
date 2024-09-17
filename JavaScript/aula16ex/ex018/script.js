let num = document.getElementById('fnum')
let lista = document.getElementById('flista')
let res = document.getElementById('res')
let valores = []

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
    if (isNumero(num.value) && !inLista(num.value, valores)) { // 2 funções, verifica se é um número | verifica se NÃO está na lista
        valores.push(Number(num.value))
        let item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado.`
        lista.appendChild(item)
        res.innerHTML = ''
    } else {
        alert('[ERRO] Valor inválido OU já encontrado na lista!')
    }
    num.value = ''
    num.focus() // volta para area de digitação automaticamente
}

function finalizar() {
    if (valores.length == 0) {
        alert('[ERRO] Adicione algum valor!')
    } else {
        valores.sort()
                
        let soma = 0
        let media = 0
        for(let pos in valores) {
            soma += valores[pos]
        }
        media = soma / valores.length
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${valores.length} elementos cadastrados.</p>`
        res.innerHTML += `<p>Maior valor: ${valores[valores.length - 1]}</p>`
        res.innerHTML += `<p>Menor valor: ${valores[0]}</p>`
        res.innerHTML += `<p>Soma dos valores: ${soma}</p>`
        res.innerHTML += `<p>Média dos valores: ${media}</p>`

    }
}

// Solução do ERRO que não deixava o script.js funcionar direito: local do "script:src" precisa ser no <body> ao invés do <head>