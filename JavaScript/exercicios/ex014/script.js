function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var bom = document.getElementById('bom')
    var data = new Date()

    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas`
    
    if (hora >= 0 && hora < 12) {
        bom.innerHTML = 'Bom dia!'
        img.src = 'img/manha.png'
        document.body.style.background = '#e4ccb0'
    } else if (hora >= 12 && hora < 19) {
        bom.innerHTML = 'Boa tarde!'
        img.src = 'img/tarde.png'
        document.body.style.background = '#8ccdfa'
    } else {
        bom.innerHTML = 'Boa noite!'
        img.src = 'img/noite.png'
        document.body.style.background = '#006a6e'
    }
}
