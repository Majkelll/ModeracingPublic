const slider = document.querySelector(".overlay-container");
const loginSide = document.querySelector(".form-create-acc");
const formSignIn = document.querySelector(".form-sign-in");
const btnSignIn = document.getElementById("signIn");
const btnSignUp = document.getElementById("signUp");

btnSignUp.addEventListener("click", () => {
  slider.style.transform = "translateX(100%)";
  loginSide.style.transform = "translateX(0)";
  formSignIn.style.transform = "translateX(100%)";
  // overlay btn
  btnSignUp.style.display = "none";
  btnSignIn.style.display = "block";
});

btnSignIn.addEventListener("click", () => {
  slider.style.transform = "translateX(0)";
  loginSide.style.transform = "translateX(-100%)";
  formSignIn.style.transform = "translateX(0)";
  // overlay btn
  btnSignUp.style.display = "block";
  btnSignIn.style.display = "none";
});
