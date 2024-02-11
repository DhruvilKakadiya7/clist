#!/usr/bin/env python3

from functools import partial

from django.contrib import messages


class RequestLogger:

    def __init__(self, request):
        self.request_ = request

    def __getattr__(self, attr):
        ret = getattr(messages, attr)
        if callable(ret):
            ret = partial(ret, self.request_)
        return ret


def get_filtered_list(request, field, options=None):
    return [
        option
        for option in request.GET.getlist(field)
        if options is not None and option in options or options is None and option
    ]


def get_filtered_value(request, field, options=None):
    ret = get_filtered_list(request, field, options)
    return ret[-1] if ret else None


def custom_request(request):
    setattr(request, 'logger', RequestLogger(request))
    setattr(request, 'get_filtered_list', partial(get_filtered_list, request))
    setattr(request, 'get_filtered_value', partial(get_filtered_value, request))
    return request
