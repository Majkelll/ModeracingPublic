const btnAccount = document.getElementById("btn-account");
const menu = document.querySelector(".account-settings-conteiner");
menu.style.display = "none";

console.log(btnAccount);
if (btnAccount) {
  btnAccount.addEventListener("click", function () {
    if (menu.style.display !== "none") {
      menu.style.display = "none";
    } else {
      menu.style.display = "flex";
    }
  });
}
