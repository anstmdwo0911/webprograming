from django.shortcuts import render, redirect
from notion.models import Post

# def index(request):
#     latest_notion_list = Post.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_notion_list':latest_notion_list}
#     return render(request, 'notion/index.html',context)

def notion(request):
    p_list = Post.objects.all().order_by('-pub_date')
    return render(request, 'notion/notion.html', {'p_list': p_list})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'notion/post.html', {'post':post})

def create(request):
    if request.method == 'POST':
        if request.POST['name'] == '':
            return render(request, 'notion/create.html')
        else:
            post = Post()
            post.name = request.POST['name']
            post.text = request.POST['text']
            post.save()
            return redirect('/')
    return render(request, 'notion/create.html')

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'notion/delete.html', {'Post': post})

# def pw(request,pk):
#     post = Post.objects.get(pk=pk)
#     if request.method == 'POST':
#         if request.POST[pw] == post.pw:
#             return render(request, 'notion/post.html', {'post':post})
#         elif post.pw == None:
#             return render(request, 'notion/post.html', {'post':post})
#     return render(request, 'notion/pw.html', {'Post': post})
