

from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.http import HttpRequest

#
from django.core.management import call_command
from django_extensions.management.commands.show_urls import Command as ShowUrlsCommand
from django.urls import get_resolver

from views_decorators import json_response_decorator


# root
# /
def index(request):
    return application_routes(request)
    # return render(
    #   request,
    #   "base_index.html",
    #   { "person": "Andrew" }
    # )


import re
ansi_escape_regex = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def delete_ansi_escape(string):
    string = str(string)
    return ansi_escape_regex.sub("", string)


def get_all_routes_json() -> list:
    output = call_command(ShowUrlsCommand())
    routes = []
    lines = output.split("\n")
    for line in lines:
        # print(line)
        route_list = line.split()
        if route_list == []:
            continue

        route = delete_ansi_escape(route_list[0]).strip()
        view_func_name = delete_ansi_escape(route_list[1]).strip()
        name = delete_ansi_escape(route_list[2]).strip()
        # print(route)
        routes.append({
            "route": route,
            "view": view_func_name,
            "name": name
        })
    return routes

# /routes


def application_routes(request: HttpRequest):
    output = call_command(ShowUrlsCommand())
    routes = []
    lines = output.split("\n")
    for line in lines:
        # print(line)
        route = line.split()
        if route == []:
            continue

        route = delete_ansi_escape(route[0]).strip()
        # print(route)
        routes.append(route)

    return render(request, "index_routes.html", {
        "routes": routes
    })

# /routes/json


def application_routes_json(request):
    return json_response({
        "routes": get_all_routes_json()
    })


def context_menu_index(request):
    return render(
        request,
        "context_menu.html")


@json_response_decorator
def test_decorator(request):
    return {"data": 123}, 403


@json_response_decorator
def test_decorator2(request):
    return {"data": 123}



from ipware import get_client_ip

banned_ips_list = [
    "127.0.0.1"
]

@json_response_decorator
def test_ip(request):
    # In a view or a middleware where the `request` object is available

    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        return {
            "m": "Unable to get the client's IP address",
            "is_routable": is_routable
        }
    else:
        if client_ip in banned_ips_list:
            return {
                "message": "your ip address is banned, sorry"
            }, 403

        if client_ip == "127.0.0.1":
            return {
                "m": "your ip address is localhost"
            }
        # We got the client's IP address
        if is_routable:
            # The client's IP address is publicly routable on the Internet
            return {
                "m": "# The client's IP address is publicly routable on the Internet: meaning that the ip is from outside local network (internet)",
                "ip": client_ip
            }
        else:
            # adica este din local network
            return {
                "m": "The client's IP address is private: meaning that ip is from local network",
                "ip": client_ip
            }

    # Order of precedence is (Public, Private, Loopback, None)
