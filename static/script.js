window.onload = function () {
  //zimetUzCanva();
  //alert("Mans projekts!");
  var navLinks = document.querySelectorAll(".topnav a");
  console.log(navLinks);
  navLinks.forEach(function (link) {
    link.addEventListener("click", function (link) {
      navLinks.forEach(function (link) {
        link.classList.remove("active");
      });
      this.classList.add("active");
    });
  });
};

function atjaunotIetvaru(whitch) {
  document.getElementById("Lapas_saturs").innerHTML =
    "<" +
    'object id="lapas" type="text/html" data="' +
    whitch.href +
    '"></' +
    "object>";
}

function saskaitit() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);
  let z = x + y;
  if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž]*$/)) {
    alert("Ievadi vārdu ar burtiem!!!");
    return;
  }
  if (vards == "" || isNaN(x) || isNaN(y)) {
    console.log("Ievadi vertību!!!");
    alert("Visām vērtībām jābut ievadītām!!!");
  } else {
    console.log("Ievadītas vārds:" + vards);
    console.log("Pirmā vērtība:" + x);
    console.log("Otrā vērtība:" + y);
    console.log("Rezultāts:" + z);
    document.getElementById("rezultats").innerHTML =
      "<br><br><br>" + vards + ", Summa ir:" + z + "<br><br><br>";
    //alert("Rezultāts ir:" + z);
  }
}

function atnemt() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);
  let z = x - y;
  if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž]*$/)) {
    alert("Ievadi vārdu ar burtiem!!!");
    return;
  }
  if (vards == "" || isNaN(x) || isNaN(y)) {
    console.log("Ievadi vertību!!!");
    alert("Visām vērtībām jābut ievadītām!!!");
  } else {
    console.log("Ievadītas vārds:" + vards);
    console.log("Pirmā vērtība:" + x);
    console.log("Otrā vērtība:" + y);
    console.log("Rezultāts:" + z);
    document.getElementById("rezultats").innerHTML =
      "<br><br><br>" + vards + ", Starpība ir:" + z + "<br><br><br>";
    //alert("Rezultāts ir:" + z);
  }
}

function reizinat() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);
  let z = x * y;
  if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž]*$/)) {
    alert("Ievadi vārdu ar burtiem!!!");
    return;
  }
  if (vards == "" || isNaN(x) || isNaN(y)) {
    console.log("Ievadi vertību!!!");
    alert("Visām vērtībām jābut ievadītām!!!");
  } else {
    console.log("Ievadītas vārds:" + vards);
    console.log("Pirmā vērtība:" + x);
    console.log("Otrā vērtība:" + y);
    console.log("Rezultāts:" + z);
    document.getElementById("rezultats").innerHTML =
      "<br><br><br>" + vards + ", Reizinājums ir:" + z + "<br><br><br>";
    //alert("Rezultāts ir:" + z);
  }
}

function dalit() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);
  let z = x / y;
  if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž]*$/)) {
    alert("Ievadi vārdu ar burtiem!!!");
    return;
  }
  if (vards == "" || isNaN(x) || isNaN(y)) {
    console.log("Ievadi vertību!!!");
    alert("Visām vērtībām jābut ievadītām!!!");
  } else {
    console.log("Ievadītas vārds:" + vards);
    console.log("Pirmā vērtība:" + x);
    console.log("Otrā vērtība:" + y);
    console.log("Rezultāts:" + z);
    document.getElementById("rezultats").innerHTML =
      "<br><br><br>" + vards + ", Dalījums ir:" + z + "<br><br><br>";
    //alert("Rezultāts ir:" + z);
  }
}

//window.onload = function () {
//zimetuzcanva();
//alert('Mans projekts');
//};

function convertToCm() {
  const inches = document.getElementById("inchesInput").value;
  const cm = inches * 2.54; // Konvertācija
  const result = document.getElementById("result");
  result.textContent = `centimetros tas ir ${cm.toFixed(2)}`;
}

function downloadFile() {
  let datnesNosaukums = "rezultats.txt";
  let rezultats = document.getElementById("result").textContent;

  if (!rezultats) {
    alert("Lūdzu, vispirms konvertē vērtību!");
    return;
  }

  let blob = new Blob([rezultats], { type: "text/plain" });
  let saite = document.createElement("a");
  saite.href = URL.createObjectURL(blob);
  saite.download = datnesNosaukums;

  saite.style.display = "none";
  document.body.appendChild(saite);
  saite.click();
  document.body.removeChild(saite);
  URL.revokeObjectURL(saite.href);
}

function zimetuzcanva() {}

function taisnsturis() {
  const kanva = document.getElementById("zimejums"); //iegut kanvu pēc ID
  const konteksts = kanva.getContext("2d"); //iegut 2d zimējumu
  konteksts.fillStyle = "green";
  konteksts.fillRect(20, 20, 150, 100);

  //taisnstūris
  konteksts.strokeStyle = "yellow";
  konteksts.strokeRect(200, 20, 150, 200);
}

function aplis() {
  //aplis
  const kanva = document.getElementById("zimejums"); //iegut kanvu pēc ID
  const konteksts = kanva.getContext("2d"); //iegut 2d zimējumu
  konteksts.beginPath();
  konteksts.arc(100, 200, 50, 0, 2 * Math.PI);
  konteksts.fillStyle = "yellow";
  konteksts.fill();
  konteksts.lineWidth = 8;
  konteksts.strokeStyle = "white";
  konteksts.stroke();
}

function teksts() {
  const kanva = document.getElementById("zimejums"); //iegut kanvu pēc ID
  const konteksts = kanva.getContext("2d"); //iegut 2d zimējumu
  //izveidot tekstu
  konteksts.font = "40px Bebas Neue";
  konteksts.fillStyle = "red";
  konteksts.fillText("Sveicieni!!!!!", 500, 100);
}

function linija() {
  const kanva = document.getElementById("zimejums"); //iegut kanvu pēc ID
  const konteksts = kanva.getContext("2d"); //iegut 2d zimējumu
  //Izveidot līniju
  konteksts.beginPath();
  konteksts.moveTo(20, 300);
  konteksts.lineTo(500, 300);
  konteksts.lineWidth = 8;
  konteksts.strokeStyle = "blue";
  konteksts.stroke();
}

let age = 70;
console.log(age);
if (age < 18) {
  console.log("nepilngadīgs");
} else if (age >= 18 && age < 65) {
  console.log("pilngadīgs");
} else {
  console.log("Pensionārs");
}

for (let i = 0; i <= 10; i = i + 2) {
  if (i == 4 || i == 6) {
    console.log("For cikls ir uz" + i);
  } else {
    console.log(i);
  }
  //console.log(i);
}

let j = 0;
while (j <= 10) {
  console.log("while rezultāti" + j);
  j++;
}

let k = 1;
do {
  console.log("DO WHILE" + k);
  k++;
} while (k <= 10);

let skaitli = [6, 3, 0, 7, 4, 9, 2];

let summa = 0;
for (let i = 0; i < skaitli.length; i++) {
  summa = summa + skaitli[i];
  console.log(i + "vērtība = " + skaitli[i]);
}
console.log("Atbilde: " + summa);
console.log(skaitli);
