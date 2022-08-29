import re
retorno1 = re.split(r'\W+', 'Palabras, palabras, palabras.')
retorno2 = re.split(r'(\W+)', 'Palabras, palabras, palabras.')
retorno3 = re.split(r'\W+', 'Palabras, palabras, palabras.', 1)
retorno4 = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
retorno5 = re.split('[a-f]+', '0a3B9')
print(retorno1)
print(retorno2)
print(retorno3)
print(retorno4)
print(retorno5)
print("----------------------------")
retorno5 = re.split(r'\W+', '...Palabras..., palabras, palabras...')
retorno6 = re.split(r'(\W+)', '...Palabras..., palabras, palabras...')
print(retorno5)
print(retorno6)

