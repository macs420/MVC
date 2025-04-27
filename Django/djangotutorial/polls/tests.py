
from django.test import TestCase
from django.urls import reverse
from .models import Question, Choice
from django.utils import timezone

class VotingTest(TestCase):
    def test_vote_on_question(self):
        question = Question.objects.create(question_text="What's new?", pub_date=timezone.now())
        choice = Choice.objects.create(question=question, choice_text="Not much", votes=0)

        response = self.client.post(reverse('polls:vote', args=(question.id,)), {'choice': choice.id})

        self.assertRedirects(response, reverse('polls:results', args=(question.id,)))
