let csrftoken = null;
$(document).ready(function () {
    csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    // this is not document on load
    // keybindings
    $(document).keypress(function (event) {
        // enter
        // https://stackoverflow.com/a/6542455/12172291
        if (event.which == 13) {
            create_new_account()
        }
    });
})


function create_new_account() {
    const username_input = $('#username')
    const username_small = $("#username_small")

    const email_input = $('#email')
    const email_small = $("#email_small")

    const password_input = $('#password')
    const password_small = $('#password_small')

    const password_check_input = $("#password_check")
    const password_check_small = $("#password_check_small")

    const remember_me_checkbox = $("#remember-me")

    const ui_controller = {
        "username": {
            "input": username_input,
            "small": username_small
        },
        "email": {
            "input": email_input,
            "small": email_small
        },
        "password": {
            "input": password_input,
            "small": password_small
        },
        "password_check": {
            "input": password_check_input,
            "small": password_check_small
        }
    }
    // console.log("creating new account ...")
    // console.log("just pressed enter")

    const username = username_input.val()
    const email = email_input.val()
    const password = password_input.val()
    const password_check = password_check_input.val()
    const remember_me = remember_me_checkbox.is(":checked")

    payload = {
        "username": username,
        "email": email,
        "password": password,
        "password_check": password_check,
        "remember_me": remember_me
    }

    let has_empty = false;
    for (var key in payload) {
        console.log(key)
        if (key == "remember_me") {
            continue
        }
        if (payload[key] == "") {
            has_empty = true;
            ui_controller[key]["input"].css({ "border-color": "#e74c3c" })
            ui_controller[key]["small"].text("field cannot be empty")
            ui_controller[key]["small"].css({ "visibility": "visible" })
        } else {
            ui_controller[key]["small"].css({ "visibility": "hidden" })
            ui_controller[key]["input"].css({ "border-color": "#2ecc71" })
        }
    }

    if (has_empty) {
        console.log("input cannot be empty")
        return
    }

    // console.log(payload)

    $.ajax({
        type: "POST",
        headers: { 'X-CSRFToken': csrftoken },
        contentType: "application/json",
        data: JSON.stringify(payload),
        dataType: "json",
        url: "/todos/api/register/validation",
        // if this is wrong, then we do something about it
        // url: "/todos/api/mongo/ad",
        success: function (json_response) {
            // here i should receive the oid from database
            console.log(json_response)

            let has_errors = false
            for (var key in json_response) {
                if (key == "register_token") {
                    continue
                }
                if (json_response[key]["passed"] === false) {
                    has_errors = true
                    // 4jvndu__!@#qmgh49195AND
                    ui_controller[key]["input"].css({ "border-color": "#e74c3c" })
                    ui_controller[key]["small"].text(json_response[key]["error_message"])
                    ui_controller[key]["small"].css({ "visibility": "visible" })
                } else {
                    ui_controller[key]["small"].css({ "visibility": "hidden" })
                    ui_controller[key]["input"].css({ "border-color": "#2ecc71" })
                }
            }

            if (has_errors) {
                return;
            }

            payload["register_token"] = json_response["register_token"]

            $.ajax({
                type: "POST",
                headers: { 'X-CSRFToken': csrftoken },
                contentType: "application/json",
                data: JSON.stringify(payload),
                dataType: "json",
                url: "/todos/register",
                // if this is wrong, then we do something about it
                // url: "/todos/api/mongo/ad",
                success: function (data) {
                    console.log("account created with success :)")
                    username_input.val("")
                    email_input.val("")
                    password_input.val("")
                    password_check_input.val("")
                    remember_me_checkbox.val("")
                    if (data.redirectTo) {
                        // data.redirect contains the string URL to redirect to
                        window.location.href = data.redirectTo;
                    } else {
                        console.log("there is not redirect")
                    }
                },
                error: function (error) {
                    console.log(error)
                    alert('error from server')
                }
            })


        },
        error: function () {
            alert('some error occured. cant update UI')
        }
    })
}

function check_username_real_time() {
    const username_input = $('#username')
    const username_small = $("#username_small")

    const payload = {
        "username": username_input.val()
    }
    $.ajax({
        type: "POST",
        headers: { 'X-CSRFToken': csrftoken },
        contentType: "application/json",
        data: JSON.stringify(payload),
        dataType: "json",
        url: "/todos/api/register/validation/username",
        // if this is wrong, then we do something about it
        // url: "/todos/api/mongo/ad",
        success: function (json_response) {
            // here i should receive the oid from database
            console.log(json_response)

            if (json_response["username"]["passed"] === false) {
                username_input.css({ "border-color": "#e74c3c" })
                username_small.text(json_response["username"]["error_message"])
                username_small.css({ "visibility": "visible" })
            } else {
                username_small.css({ "visibility": "hidden" })
                username_input.css({ "border-color": "#2ecc71" })
            }
        },
        error: function () {
            alert('some error occured. cant update UI')
        }
    })
}

function generate_random_password() {
    const random_password_button = $('#random_password_button')
    const password_input = $('#password')
    const password_check_input = $("#password_check")


    $.ajax({
        type: "GET",
        headers: { 'X-CSRFToken': csrftoken },
        url: "/todos/api/register/random/password",
        // if this is wrong, then we do something about it
        // url: "/todos/api/mongo/ad",
        success: function (json_response) {
            // here i should receive the oid from database
            console.log(json_response)

            const _random_password = json_response["random_password"]
            console.log(_random_password)
            password_input.val(_random_password)
            password_check_input.val(_random_password)
        },
        error: function () {
            alert('some error occured. cant update UI')
        }
    })
}