#needs verify steps still? 
import logging
import time

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_wait_for_label')
    context.perform_gesture('tap', 'btn_template_matched')
    context.perform_gesture('tap', 'btn_open_slow_modal')
    time.sleep(40)
    context.perform_gesture('tap', 'btn_complete_job')
