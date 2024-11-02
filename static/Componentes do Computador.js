// Função para abrir um modal específico pelo ID
function abrirModal(id) {
  document.getElementById(id).style.display = "flex";
}

// Função para fechar todos os modais
function fecharModal() {
  const modais = document.querySelectorAll(".modal");
  modais.forEach((modal) => (modal.style.display = "none"));
}

// Associar o evento de clique à imagem da motherboard
document.getElementById("imagem").onclick = function () {
  document.getElementById("modal").style.display = "flex"; // Abre o modal da imagem principal
};

// Fechar o modal ao clicar fora do conteúdo
window.onclick = function (event) {
  if (event.target.classList.contains("modal")) {
    fecharModal();
  }
};
