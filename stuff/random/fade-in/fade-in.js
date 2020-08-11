var txt;

async function fadein() {
  document.getElementById('title').style.display = 'none';
  document.getElementById('background').style.display = 'block';
  document.getElementById('fadeintext').innerHTML = txt;
  document.getElementById('fadeintext').style.display = 'block';
  await sleep(500);
  document.getElementById('fadeintext').style.opacity = '1';
  document.getElementById('fadeintext').style.fontSize = '15em';
  await sleep(1000);
  document.getElementById('btn').style.top = '32px';
}

function input() {
  txt = document.getElementById('textinput').value;
  document.getElementById('textinput').style.display = 'none';
  fadein();
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function copy() {
  var copyText = `http://legendcow.com/stuff/random/fade?txt=${txt}`;
  navigator.clipboard.writeText(copyText);
  var copyAlert = document.getElementById('copyAlert');
  copyAlert.style.display = 'block';
  await sleep(100);
  copyAlert.style.opacity = '1';
}

function hide() {
  document.getElementById('copyAlert').style.opacity = '0';
}