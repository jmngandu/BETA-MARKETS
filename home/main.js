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
