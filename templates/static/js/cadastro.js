var cpf = document.getElementById('id_cpf');
var rg= document.getElementById('id_rg');
var data = document.getElementById('id_data_de_nascimento');
data.setAttribute("maxlength","10")

cpf.addEventListener("input",formatar_cpf)
rg.addEventListener("input",formatar_rg)
data.addEventListener("input",formatar_data)
function formatar_cpf() {
    let cpf_valido = /^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$/;
    if (cpf_valido.test(cpf.value)==false) {
        cpf.value=cpf.value.replace(/\D/,"");
        if (cpf.value.length === 11) {
            cpf.value= cpf.value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/,"$1.$2.$3-$4");
        }
    }
}
function formatar_rg() {
    let rg_valido=/^[0-9]{2}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$/;
        if (rg_valido.test(rg.value)==false) {
            rg.value=rg.value.replace(/\D/,"")
            if (rg.value.length === 10) {
                rg.value= rg.value.replace(/(\d{2})(\d{3})(\d{3})(\d{2})/,"$1.$2.$3-$4")
            }
        }
}
function formatar_data() {
    let data_valido=/^[0-9]{2}[/][0-9]{3}[/][0-9]{4}$/;
            if (data_valido.test(data.value)==false) {
                data.value=data.value.replace(/\D/,"")
                if (data.value.length === 8) {
                    data.value= data.value.replace(/(\d{2})(\d{2})(\d{4})/,"$1/$2/$3")
                }
            }
}