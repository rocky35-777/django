from django.contrib import admin
from .models import Board
# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'date', 'likes', "content", "updated_at", "created_at") #항목리스트
    list_filter = ('date', 'writer', 'updated_at') #필터기능
    search_fields = ('title', 'content') #검색기능
    ordering = ('-date',) # -date 는 역순으로 정렬
    readonly_fields = ('writer',)
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('추가옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    ) #상세페이지에서 쉽게 볼 수 있는 옵션
    list_per_page = 1
    actions = ('increment_likes',)

    def increment_likes(self, request, queryset):
        # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
        for board in queryset:
            board.likes += 1
            board.save()
    increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"
