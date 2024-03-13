let connected = document.querySelector("#starting");
let helpTag = document.getElementById("help-tag")
helpTag.addEventListener("dblclick", () => {
    document.body.style.backgroundColor = 'grey';
    helpTag.innerText = "SHOP PRO"
})
helpTag.addEventListener("click", () => {
    document.body.style.backgroundColor = 'blue';
    document.body.style.color = 'black';
    helpTag.innerText = "SHOP BLUE"
})


window.addEventListener("load", function () {
    connected.style.display = "none"
})

const barsMenu = document.querySelector(".fa-bars")
const crossMenu = document.querySelector(".fa-xmark")
const navs = document.querySelector(".navs")
const joinEl = document.getElementById("main-btn")

barsMenu.addEventListener("click", () => {
    navs.style.display = "block"
    barsMenu.style.display = "none"
    crossMenu.style.display = "block"
})
crossMenu.addEventListener("click", () => {
    navs.style.display = "none"
    barsMenu.style.display = "flex"
    crossMenu.style.display = "none"
    window.scrollTo({top: 0, behavior: "smooth"})
});

joinEl.addEventListener("click", () => {
    prompt('Confirm your not a robot');
    alert('Please wait ...');
})
