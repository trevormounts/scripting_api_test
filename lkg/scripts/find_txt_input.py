#needs verify steps still? 
import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info=context.find_element('txt_input')
    data=json.dump('element_info')
    #json_info=json.dumps('data')
    #context.perform_gesture('text_entry_no_submit', 'inp_element_info_txt', data)


    print('=======================================output find element===============================')
    print(element_info)
    #print(data)
    # print(json_info)
    print('=========================================end find element================================')

    #context.perform_gesture('text_entry_no_submit', 'inp_element_info_txt', einfo_json_str)

    ##how to parse json, how to print info from python dict, how to pull info from nested JSON or dict

    # I want you to extract three items of information from this dict / json / unicode...whatever it is:
    # 1. height and width, text
    # 2. attribute type value
    # 3. flags clickable value