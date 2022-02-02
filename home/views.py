from django.shortcuts import render, redirect
from home.forms import AloqaForm
from home.models import Blog, Aloqa
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index/base.html')


def team(request):
    return render(request, 'team/base.html')


def services(request):
    return render(request, 'services/base.html')


def portfolio(request):
    return render(request, 'portfolio/base.html')


def about(request):
    return render(request, 'about/base.html')


def contact(request):
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            data = Aloqa()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Sizning xabaringiz qabul qilindi! Rahmat')
            return redirect('contact')
    form = AloqaForm
    context = {'form': form, }
    return render(request, 'contact/base.html', context)


def blogview(request):
    blog_latest = Blog.objects.all().order_by('-id')[:20]
    context = {
        'blog_latest': blog_latest,
    }
    return render(request, 'blog/base.html', context)


def blog_detail(request, id, slug):
    blog_latest = Blog.objects.all().order_by('-id')
    blog = Blog.objects.get(pk=id)
    context = {
        'blog': blog,
        'blog_latest': blog_latest,
    }
    return render(request, 'blog_details/base.html', context)
