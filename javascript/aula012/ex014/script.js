function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()

    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >=0 && hora< 12) {
        // Bom Dia!
        img.src = 'manha1.png'
        document.body.style.background = "#15380A"
    }//
    else if (hora >=12 && hora < 18) {
        //Boa Tarde!
        img.src = 'tarde1.png'
        document.body.style.background = "#E9C072"
    }//#
    else {
        //Boa noite
        img.src = 'noite1.png'
        document.body.style.background = "#834B5C"
    }//
}