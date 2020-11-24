from django.contrib import admin
from notion.models import Post

admin.site.register(Post) # 관리자가 Post에 접근 가능할 수 있도록 한다.