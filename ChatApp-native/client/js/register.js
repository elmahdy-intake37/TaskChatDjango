let ws = new WebSocket("ws://127.0.0.1:5678/"),

  register = document.getElementById("register"),
  UserName = document.getElementById('username'),
  email = document.getElementById("email"),
  pass = document.getElementById("pass"),
  PassConfirm = document.getElementById('confirm')

ws.onopen = function(event) {
  register.addEventListener("submit", function(e) {
    e.preventDefault();
    register = {
      user_name: UserName.value,
      email: email.value,
      pass: pass.value,
      reg: "reg"
    };
    window.location.href=('chat.html');
    ws.send(JSON.stringify(register));
  })
};
