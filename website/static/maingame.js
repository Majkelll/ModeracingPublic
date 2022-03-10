const textBlock = document.getElementById("top");
const mainText =
  "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Soluta deserunt rem, molestias, iure sint voluptatibus aut sit numquam error illo nulla maxime ipsa, ut veritatis laborum architecto cum. Deleniti quis quibusdam doloremque dolores fugit praesentium enim quasi velit aliquid error repellendus, ab illo quisquam culpa eos aperiam accusantium laudantium nihil!";

generatedText = textPrepare(mainText);
textBlock.innerHTML = generatedText;
let writtenText = "";

document.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
  } else {
    writtenText += event.key;
    colorCorrect(correctCheck(writtenText, mainText), writtenText);
    cursorMenager(writtenText);
  }
});

document.addEventListener("keydown", function (event) {
  if (event.key === "Backspace") {
    writtenText = writtenText.slice(0, -1);
    colorCorrect(correctCheck(writtenText, mainText), writtenText);
    cursorMenager(writtenText);
  }
});

function correctCheck(textW, textM) {
  let temp = [];
  for (let i = 0; i < textM.length; i++) {
    if (textM[i] === textW[i]) {
      temp.push(1);
    } else {
      temp.push(0);
    }
  }
  return temp;
}

function textPrepare(text) {
  let output = "";
  for (let i = 0; i < text.length; i++) {
    output += "<span id=" + "letter" + i + ">" + text[i] + "</span>";
  }
  return output;
}

function colorCorrect(list, textW) {
  for (let i = 0; i < textW.length; i++) {
    const letter = document.getElementById("letter" + i);
    if (list[i] == 1) {
      letter.style.color = "green";
    } else {
      letter.style.color = "red";
    }
  }
}

function cursorMenager(textW) {
  const cursor = document.querySelector(".cursor");
  cursor.style.display = "block";
  const currLetter = document
    .getElementById("letter" + textW.length)
    .getBoundingClientRect();
  let position = [currLetter.left, currLetter.top];
  cursor.style.left = `${position[0]}px`;
  cursor.style.top = `${position[1]}px`;
}
