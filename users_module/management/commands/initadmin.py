import logging
import os

from django.core.management.base import BaseCommand

from users_module.models import User
from youtube_module.models import YoutubeAPIToken

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASS = os.getenv("ADMIN_PASS")


class Command(BaseCommand):

    def handle(self, *args, **options):
        if YoutubeAPIToken.objects.count() == 0:
            YoutubeAPIToken.objects.create(
                token=os.environ.get('YOUTUBE_API_TOKEN'),
                active=True
            )
        if User.objects.count() == 0:
            User.objects.create_superuser(
                email=ADMIN_EMAIL,
                password=ADMIN_PASS
            )
            logger.info(f"Admin User created with email: {ADMIN_EMAIL}")
        else:
            logger.info("Admin user can only be created when there are no existing users")
