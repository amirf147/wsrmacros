import xml.etree.ElementTree as ET
from pathlib import Path
import json
import pandas as pd

def load_xml_file(xml_file_path):
    # Load the XML file
    tree = ET.parse(xml_file_path)
    return xml_to_dict(tree.getroot())

def xml_to_dict(element):
    """
    Recursively convert an XML element and its children to a dictionary of dictionaries.
    """
    result = {}

    # Store element attributes, if any
    result.update(element.attrib)

    # Store text content of the element, if any
    if element.text:
        result["_text"] = element.text.strip()

    # Recursively process child elements
    for child in element:
        child_data = xml_to_dict(child)
        child_tag = child.tag.lower()

        # Check if the tag already exists in the result
        if child_tag in result:
            # If the tag already exists, convert it to a list if not already
            if not isinstance(result[child_tag], list):
                result[child_tag] = [result[child_tag]]
            result[child_tag].append(child_data)
        else:
            # If the tag is encountered for the first time, create a new entry
            result[child_tag] = child_data

    return result

def to_excel_structure(commands_list, excel_structure): 
    # the command element does not have text within it so we need to remove its field
    for command in commands_list:
        del command['_text']

    for command in commands_list:
        # action_list = []
        print(command)
        l = [[],[],[],[]]
        for action in command:
            # print(action)
            if action == "priority":
                print(command[action])
                l[0].append(command[action])
            elif action == "listenfor":
                if isinstance(command[action], dict):
                    l[1].append(command[action]["_text"])
                    # print(l)
                elif isinstance(command[action], list):
                    for t in command[action]:
                        l[1].append(t["_text"])
                        # print(l)
                # print(excel_structure)
            elif action == "rule":
                # for range(len(command[action])):
                l[1].append("rule "+str(command[action]))
            elif action == "emulaterecognition":
                if isinstance(command[action], dict):
                    l[2].append(command[action]["_text"])
                elif isinstance(command[action], list):
                    for t in command[action]:
                        l[2].append(t["_text"])
            elif action == "sendkeys":
                if isinstance(command[action], dict):
                    if "_text" in command[action] and not "times" in command[action]:
                        # print(command[action]["_text"])
                        l[3].append(("1", command[action]["_text"]))
                    elif "times" in command[action]:
                        # print(command[action]["times"], command[action]["_text"])
                        l[3].append((command[action]["times"], command[action]["_text"]))
                elif isinstance(command[action], list):
                    for sendkeys in command[action]:
                        if "_text" in sendkeys and not "times" in sendkeys:
                            # print(sendkeys["_text"])
                            l[3].append(("1", sendkeys["_text"]))
                        elif "times" in sendkeys:
                            # print(sendkeys["times"], sendkeys["_text"])
                            l[3].append((sendkeys["times"], sendkeys["_text"]))
            # print(l)
        excel_structure["priority"].append(l[0])
        excel_structure["listenFor/rule"].append(l[1])
        excel_structure["emulateRecognition"].append(l[2])
        excel_structure["sendKeys"].append(l[3])
        print(excel_structure)

    # Convert the lists to strings with commas separating the list elements
    excel_structure["priority"] = [', '.join(map(str, item)) for item in excel_structure["priority"]]
    excel_structure["listenFor/rule"] = [', '.join(map(str, item)) for item in excel_structure["listenFor/rule"]]
    excel_structure["emulateRecognition"] = [', '.join(map(str, item)) for item in excel_structure["emulateRecognition"]]
    excel_structure["sendKeys"] = [', '.join(map(str, item)) for item in excel_structure["sendKeys"]]
    return excel_structure


def convert_rule_string_to_xml(rule_string):
    rule_dict = json.loads(rule_string) 
    root = ET.Element("rule")

    if '_text' in rule_dict:
        ET.SubElement(root, 'p').text = rule_dict['_text']
    
    if 'p' in rule_dict:
        for p_item in rule_dict['p']:
            p_element = ET.SubElement(root, 'p')
            if '_text' in p_item:
                p_element.text = p_item['_text']
            elif 'min' in p_item and 'max' in p_item:
                p_element.set('min', p_item['min'])
                p_element.set('max', p_item['max'])
                ruleref_element = ET.SubElement(p_element, 'ruleref')
                ruleref_element.set('name', p_item['ruleref']['name'])
                ruleref_element.set('propname', p_item['ruleref']['propname'])

    return ET.tostring(root, encoding='utf8').decode('utf8')

