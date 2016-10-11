"""
Lambda example with external dependency
"""

import logging
from subprocess import call


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    """
    Lambda handler
    """
    logger.info("%s - %s", event, context)

    call(["python", "Scout2.py", "--force"])

    return event
