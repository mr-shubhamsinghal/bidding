from django.shortcuts import render


def check_group_permission(group_name):
    def wrap(desired_function):
        def wrapped_f(request, *args, **kwargs):
            user = request.user
            if user.groups.filter(name=group_name).count():
                # User belongs to the group
                response = desired_function(request, *args, **kwargs)
                return response
            else:
                return render(request, 'invalid_page.html')
        return wrapped_f
    return wrap
