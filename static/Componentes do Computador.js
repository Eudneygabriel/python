// Função para abrir o modal do Slot IDE
function abrirMiniPagina() {
  document.getElementById("modal-slot-ide").style.display = "flex";
}

// Função para fechar o modal
function fecharModal() {
  document.getElementById("modal").style.display = "none";
  document.getElementById("modal-slot-ide").style.display = "none";
}

// Fechar o modal ao clicar fora do conteúdo
window.onclick = function (event) {
  if (event.target.classList.contains("modal")) {
    fecharModal();
  }
};

// Associar o evento de clique à imagem da motherboard
document.getElementById("imagem").onclick = function () {
  document.getElementById("modal").style.display = "flex"; // Abre o modal da imagem
};

// Fechar o modal ao clicar fora do conteúdo
window.onclick = function (event) {
  if (event.target.id === "modal") {
    fecharModal();
  }
};
