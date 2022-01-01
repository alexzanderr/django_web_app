
import functools

from django.http import JsonResponse
from rest_framework.views import Response as JsonAPIResponse


class _json_response_decorator(object):
    def __init__(self, _django_view_func, rest_api=False) -> None:
        functools.update_wrapper(self, _django_view_func)

        self._django_view_func = _django_view_func
        self.rest_api = rest_api

        self._calls = 0


    def _json_response(self,
        remote_self, *args, **kwargs
    ):
        if remote_self:
            _returned = self._django_view_func(remote_self, *args, **kwargs)
        else:
            _returned = self._django_view_func(*args, **kwargs)


        _data = {}
        _status_code = 200

        if isinstance(_returned, tuple):
            def validate_and_update_data():
                nonlocal _data
                __data: dict = _returned[0]
                if not isinstance(__data, dict):
                    raise TypeError(f"data must be dict. your data: {__data}")

                _data = __data

            if len(_returned) == 1:
                validate_and_update_data()

            elif len(_returned) == 2:
                # here must be status code
                __status_code: int = _returned[1]
                if not isinstance(__status_code, (str, int)):
                    raise TypeError(f"status code must be integer or string. your status code: {__status_code}")

                if not (99 < __status_code < 513):
                    raise ValueError(f"status code must be between 100 and 512. your status code: {__status_code}")

                _status_code = __status_code
                del __status_code

                validate_and_update_data()
        else:
            # _returned is dict type
            _data = _returned
            del _returned

        if self.rest_api:
            # django func
            return JsonAPIResponse(data=_data, status=_status_code)

        # django func
        return JsonResponse(data=_data, status=_status_code)


    def __get__(self, remote_self, object_type=None):
        return functools.partial(self.__call__, remote_self)


    # inner wrapper
    def __call__(self, remote_self=None, *args, **kwargs):
        self._calls += 1
        return self._json_response(remote_self, *args, **kwargs)


    @property
    def calls(self):
        return self._calls


def json_response_decorator(
    _django_view_func=None, *args, **kwargs
):
    if _django_view_func:
        return _json_response_decorator(_django_view_func, rest_api=False)

    def inner_wrapper(_django_view_func):
        return _json_response_decorator(_django_view_func, rest_api=False, *args, **kwargs)
    return inner_wrapper


def json_api_response_decorator(
    _django_view_func=None, *args, **kwargs
):
    if _django_view_func:
        return _json_response_decorator(_django_view_func, rest_api=True)

    def inner_wrapper(_django_view_func):
        return _json_response_decorator(_django_view_func, rest_api=True, *args, **kwargs)
    return inner_wrapper
