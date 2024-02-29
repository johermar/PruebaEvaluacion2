from estrella import Estrella
from galaxia import Galaxia
from universo import Universo

# Creación de estrellas
estrella1 = Estrella("adrian")
estrella2 = Estrella("dani")
estrella3 = Estrella("nacho")

# Creación de galaxias y adición de estrellas
galaxia1 = Galaxia("via semidesnatada")
galaxia1.añadir_estrella(estrella1)
galaxia1.añadir_estrella(estrella2)

galaxia2 = Galaxia("pantalon")
galaxia2.añadir_estrella(estrella3)

# Creación del universo y adición de galaxias
universo = Universo()
universo.añadir_galaxia(galaxia1)
universo.añadir_galaxia(galaxia2)

# Impresión de estructuras
print(estrella1)
print(estrella2)
print(estrella3)
print(galaxia1)
print(galaxia2)
print(universo)