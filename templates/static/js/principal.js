window.addEventListener('DOMContentLoaded',tamanho_tela)
window.addEventListener('resize', tamanho_tela)

function tamanho_tela() {
    if (window.innerWidth < 800) {
        document.getElementById('menu-conteudo').classList.remove('mostrarSidebar')
        document.getElementById('menu-lateral').classList.remove('abrir')
    }
    else{
        document.getElementById('menu-conteudo').classList.add('mostrarSidebar')
        document.getElementById('menu-lateral').classList.add('abrir')
    }
}

function mostrar_lateral() {
    document.getElementById('menu-conteudo').classList.toggle('mostrarSidebar')
    document.getElementById('menu-lateral').classList.toggle('abrir')
}


menu_perfil= document.getElementById('perfil')
menu_perfil.addEventListener('click',sub_menuAbrir)
function sub_menuAbrir() {
    document.getElementById('subMenu').classList.toggle("aberto")
}
menu_cadastrados= document.getElementById('menu-cadastrados')
menu_cadastrados.addEventListener('click',aparecer_cadastrados)
function aparecer_cadastrados() {
    document.getElementById('menuCadastrados').classList.toggle('aberto')
}