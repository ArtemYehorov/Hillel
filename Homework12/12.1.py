import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
           text_html = file.read()

    def get_cleaned_text(cleaned_text = ''):
        in_tag = False
        for char in text_html:
            if char == '<':
                in_tag = True
            elif char == '>':
                in_tag = False
            elif not in_tag:
                cleaned_text += char
        return cleaned_text

    def get_text_without_empty_lines(cleaned_text):
       lines = cleaned_text.splitlines()
       non_empty_lines = [line.strip() for line in lines if line.strip()]
       final_text = '\n'.join(non_empty_lines)
       return final_text

    with open(result_file, 'w', encoding='utf-8') as output_file:
        output_file.write(get_text_without_empty_lines(get_cleaned_text()))

    print(f"HTML-файл успешно записан в {result_file}")


delete_html_tags('draft.html')