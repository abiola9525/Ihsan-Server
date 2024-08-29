from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from school.models import Course, Module, Topic, Quiz, Question, Answer, PaymentTransaction, UserModuleScore
from school.serializers import CourseSerializer, ModuleSerializer, TopicSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, PaymentTransactionSerializer, UserModuleScoreSerializer

# Course Views
@api_view(['GET', 'POST'])
def course_list_create(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({"message": "Courses retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create course", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response({"message": "Course retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Course updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update course", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Module Views
@api_view(['GET', 'POST'])
def module_list_create(request):
    if request.method == 'GET':
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response({"message": "Modules retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Module created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create module", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def module_detail(request, pk):
    try:
        module = Module.objects.get(pk=pk)
    except Module.DoesNotExist:
        return Response({"message": "Module not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ModuleSerializer(module)
        return Response({"message": "Module retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Module updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update module", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        module.delete()
        return Response({"message": "Module deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Topic Views
@api_view(['GET', 'POST'])
def topic_list_create(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response({"message": "Topics retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Topic created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create topic", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response({"message": "Topic not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response({"message": "Topic retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Topic updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update topic", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return Response({"message": "Topic deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Quiz Views
@api_view(['GET', 'POST'])
def quiz_list_create(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response({"message": "Quizzes retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Quiz created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create quiz", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def quiz_detail(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
    except Quiz.DoesNotExist:
        return Response({"message": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response({"message": "Quiz retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Quiz updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update quiz", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        quiz.delete()
        return Response({"message": "Quiz deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Question Views
@api_view(['GET', 'POST'])
def question_list_create(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"message": "Questions retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Question created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create question", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({"message": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response({"message": "Question retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Question updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update question", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response({"message": "Question deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Answer Views
@api_view(['GET', 'POST'])
def answer_list_create(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response({"message": "List of all answers", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Answer created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create answer", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def answer_detail(request, pk):
    try:
        answer = Answer.objects.get(pk=pk)
    except Answer.DoesNotExist:
        return Response({"message": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return Response({"message": "Answer retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Answer updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update answer", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        answer.delete()
        return Response({"message": "Answer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#Score Views
@api_view(['GET', 'POST'])
def user_module_score_list_create(request):
    if request.method == 'GET':
        scores = UserModuleScore.objects.all()
        serializer = UserModuleScoreSerializer(scores, many=True)
        return Response({"message": "List of all user module scores", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UserModuleScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User module score created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create user module score", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_module_score_detail(request, pk):
    try:
        score = UserModuleScore.objects.get(pk=pk)
    except UserModuleScore.DoesNotExist:
        return Response({"message": "User module score not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserModuleScoreSerializer(score)
        return Response({"message": "User module score retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserModuleScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User module score updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update user module score", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        score.delete()
        return Response({"message": "User module score deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
# PaymentTransaction Views
@api_view(['GET', 'POST'])
def payment_transaction_list_create(request):
    if request.method == 'GET':
        payments = PaymentTransaction.objects.all()
        serializer = PaymentTransactionSerializer(payments, many=True)
        return Response({"message": "List of all payment transactions", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PaymentTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment transaction created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create payment transaction", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def payment_transaction_detail(request, pk):
    try:
        payment = PaymentTransaction.objects.get(pk=pk)
    except PaymentTransaction.DoesNotExist:
        return Response({"message": "Payment transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentTransactionSerializer(payment)
        return Response({"message": "Payment transaction retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = PaymentTransactionSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Payment transaction updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update payment transaction", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        payment.delete()
        return Response({"message": "Payment transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)