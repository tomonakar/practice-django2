from django.contrib import admin
from .models import Choice, Question


# admin.StackedInlineは積み重ねて表示
# admin.TabularInlineは一行で表示
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # inles リストでクラスを追加すると外部キーでリレーションを貼ったオブジェクトを
    # 同じ画面で追加できるようになる
    inlines = [ChoiceInline]
    # 表示項目を編集
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # フィルタ機能を追加
    list_filter = ['pub_date']
    # 検索機能を追加
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
