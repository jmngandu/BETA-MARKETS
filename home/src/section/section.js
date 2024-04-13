let running = document.querySelector("#starting");
window.addEventListener("load", function () {
  running.style.display = "none";
});

const welcomeEl = document.getElementById("signup");
const loginEL = document.querySelector(".loginEl");
const signEL = document.querySelector(".signEL");

welcomeEl.addEventListener("click", () => {
  alert("welcome to BETAMARKETS");
});
loginEL.addEventListener("click", () => {
  alert("logged in successfully");
});

signEL.addEventListener("click", () => {
  alert("account created");
});
