from django.shortcuts import render,redirect
from .models import Post,Comment
from django.contrib import messages

# Create your views here.
def blog(request):
    if request.user.is_superuser:
        allPosts=Post.objects.all()
    else:
        allPosts=Post.objects.filter(visibility=True)
    context={'allPosts': allPosts}
    return render(request, "blog/blog.html", context)

def BlogDashboard(request):
    if request.method == "POST" :
        return render(request, "blog/blogDashboard.html")
    if request.user.is_superuser:
        allPosts=Post.objects.all()
    else:
        allPosts=Post.objects.filter(visibility=True)
    context={'allPosts': allPosts,'data':'NewPost'}
    return render(request, "blog/blogDashboard.html",context)

def EditBlogPost(request,slug):
    return redirect(request.META.get('HTTP_REFERER'))

def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Post.objects.none()
        show=True
    else:
        allPostTitle= Post.objects.filter(title__icontains=query,visibility=True)
        allPostAuthor= Post.objects.filter(author__icontains=query)
        allPostContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostTitle.union(allPostContent, allPostAuthor)
    if allPosts.count()==0:
        show=True
    else:
        show=False
    params={'show':show,'allPosts':allPosts,'query':query}
    return render(request, 'blog/searchResults.html', params)

def blogPost(request, slug):
    post=Post.objects.filter(slug=slug,visibility=True).first()
    comments=Comment.objects.filter(post=post)
    if post:
        context={'post':post,'comments':comments}
        return render(request, "blog/blogPost.html",context)
    else:
        context={'error':'404'}
        return render(request, "newsite/error.html",context)

def postComment(request):
    if request.method == "POST":
        content=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        comment=Comment(content= content, user=user, post=post)
        comment.save()

    return redirect(request.META.get('HTTP_REFERER'))
    
def deleteComment(request):
    if request.method == "POST":
        postSno=request.POST.get('postSno')
        commentSno=request.POST.get('commentSno')
        post=Post.objects.get(sno=postSno)
        comment=Comment.objects.filter(post=post,sno=commentSno).first()
        comment.delete()
        
    return redirect(request.META.get('HTTP_REFERER'))