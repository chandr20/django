from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm,RestaurantLocationCreateForm
# Create your views here.
# function based view
from .forms import RestaurantCreateForm
#
# @login_required()
# def Restaurant_Createview(request):
#     form = RestaurantLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         if request.user.is_authenticated():
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#             return HttpResponseRedirect("/restaurants/")
#         else:
#             return HttpResponseRedirect("/login/")
#     if form.errors:
#         errors = form.errors
#     template_name = 'restaurants/form.html'
#     context = {"form": form ,"errors": errors}
#     return render(request,template_name,context)




# def restaurant_listview(request):
#     template_name = 'restaurants/restaurants_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "object_list": queryset
#     }
#     return render(request,template_name,context)



class RestaurantListview(LoginRequiredMixin,ListView):
    template_name = 'restaurants/restaurants_list.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailedView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)



class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    # login_url = '/login/'
    template_name = 'form.html'
    # success_url = "/restaurants/"

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestaurantLocationCreateForm
    # login_url = '/login/'
    template_name = 'restaurants/detail-update.html'
    # success_url = "/restaurants/"

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantUpdateView,self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f'Update restaurant: {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
















