function saskaitit() {
  let vards = document.getElementById('vards').value;
  let x = parseInt(document.getElementById('x').value);
  let y = parseInt(document.getElementById('y').value);
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
  document.getElementById("rezultats").innerHTML = "<br><br><br>" + vards + ", Summa ir:" + z + "<br><br><br>";
  //alert("Rezultāts ir:" + z);
  }
}

function atnemt() {
  let vards = document.getElementById('vards').value;
  let x = parseInt(document.getElementById('x').value);
  let y = parseInt(document.getElementById('y').value);
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
  document.getElementById("rezultats").innerHTML = "<br><br><br>" + vards + ", Starpība ir:" + z + "<br><br><br>";
  //alert("Rezultāts ir:" + z);
  }
}

function reizinat() {
  let vards = document.getElementById('vards').value;
  let x = parseInt(document.getElementById('x').value);
  let y = parseInt(document.getElementById('y').value);
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
  document.getElementById("rezultats").innerHTML = "<br><br><br>" + vards + ", Reizinājums ir:" + z + "<br><br><br>";
  //alert("Rezultāts ir:" + z);
  }
}

function dalit() {
  let vards = document.getElementById('vards').value;
  let x = parseInt(document.getElementById('x').value);
  let y = parseInt(document.getElementById('y').value);
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
  document.getElementById("rezultats").innerHTML = "<br><br><br>" + vards + ", Dalījums ir:" + z + "<br><br><br>";
  //alert("Rezultāts ir:" + z);
  }
}

window.onload = function() {
  zimetuzcanva();
  //alert('Mans projekts');
}

function zimetuzcanva() {
  
}

function taisnsturis() {
const kanva = document.getElementById('zimejums'); //iegut kanvu pēc ID
  const konteksts = kanva.getContext('2d'); //iegut 2d zimējumu
  konteksts.fillStyle = "green";
  konteksts.fillRect(20, 20, 150, 100);
  
  //taisnstūris
  konteksts.strokeStyle = "yellow";
  konteksts.strokeRect(200, 20, 150, 200);
}

function aplis() {
  //aplis
  const kanva = document.getElementById('zimejums'); //iegut kanvu pēc ID
  const konteksts = kanva.getContext('2d'); //iegut 2d zimējumu
  konteksts.beginPath();
  konteksts.arc(100, 200, 50, 0, 2 * Math.PI);
  konteksts.fillStyle = "yellow";
  konteksts.fill();
  konteksts.lineWidth = 8;
  konteksts.strokeStyle = "white";
  konteksts.stroke();
}

function teksts() {
  const kanva = document.getElementById('zimejums'); //iegut kanvu pēc ID
  const konteksts = kanva.getContext('2d'); //iegut 2d zimējumu
  //izveidot tekstu
  konteksts.font = "40px Bebas Neue"
  konteksts.fillStyle = "red";
  konteksts.fillText("Sveicieni!!!!!", 500, 100);
}

function linija() {
  const kanva = document.getElementById('zimejums'); //iegut kanvu pēc ID
  const konteksts = kanva.getContext('2d'); //iegut 2d zimējumu
  //Izveidot līniju
  konteksts.beginPath();
  konteksts.moveTo(20,300);
  konteksts.lineTo (500, 300);
  konteksts.lineWidth = 8;
  konteksts.strokeStyle = "blue";
  konteksts.stroke();
}


