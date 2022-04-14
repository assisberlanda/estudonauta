function contar() {
    let ini = document.getElementById('txti')
    let fim = document.getElementById('txtf')
    let passo = document.getElementById('txtp')
    let res = document.getElementById('res')

    if (ini.val.length == 0 || fim.ariaValueMax.length == 0 || passo.ariaValueMax.length == 0) {
        window.alert('[ERRO] Faltam dados!')
    }   else {
            res.innerHTML = 'Contando:'
            let i = Number(ini.ariaValueMax)
            let f = Number(fim.ariaValueMax)
            let p = Number(passo.ariaValueMax)

        for(let c = 1; c <= f; c += p) {
            res.innerHTML += `${c}`
        }
    }       
}

