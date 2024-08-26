function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas`
    if (hora >= 0 && hora < 12) {
        // Bom dia!
        img.src = 'img/manha.png'
        document.body.style.background = '#e4ccb0'
    } else if (hora >= 12 && hora < 19) {
        // Boa tarde!
        img.src = 'img/tarde.png'
        document.body.style.background = '#8ccdfa'
    } else {
        // Boa noite!
        img.src = 'img/noite.png'
        document.body.style.background = '#006a6e'
    }
}
