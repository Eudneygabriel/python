// Função para abrir o modal
function abrirModal() {
  document.getElementById("modal").style.display = "flex";
}

// Função para fechar o modal
function fecharModal() {
  document.getElementById("modal").style.display = "none";
}

// Associar o evento de clique à imagem
document.getElementById("imagem").onclick = function () {
  abrirModal();
};

// Fechar o modal ao clicar fora do conteúdo
window.onclick = function (event) {
  if (event.target.classList.contains("modal")) {
    fecharModal();
  }
};
