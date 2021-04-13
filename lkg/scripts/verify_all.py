#still needs verify steps!!! 

import logging
log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_one_string')
    #context.verify(grep="Please Verify My Existence", grep_count=1)
    context.perform_gesture('tap', 'btn_verified')
    context.perform_gesture('tap', 'btn_two_strings')
    
    context.perform_gesture('tap', 'btn_verified')
    context.perform_gesture('tap', 'btn_one_label')
    
    context.perform_gesture('tap', 'btn_accept')
    context.perform_gesture('tap', 'btn_two_labels')
    
    context.perform_gesture('tap', 'btn_accept')
    context.perform_gesture('tap', 'btn_two_labeled_elements')
    
    context.perform_gesture('tap', 'btn_verified')
    context.perform_gesture('tap', 'btn_verify_label_not_present')
    
    context.perform_gesture('tap', 'btn_verified')