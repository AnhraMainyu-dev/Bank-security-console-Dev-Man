import os
import django
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard

if __name__ == '__main__':
    active_passcard = Passcard.objects.filter(is_active=True)
    print('Количество пропусков:', Passcard.objects.count())
    print("Активных пропусков:", len(active_passcard))
