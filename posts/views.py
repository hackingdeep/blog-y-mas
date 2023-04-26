from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,PostView,Like,Comment,FollowersCount
from users.models import User
from django.utils.decorators import method_decorator
from .form import PostForm,CommentForm
from django.contrib.auth.decorators import login_required





@login_required(login_url='/users/login')
def home(request):
    post_list = Post.objects.all()
    return render(request,'posts/list_post.html',{'post_list':post_list})




def post_following(request):
    user = request.user
    users_followed = [follow.seguidor for follow in user.seguidores.all()]
    posts = Post.objects.filter(author__in=users_followed)
    print(users_followed)
    context = {'publicaciones':posts}
    return render(request,'posts/post_following.html',context)

class PostListView(ListView):
    model = Post



@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


    def post(self,*args,**kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid:
            post = self.get_object()
            comment = form.save(commit=False)
            comment.user  = self.request.user
            comment.post = post
            comment.save() 

            
            return redirect('detail',slug=post.slug,)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form':CommentForm()
        })
        return context
    
    def get_object(self,**kwargs):
        object = super().get_object(**kwargs)
        PostView.objects.get_or_create(user=self.request.user,post=object)
        return object

@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
  
    template_name = 'posts/post_create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context

@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
  
    template_name = 'posts/post_create.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context


@method_decorator(login_required(login_url='/users/login'), name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
 




@login_required(login_url='/users/login')
def like(request,slug):
    post = get_object_or_404(Post,slug=slug)
    like_qs = Like.objects.filter(user=request.user,post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail',slug=slug)
    else:
        Like.objects.create(user=request.user,post=post)
        return redirect('/')



def followers(request,id):

    followinsg_users = User.objects.get(id=id)
    print(followinsg_users)
    follower = FollowersCount.objects.filter(seguidor=request.user,siguiendo_a=followinsg_users)
    if follower.exists():
        follower[0].delete()
        return redirect('users:perfil',id=id)
    else:
        FollowersCount.objects.create(seguidor=request.user,siguiendo_a=followinsg_users)
        return redirect('users:perfil',id=id)
