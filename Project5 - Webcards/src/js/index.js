const btnAvancar = document.getElementById("btn-avancar");
const btnVoltar = document.getElementById("btn-voltar");
const cards = document.querySelectorAll(".card");
let nowcard = 0;

btnAvancar.addEventListener("click", function () {
  if (nowcard === cards.length - 1) return;

  hideselectedcard();

  nowcard++;
  showcard(nowcard);
});

btnVoltar.addEventListener("click", function () {
  if (nowcard === 0) return;

  hideselectedcard();

  nowcard--;
  showcard(nowcard);
});

function showcard(nowcard) {
  cards[nowcard].classList.add("selected");
}

function hideselectedcard() {
  const selectedcard = document.querySelector(".selected");
  selectedcard.classList.remove("selected");
}
