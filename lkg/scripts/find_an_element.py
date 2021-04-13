import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info = context.find_element('btn_button_find_element')
    einfo_json = json.dumps(element_info)
    einfo_loads = json.loads(element_info)

    print('====================output find element====================') 
    print(element_info)
    print(einfo_json)
    print(element_info['flags'])
    print(element_info.flags)
    # print(einfo_loads)
    print('====================end find element====================')

    context.perform_gesture('text_entry_no_submit', 'inp_element_info_txt', einfo_json)