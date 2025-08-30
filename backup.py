import os
from datetime import date

def crear_backup(exclude_dirs: list = None):
    """
    Crea un backup de los directorios en el directorio actual.
    Los archivos de backup se guardan en formato tar.gz y se les agrega la fecha actual.

        :param exclude_dirs: Lista de directorios a excluir del backup.
    """
    
    if exclude_dirs is None:
        exclude_dirs = []
    

    fecha_actual = date.today().strftime('%Y-%m-%d')

    directorios = []

    # crear la lista de directorios
    for d in os.listdir('.'):
        if os.path.isdir(d):
            directorios.append(d)
            
    # filtrar los directorios excluidos
    directorios = [d for d in directorios if d not in exclude_dirs]
    
    os.makedirs('backup', exist_ok=True)

    # iterar sobre los directorios
    for carpeta in directorios:
        print(carpeta)
        # crear un tar -zcvf del directorio agregandole la fecha actual
        nombre_archivo = f"{carpeta}_{fecha_actual}.tar.gz"
        comando = f"tar -zcf backup/{nombre_archivo} {carpeta}"
        os.system(comando)
        
def crear_backup_incluidos(include_dirs: list):
    """
    Crea un backup solo de los directorios especificados en include_dirs.
    Los archivos de backup se guardan en formato tar.gz y se les agrega la fecha actual.

        :param include_dirs: Lista de directorios a incluir en el backup.
    """
    fecha_actual = date.today().strftime('%Y-%m-%d')
    os.makedirs('backup', exist_ok=True)

    # Filtrar solo los directorios existentes
    carpetas_validas = [c for c in include_dirs if os.path.isdir(c)]

    for carpeta in carpetas_validas:
        print(carpeta)
        nombre_archivo = f"{carpeta}_{fecha_actual}.tar.gz"
        comando = f"tar -zcf backup/{nombre_archivo} {carpeta}"
        os.system(comando)
        
if __name__ == "__main__":
    # Excluir el directorio 'backup' del backup
    #crear_backup(exclude_dirs=['backup'])
    crear_backup_incluidos(include_dirs=['dir1', 'dir2'])  # Reemplaza con los nombres de los directorios que deseas incluir