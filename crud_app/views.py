from django.shortcuts import render, redirect
from crud_app.models import Students


# Create your views here.
def INDEX(request):
    std = Students.objects.all()

    context = {
        'std': std
    }
    return render(request, 'index.html', context)


def ADD(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Gender = request.POST.get('Gender')
        Section = request.POST.get('Section')
        Roll_Number = request.POST.get('Roll_Number')
        Address = request.POST.get('Address')
        Phone = request.POST.get('Phone')

        std_add = Students(
            Name=Name,
            Email=Email,
            Gender=Gender,
            Section=Section,
            Roll_Number=Roll_Number,
            Address=Address,
            Phone=Phone,
        )

        std_add.save()
        return redirect('read')
    return render(request, 'index.html')


def EDIT(request):
    std = Students.objects.all()

    context = {
        'std': std,
    }
    return render(request, 'index.html', context)


def UPDATE(request, id):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Gender = request.POST.get('Gender')
        Section = request.POST.get('Section')
        Roll_Number = request.POST.get('Roll_Number')
        Address = request.POST.get('Address')
        Phone = request.POST.get('Phone')

        std_update = Students(
            id=id,
            Name=Name,
            Email=Email,
            Gender=Gender,
            Section=Section,
            Roll_Number=Roll_Number,
            Address=Address,
            Phone=Phone,
        )
        std_update.save()
        return redirect("read")

    return render(request, 'index.html')

#Delete Section
def DELETE(request, id):
    std = Students.objects.filter(id = id)
    std.delete()

    context = {
        'std':std,
    }

    return redirect('read')
