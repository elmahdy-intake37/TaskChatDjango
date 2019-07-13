$(function() {
    // When we're using HTTPS, use WSS too.
    let ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

    let loadhistorysock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/loadhistory/");

    loadhistorysock.onmessage = function(message) {

        let data = JSON.parse(message.data);

        new_messages = data.messages

        last_id = data.previous_id

        if(last_id == -1){
            $("#load_old_messages").remove();
            $("#last_message_id").text(last_id)
            if(new_messages.length == 0){
                return;
            }
        }
        else{
            $("#last_message_id").text(last_id)
        }

        let chat = $("#chat")

        for(let i=new_messages.length - 1; i>=0; i--){
            let ele = $('<li class="list-group-item"></li>')

            ele.append(
                '<strong>'+new_messages[i]['user']+'</strong> : '
                )

            ele.append(
                new_messages[i]['message'])

            chat.prepend(ele)
        }

    };

    $("#load_old_messages").on("click", function(event) {
        let message = {
            last_message_id: $('#last_message_id').text()
        }
        loadhistorysock.send(JSON.stringify(message));
        return false;
    });
});
