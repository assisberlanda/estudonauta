function Verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value.length == 0 || fano.value.length > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!') 
    } else {
        window.alert('tudo ok')
}
