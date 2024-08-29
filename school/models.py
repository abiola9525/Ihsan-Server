from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import cloudinary
from account.models import User
from cloudinary.models import CloudinaryField
   
        
class Course(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    img = CloudinaryField('img', blank=True, null=True)
    metades = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    rating = models.FloatField()
    free_course_link = models.URLField(("Free course link"), max_length=500, blank=True, null=True)
    duration = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        # Upload img to Cloudinary if it's not already uploaded or if it's changed
        if self.img and hasattr(self.img, 'read'):
            result = cloudinary.uploader.upload(self.img)
            self.img = result['url']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    is_last_module = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'title']

    def __str__(self):
        return f'{self.title} ({self.course.title})'


class Topic(models.Model):
    module = models.ForeignKey(Module, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Quiz(models.Model):
    module = models.OneToOneField(Module, related_name='quiz', on_delete=models.CASCADE)
    passing_score = models.FloatField(default=70.0)

    def __str__(self):
        return f"Quiz for {self.module.title}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = RichTextField()

    def __str__(self):
        return f"{self.question_text} ({self.quiz.module.course.title} - {self.quiz.module.title})"


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = RichTextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

class UserModuleScore(models.Model):
    user = models.ForeignKey(User, related_name='module_scores', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='user_scores', on_delete=models.CASCADE)
    module = models.ForeignKey(Module, related_name='user_scores', on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user.email}'s score in {self.module.title} ({self.course.title})"


class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='payments', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # You may need to add more fields depending on your requirements

    # Additional fields as per your requirement

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"