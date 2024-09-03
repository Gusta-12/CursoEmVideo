function tabuada() {
    let num = document.getElementById("txtn")
    let tab = document.getElementById("seltab")
    
    if (num.value.length == 0) {
        alert("[ERRO] Informe um número!")
    } else {
        let x = Number(num.value)
        let c = 0
        /* Usando FOR
        for(c = 0; c <= 10; c++) {
            res.innerHTML += `${x} x ${c} = ${x * c} </br>`
        }
        */
        // Usando WHILE
        tab.innerHTML = '' // Limpa a área da tabuada
        while(c <= 10) {
            let item = document.createElement('option')
            item.text = `${x} x ${c} = ${x * c}` 
            item.value = ´tab${c}´ // Para linguagens como PHP
            tab.appendChild(item)
            c++
        }
    }

}
