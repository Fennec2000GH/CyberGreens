
function setActiveCard(index) {
    var cards = document.querySelector(".card-group");
    console.log(cards);
    for (var i = 0; i < 5; i++) {
        cards.children[i].style.display = "none";
        if (index == i) {
            cards.children[i].style.display = "inline";
            cards.children[i].style.width = "100%";
        }
    }
}
