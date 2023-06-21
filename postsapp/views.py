from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, TemplateView
from .models import Post, Response
from datetime import datetime
from .filters import PostFilter, ResponseFilter
# from .forms import PostForm
from .forms import PostForm, ResponseForm
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.core.mail.message import EmailMultiAlternatives

# Create your views here.
class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-dataCreation']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра в posts.html
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostsDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form_class = ResponseForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST
    success_url = '/posts/'
    ordering = ['-dataCreation']
    paginate_by = 4

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        responses = Response.objects.filter(postsResponse=post)
        context['form'] = ResponseForm()
        context['responses'] = responses
        return context

    def post(self, request, *args, **kwargs):
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.userResponse = request.user
            response.postsResponse = self.get_object()
            response.save()
        return redirect('post', pk=self.get_object().pk)


class PostsSearchView(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'search.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    ordering = ['-dataCreation']
    paginate_by = 6

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class PostsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'create.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST
    success_url = '/posts/'
    permission_required = ('postsapp.add_post')

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        # publications = Post.objects.filter(author=Author.objects.get(authorUser=author))\
        #     .filter(dataCreation__date=date.today())
        # if publications.count() >= 3:
        #     return render(request, 'manyposts.html')

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            # print(form.cleaned_data)  # Выводит значения формы для отладки
            post = form.save(commit=False)
            post.user = self.request.user
            form.save()
            return redirect(self.success_url)

        return super().get(request, *args, **kwargs)


# class PostsEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class PostsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    form_class = PostForm
    success_url = '/posts/'
    permission_required = ('postsapp.change_post')

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostsDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        posts = Post.objects.filter(user=user)  # Получение всех постов пользователя
        responses = Response.objects.filter(postsResponse__in=posts)  # Получение всех откликов на посты пользователя
        context['responses'] = responses
        context['response_filter'] = ResponseFilter(self.request.GET, queryset=responses)  # вписываем наш фильтр в контекст
        return context


@login_required
def accept_response(request, pk):
    response = get_object_or_404(Response, pk=pk)

    if request.user == response.postsResponse.user: # Проверяем, что пользователь является владельцем объявления
        response.accepted = True
        response.save()

        subject = 'Response accepted'
        message = f'Ваш отклик на объявление "{response.postsResponse.title}" был принят.'
        from_email = 'newspaperss@yandex.ru'
        to_email = response.userResponse.email

        msg = EmailMultiAlternatives(subject, message, from_email, [to_email])
        msg.send()

    return redirect('profile')


@login_required
def delete_response(request, pk):
    response = get_object_or_404(Response, pk=pk)

    if request.user == response.postsResponse.user:
        response.delete()

    return redirect('profile')


