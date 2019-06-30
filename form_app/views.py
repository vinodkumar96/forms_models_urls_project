from django.shortcuts import render
from django.http import HttpResponse
from .models import Name
from .forms import NameForm
# Create your views here.
def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            n=Name(first_name=form.cleaned_data['First_Name'],
                   last_name=form.cleaned_data['Last_Name'])
            n.save()
            return HttpResponse("Name Submitted Successfully")

    else:
        form=NameForm
        return render(request, 'input.html', {'form': form})