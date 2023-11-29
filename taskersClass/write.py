file="taskersClass/texto.txt"
def write(text):
    try:
        with open(file, 'w') as archivo:
            archivo.write(text)
        print(f'Se ha escrito en el archivo "{file}" con éxito.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
 