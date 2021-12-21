// document ready is when you load the html file
// on your browser
$(document).ready(function () {

    var socket = io.connect('http://localhost:9999');
    var current_username = undefined;

    socket.on('connect', function () {
        socket.emit("logmein", "hello")
    });

    socket.on("usertype", function (message) {
        current_username = message
        if (current_username !== undefined) {
            document.title = `${current_username}`
        }
    })

    socket.on('message', function (msg) {
        var message = `${current_username}: ${msg}`
        $("#messages").append('<li>' + message + '</li>');

        console.log('Received message');
    });




    var sendButton = document.getElementById("sendbutton")
    sendButton.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            var textboxMessage = $('#myMessage').val()
            if (textboxMessage != "") {
                socket.send(textboxMessage);
                $('#myMessage').val('');
            } else {
                alert("message cannot be empty")
            }
        }
    })

    function send_message_to_all() {
        var textboxMessage = $('#myMessage').val()
        if (textboxMessage != "") {
            socket.send(textboxMessage);
            $('#myMessage').val('');
        } else {
            alert("invalid message")
            $('#myMessage').val('');
        }
    }

    $('#sendbutton').on('click', function () {
        send_message_to_all()
    });

    // keybindings
    $(document).keypress(function (e) {
        // enter
        // https://stackoverflow.com/a/6542455/12172291
        if (e.which == 13) {
            console.log("im working")
            var textboxMessage = $('#myMessage').val()
            if (textboxMessage != "") {
                socket.send(textboxMessage);
                $('#myMessage').val('');
            } else {
                alert("invalid message")
                $('#myMessage').val('');
            }
        }
        console.log("im not working")
    });
});
