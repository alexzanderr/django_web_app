
console.log("index.js loaded")

let csrftoken = null;
$(document).ready(function () {
    // this is not document on load
    // keybindings
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    $(document).keypress(function (event) {
        // enter
        // https://stackoverflow.com/a/6542455/12172291
        if (event.which == 13) {
            console.log("just pressed enter")
            const textbox = $('#textbox')
            var textboxMessage = textbox.val()

            if (textboxMessage != "") {
                $.ajax({
                    type: "POST",
                    headers: { 'X-CSRFToken': csrftoken },
                    contentType: "application/json",
                    data: JSON.stringify({ "text": textboxMessage }),
                    dataType: "json",
                    url: "/todos/api/mongo/add",
                    // if this is wrong, then we do something about it
                    // url: "/todos/api/mongo/ad",
                    success: function (json_response) {
                        // here i should receive the oid from database
                        console.log(json_response)
                        console.log("new todo registered")
                        const todo_list = $("#todo-list")
                        todo_list.append(`
                                    <li class="todo-list-item" id="${json_response['oid']}">
                                        <button class="complete-todo-button" id="${json_response['oid']}" onclick="complete_todo_ajax(this.id)" style="width: 300px;">
                                            ${textboxMessage}
                                        </button>

                                        <button class="delete-todo-button" id="${json_response['oid']}" onclick="delete_todo_ajax(this.id)">
                                            delete
                                        </button>
                                    </li>`)
                    },
                    error: function () {
                        alert('some error occured. cant update UI')
                    }
                })
                textbox.val('');
            }
        }
    });
})

function ajax_request() {
    $.ajax({
        type: "GET",
        url: "/json",
        success: function (data) {
            console.log("got response")
            // var _json = $.parseJSON(data)
            $("#json-response").text(JSON.stringify(data))
        }
    })
}

window.addEventListener("offline",
    () => console.log("No Internet")
);

window.addEventListener("online",
    () => console.log("Connected Internet")
);

function complete_todo_ajax(oid) {
    console.log("time to complete something")
    $.ajax({
        type: "PATCH",
        headers: { 'X-CSRFToken': csrftoken },
        url: `/todos/api/mongo/complete`,
        data: JSON.stringify({ "oid": oid }),

        // if this is wrong, then we do something about it
        // url: "/todos/api/mongo/ad",
        success: function (json_response) {
            console.log(json_response)
            const complete_todo_button = $(`#${oid}.complete-todo-button`)

            if (json_response["completed"]) {
                // complete_todo_button.css({
                //  'text-decoration': 'line-through',
                //  "text-decoration-thickness": "2px"
                //  });
                // this is enough
                complete_todo_button.addClass("todo-completed")
            } else {
                // complete_todo_button.css({
                //  'text-decoration': 'none'
                //  });
                // this is enough
                complete_todo_button.removeClass("todo-completed")
            }
        },
        error: function () {
            alert('some error occured. cant update UI')
        }
    })
}

function delete_todo_ajax(oid) {
    console.log("time to delete something")
    $.ajax({
        type: "DELETE",
        headers: { 'X-CSRFToken': csrftoken },
        data: JSON.stringify({ "oid": oid }),
        url: `/todos/api/mongo/delete`,

        // if this is wrong, then we do something about it
        // url: "/todos/api/mongo/ad",
        success: function (json_response) {
            console.log(json_response)
            const todo_list_item = $(`#${oid}.todo-list-item`)
            console.log(`just deleted: ${todo_list_item.val()}`)
            todo_list_item.remove()
        },
        error: function () {
            alert('some error occured. cant update UI')
        }
    })
}

