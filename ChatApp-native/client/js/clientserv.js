let ws = new WebSocket("ws://127.0.0.1:5678/"),
  UserName = document.getElementById('username'),
  email = document.getElementById("email"),
  pass = document.getElementById("pass");
ws.onopen = function(event) {
  document.getElementById("signin").addEventListener("submit", function(e) {
    e.preventDefault();
    login = {
      email: email.value,
      pass: pass.value
    };
    ws.send(JSON.stringify(login));
  });
};

ws.onmessage = function(event) {
  let status = event.data;
  if (status == 200) {
    window.location.href=('chat.html');
  } else {
    window.location.href=("register.html");
  }
};

// ws.onmessage = function(event) {
//   var messages = document.getElementsByTagName("ul")[0],
//     message = document.createElement("li"),
//     content = document.createTextNode(event.data);
//   message.appendChild(content);
//   messages.appendChild(message);
// };
// document.body.appendChild(messages);
