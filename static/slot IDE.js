// Função para abrir o modal e carregar o conteúdo da página "slot IDE"
function abrirModalSlotIDE() {
  fetch("/caminho/para/slot-ide.html") // Substitua pelo caminho real do arquivo "slot IDE"
    .then((response) => response.text())
    .then((html) => {
      // Insere o conteúdo HTML carregado no modal
      document.getElementById("modal-slot-ide-content").innerHTML = html;
      // Exibe o modal
      document.getElementById("modal-slot-ide").style.display = "flex";
    })
    .catch((error) => {
      console.error("Erro ao carregar a página Slot IDE:", error);
    });
}

// Função para fechar o modal
function fecharModalSlotIDE() {
  document.getElementById("modal-slot-ide").style.display = "none";
}

// Fecha o modal ao clicar fora do conteúdo
window.onclick = function (event) {
  if (event.target.classList.contains("modal")) {
    fecharModalSlotIDE();
  }
};
