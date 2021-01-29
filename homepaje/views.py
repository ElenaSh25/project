from django.http import HttpResponse
from posts.models import posts_db
from user.models import user_db


def index(request):
   for i in range(len(post_db)):

        title_form = (f' value="{posts_db[i]["title"]}">{icecream_db[i]["title"]}')
        body_form = (f' value="{posts_db[i]["body"]}">{icecream_db[i]["body"]}')

    for user in user_db:
        users += ( f' required value="{username}">{username}<br>')

    if request.method == 'POST':
        selected_user = request.POST['user']
        selected_title = request.POST['title_form']
        selected_body= request.POST['body_form']

    context = {
        'username': user,
        'title': title_form,
        'body': body_form,
    }
    return render(request, 'homepage/index.html', context)