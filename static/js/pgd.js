  // Função para abrir o modal específico
  function abrirModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
}


// Função para fechar o modal específico
function fecharModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Associar eventos de clique às imagens
document.getElementById('imagem1').onclick = function() {
    abrirModal('modal1');
};

document.getElementById('imagem2').onclick = function() {
    abrirModal('modal2');
};

// Fechar modal ao clicar fora do conteúdo
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
};