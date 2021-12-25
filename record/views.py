from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import os


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        user_object = User.objects.filter(email=email).count()
        if user_object > 0:
            messages.success(request, 'Email already exists')
            return redirect(request.META.get('HTTP_REFERER'))
        gender = request.POST['gender']
        country = request.POST['country']
        language = request.POST.getlist('language')
        language_list = ','.join(map(str, language))
        image = ''
        if request.FILES:
            image = request.FILES['image']

        obj = User.objects.create(name=name, email=email, gender=gender,
                                  language=language_list, country=country, image=image
                                  )
        obj.save()
        messages.success(request, "Data was inserted")
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        content = {
            'userData': User.objects.all()
        }
        return render(request, 'index.html', content)


def delete_file(id):
    user_object = User.objects.get(id=id)
    if user_object.image:
        file_path = user_object.image.url
        path_dir = os.getcwd() + file_path
        if os.path.exists(path_dir):
            os.remove(path_dir)
            return True
        else:
            return True
    else:
        return True


def delete(request, id):
    if delete_file(id) and User.objects.get(id=id).delete():
        messages.success(request, "data was deleted")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, "data was not deleted")
        return redirect(request.META.get('HTTP_REFERER'))


def edit(request, id):
    if request.method == "POST":
        user_obj = User.objects.get(id=id)
        user_obj.name = request.POST['name']
        user_obj.email = request.POST['email']
        user_obj.gender = request.POST['gender']
        user_obj.country = request.POST['country']
        language = request.POST.getlist('language')
        user_obj.language = ','.join(map(str, language))
        image = ''
        if request.FILES:
            delete_file(id)
            user_obj.image = request.FILES['image']

        user_obj.save()
        messages.success(request, "Data was updated")
        return redirect('/')
    else:
        content = {
            'userData': User.objects.get(id=id)
        }
        return render(request, 'update.html', content)
