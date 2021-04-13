#needs verify steps still? 
import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info=context.find_element('btn_button_find_element')
    einfo_json_str=json.loads(element_info)


    print('====================output find element====================')
    print(element_info)
    print(einfo_json_str)
    print(element_info) 

    print('====================end find element====================')

    #context.perform_gesture('text_entry_no_submit', 'inp_element_info_txt', einfo_json_str)

    ##how to parse json, how to print info from python dict, how to pull info from nested JSON or dict

    # I want you to extract three items of information from this dict / json / unicode...whatever it is:
    # 1. height and width, text
    # 2. attribute type value
    # 3. flags clickable value
    










    # context.perform_gesture('tap', 'mnu_find_element')
    # time.sleep(10)
    # context.perform_gesture('tap', 'btn_button_find_element')
    # time.sleep(10)
    # context.perform_gesture('tap', 'inp_checkbox')
    # time.sleep(10)
    # context.perform_gesture('tap', 'inp_slider')
    # time.sleep(10)
    # context.perform_gesture('tap', 'btn_radio')
    # time.sleep(10)
    # context.perform_gesture('text_input','txt_input', 'lorem ipsum test text')
    # time.sleep(10)