import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.redis import RedisIntegration


def setup_sentry(app):
    sentry_logging = LoggingIntegration(
        level=logging.INFO,  # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    )

    sentry_sdk.init(
        environment=app.config['NAME'],
        dsn="https://7d5cd2bf472f46018ebd9f8ac9d25ce0@o409291.ingest.sentry.io/5281468",
        integrations=[sentry_logging, FlaskIntegration(), CeleryIntegration(), RedisIntegration()]
    )