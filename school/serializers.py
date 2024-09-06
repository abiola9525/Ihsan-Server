from rest_framework import serializers
from school.models import Course, Module, Topic, Quiz, Question, Answer, PaymentTransaction, UserModuleScore
from account.models import User

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'created_at', 'modified_at']

class ModuleSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'description', 'is_last_module', 'created_at', 'modified_at', 'topics']

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'img', 'metades', 'price', 'rating', 'free_course_link', 'duration', 'description', 'created_at', 'modified_at', 'modules']
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text', 'answers']
        
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'module', 'passing_score', 'questions']
        
class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'
        
class UserModuleScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModuleScore
        fields = '__all__'