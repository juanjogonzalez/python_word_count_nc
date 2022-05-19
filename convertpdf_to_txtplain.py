from tika import parser

pdf_file = parser.from_file("PROPUESTA_BORRADOR_CONSTITUCIONAL_140522.pdf")

content = pdf_file['content']
output = content.encode('utf-8', errors='ignore')

decode_output = output.decode()

with open('PROPUESTA_BORRADOR_CONSTITUCIONAL_140522.txt', 'w') as the_file:
    the_file.write(decode_output)