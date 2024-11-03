// Função para abrir o modal com base no ID
function abrirModal(idModal) {
  const modal = document.getElementById(idModal);
  if (modal) {
    modal.style.display = "flex"; // Exibe o modal como um flex container para centralização
  }
}

// Função para fechar todos os modais
function fecharModal() {
  // Seleciona todos os elementos com a classe 'modal' e oculta cada um deles
  const modals = document.querySelectorAll(".modal");
  modals.forEach((modal) => {
    modal.style.display = "none";
  });
}

// Fechar o modal ao clicar fora do conteúdo modal
window.addEventListener("click", function (event) {
  const modals = document.querySelectorAll(".modal");
  modals.forEach((modal) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});
