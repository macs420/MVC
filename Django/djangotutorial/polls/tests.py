import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=old_time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        recent_time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=recent_time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Brak dostępnych pytań.")
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question("Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            ['Past question.'],
            transform=lambda q: q.question_text
        )

    def test_future_question(self):
        create_question("Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "Brak dostępnych pytań.")
        self.assertQuerySetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_question(self):
        create_question("Past question.", days=-30)
        create_question("Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            ['Past question.'],
            transform=lambda q: q.question_text
        )

    def test_two_past_questions(self):
        create_question("Past question 1.", days=-30)
        create_question("Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            ['Past question 2.', 'Past question 1.'],
            transform=lambda q: q.question_text
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question('Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question('Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
