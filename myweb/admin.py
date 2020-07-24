from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project
from .models import Post
from .models import Comment
from .models import Reply
from .models import Service

admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)

admin.site.site_header = "Dennis Portfolio"
admin.site.site_title = "My Portfolio"
