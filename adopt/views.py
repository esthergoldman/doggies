from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from adopt.choices import sex_choices, color_choices, size_choices, area_choices



from .models import Pet

def adopt(request):
    pets = Pet.objects.order_by('-arrival_date').filter(is_published=True) #arrival_date from the model

    paginator = Paginator(pets,3) #show 3 pets per page
    page = request.GET.get('page')
    page_pets = paginator.get_page(page)
    
    context = {
        'pets': page_pets,
        'sex_choices': sex_choices,
        'color_choices': color_choices,
        'size_choices': size_choices,
        'area_choices': area_choices,
    }

    return render(request, 'adopt/adopt.html', context)


def pet(request, pet_id):
    one_pet = get_object_or_404(Pet, pk=pet_id) #check if exist or gives error

    context = {
        'one_pet': one_pet
    }

    return render(request, 'adopt/pet.html', context)


def search(request):
    queryset_list = Pet.objects.order_by('-arrival_date')

    #sex search
    if 'sex' in request.GET:
        sex = request.GET['sex']
        if sex != 'all':
            queryset_list = queryset_list.filter(sex__iexact=sex)

    #color search
    if 'color' in request.GET:
        color = request.GET['color']
        if color != 'all':
            queryset_list = queryset_list.filter(color__iexact=color)
   
    #size search
    if 'size' in request.GET:
        size = request.GET['size']
        if size != 'all':
            queryset_list = queryset_list.filter(size__iexact=size)
   
    #size search
    if 'area' in request.GET:
        area = request.GET['area']
        if area != 'all':
            queryset_list = queryset_list.filter(area__iexact=area)

    context = {
        'sex_choices': sex_choices,
        'color_choices': color_choices,
        'size_choices': size_choices,
        'area_choices': area_choices,
        'pets': queryset_list,
        'values': request.GET    
    }

    return render(request, 'adopt/search.html', context)


