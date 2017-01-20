from django.core.management.base import BaseCommand, CommandError

from shortener.models import KirrURL




class Command(BaseCommand):
    help = 'Refreshes all URL short codes'

   # def add_arguments(self, parser):
   #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
		return KirrURL.objects.refresh_shortcodes()
       