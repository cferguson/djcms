from django.core.management.base import BaseCommand, CommandError

from articles.models import Article


class Command(BaseCommand):
    help = 'Loads a set of random articles to for testing'

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int)

    def handle(self, *args, **options):
        pass