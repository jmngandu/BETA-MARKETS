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


let faqs = document.getElementById("faqs")
let storeFaqs = localStorage.setItem("faqs", "what is jthreeGlobally")
let renderFaqs = localStorage.getItem("faqs")
console.log(renderFaqs)
localStorage.clear()
