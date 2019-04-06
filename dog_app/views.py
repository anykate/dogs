# from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Dog
from .forms import DogForm


# Create your views here.
def index(request):
    form = DogForm()

    try:
        dogs = Dog.objects.all()
    except Dog.DoesNotExist:
        return redirect('/')

    return render(request, 'dog_app/index.html', {'dogs': dogs, 'form': form})


def create(request):
    if request.method == 'POST':
        form = DogForm(request.POST)

        if form.is_valid():
            new_dog = Dog(name=request.POST['name'],
                          breed=request.POST['breed'])
            new_dog.save()

    return redirect('/')


def edit(request, dog_id):
    try:
        dog = Dog.objects.get(id=dog_id)
    except Dog.DoesNotExist:
        return redirect('/')

    val = {'name': dog.name, 'breed': dog.breed}
    form = DogForm(val)
    return render(request, 'dog_app/edit.html', {'dog': dog, 'form': form})


def update(request, dog_id):
    if request.method == 'POST':
        try:
            dog = Dog.objects.get(id=dog_id)
        except Dog.DoesNotExist:
            return redirect('/')

        if dog:
            dog.name = request.POST['name']
            dog.breed = request.POST['breed']
            dog.save()

        else:
            return redirect('/')

    return redirect('/')


def delete(request, dog_id):
    if request.method == 'GET':
        try:
            dog = Dog.objects.get(id=dog_id)
        except Dog.DoesNotExist:
            return redirect('/')

        if dog:
            dog.delete()
        else:
            return redirect('/')

    return redirect('/')
