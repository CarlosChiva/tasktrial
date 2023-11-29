file="taskersClass/texto.txt"
def read():
    string=""
    try:
        with open(file, 'r') as archivo:
            string=archivo.read()
    except Exception as e:
        print(f'Ocurrio un error: {e}')        
    finally:
        return string   