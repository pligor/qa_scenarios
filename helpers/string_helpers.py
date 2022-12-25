import re

word_pattern = re.compile('\w+')

def convert_any_text_to_separated_words(text: str, seperator='_'):
    return seperator.join([word.lower() for word in word_pattern.findall(text)])
