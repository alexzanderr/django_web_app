"""
	this module is going to be used and usefull by all apps
"""


from django.http import JsonResponse


def json_response(_dict: dict, status_code=200):
	return JsonResponse(data=_dict, status=status_code)