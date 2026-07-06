// Please see documentation at https://learn.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

function getFavoritos() {
    const favs = localStorage.getItem('bibliotecaFavoritos');
    return favs ? JSON.parse(favs) : [];
}

function saveFavoritos(favs) {
    localStorage.setItem('bibliotecaFavoritos', JSON.stringify(favs));
}

function isFavorito(titulo) {
    const favs = getFavoritos();
    return favs.includes(titulo);
}

function toggleFavorito(event, titulo) {
    event.stopPropagation();
    event.preventDefault();

    let favs = getFavoritos();
    if (favs.includes(titulo)) {
        favs = favs.filter(t => t !== titulo);
    } else {
        favs.push(titulo);
    }
    saveFavoritos(favs);
    atualizarIconesFavoritos();
}

function atualizarIconesFavoritos() {
    const icones = document.querySelectorAll('.favorito-icon');
    const favs = getFavoritos();

    icones.forEach(icone => {
        const titulo = icone.getAttribute('data-fav-titulo');
        if (titulo && favs.includes(titulo)) {
            icone.style.color = '#f1c40f'; // Estrela amarela
        } else {
            icone.style.color = '#ccc'; // Estrela cinza
        }
    });
}

// Inicializa a cor das estrelas na vitrine
document.addEventListener('DOMContentLoaded', () => {
    atualizarIconesFavoritos();
});
