
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bidding_app.decorators import check_group_permission
from bidding_app import services


@login_required
def get_bidding_list(request):
    data = services.get_bidding_item_list()
    return render(request, 'index.html', data)


@check_group_permission('Admin')
@login_required
def get_bidding_details(request, id):
    service_obj = services.get_bidding_service(id)
    data = services.get_service_bidding_details(service_obj)
    context = {'vendors': data, 'service_name': service_obj.name}
    template_page = 'services_bidding_detail.html'
    return render(request, template_page, context)


@login_required
def get_bidding_page(request, id):
    vendor = services.user_done_bidding(request.user, id)
    context = {'vendor': vendor}
    template_page = 'bidding_page.html'
    return render(request, template_page, context)


@login_required
def bidding(request):
    user = request.user
    parameter_dict = request.POST
    response = services.user_bidding(user, parameter_dict)
    return redirect('/')
