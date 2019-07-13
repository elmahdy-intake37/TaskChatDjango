let ws = new WebSocket("ws://127.0.0.1:5678/"),
  chat = document.getElementById("chat");
messages = document.createElement("ul");

ws.onopen = function(event) {
  document.getElementById("chatform").addEventListener("submit", function(e) {
    e.preventDefault();
    let para = document.createElement("P");
    let t = document.createTextNode(chat.value);
    para.appendChild(t);
    document.getElementById("chatview").appendChild(para);
    ws.send(chat.value, "chat");
  });
};

ws.onmessage = function(event) {
  let messages = document.getElementsByTagName("ul")[0],
    message = document.createElement("li"),
    content = document.createTextNode(event.data);
    console.log(event.data);
  message.appendChild(content);
  messages.appendChild(message);
};
document.body.appendChild(messages);
