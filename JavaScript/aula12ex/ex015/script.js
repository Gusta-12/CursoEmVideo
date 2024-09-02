function verificar() {
    var data = new Date()
    var ano = data.getFullYear() // FullYear = 4 digitos
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || fano.value > ano) {
        alert('Verifique os dados, e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        
        // criando a tag 'img' pelo JS
        var img = document.createElement('img') // cria uma tag no html
        img.setAttribute('id', 'foto') // cria um atributo dentro da tag

        if (fsex[0].checked) { // Se a PRIMEIRA bolinha estiver marcada:
            genero = 'Homem'

            if (idade >=0 && idade < 10) {
                // Criança
                img.setAttribute('src', 'img/bebeM.png')
            } else if (idade < 21) {
                // Jovem
                img.setAttribute('src', 'img/jovemM.png')
            } else if (idade < 50) {
                // Adulto
                img.setAttribute('src', 'img/adultoM.png')
            } else {
                // Idoso
                img.setAttribute('src', 'img/idosoM.png')
            }

        } else if (fsex[1].checked) {
            genero = 'Mulher'

            if (idade >= 0 && idade < 10) {
                // Criança
                img.setAttribute('src', 'img/bebeF.png')
            } else if (idade < 21) {
                // Jovem
                img.setAttribute('src', 'img/jovemF.png')
            } else if (idade < 50) {
                // Adulta
                img.setAttribute('src', 'img/adultaF.png')
            } else {
                // Idosa
                img.setAttribute('src', 'img/idosaF.png')
            }
        }
        
        res.style.textAlign = 'center'
        res.innerHTML = `<p>Detectamos ${genero} com ${idade} anos.</p>`
        res.appendChild(img) // Adiciona um elemento
    }
}