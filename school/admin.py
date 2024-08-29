from django.contrib import admin
from .models import Course, Module, Topic, Quiz, Question, Answer, PaymentTransaction, UserModuleScore
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1

class ModuleAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.register(Course)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Topic)
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserModuleScore)
admin.site.register(PaymentTransaction)
