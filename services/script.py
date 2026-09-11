import re

def replace_between_comments(filepath, start_comment, end_comment, new_inner):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will use regex to find the section
    # Wait, it's easier to just do simple string find
    pass

