#TODAY is the 6th Day
import random

abc = 'abcdefghijklmnñopqrstuvwxyz'

class Mankind():
    def __init__(self, material='mud', gen='A', cromosomas=None):
        if cromosomas is None:
            cromosomas = []
        self.material = material
        self.cromosomas = cromosomas
        self.gen = gen
        if not cromosomas:
            self.setCromosomes()

    def appearance(self):
        pass

    def setCromosomes(self):
        for _ in range(22):
            par = random.sample(abc, 2)  
            self.cromosomas.append(''.join(par)) 
        if self.gen == 'H':
            self.cromosomas.append('xy')
        elif self.gen == 'M':
            self.cromosomas.append('xx')
        else:
            self.cromosomas.append('gy')

    def showGenotype(self):
        print(''.join(self.cromosomas))

    def getGenotype(self):
        return ''.join(self.cromosomas)

    def __add__(self, other):
        nueva_lista = []
        # Limitar el rango al tamaño mínimo de las listas de cromosomas
        for i in range(min(len(self.cromosomas), len(other.cromosomas))):
            elemento_aleatorio = random.choice([self.cromosomas[i], other.cromosomas[i]])
            nueva_lista.append(elemento_aleatorio)
        
        # Agregar el cromosoma extra si es necesario
        if len(self.cromosomas) > len(nueva_lista):
            nueva_lista.append(self.cromosomas[len(nueva_lista)])
        
        return Mankind(gen='H', cromosomas=nueva_lista)


# Crear instancias de Mankind
Adan = Mankind(gen='H')
Adan.showGenotype()
Eva = Mankind(gen='M')
Eva.showGenotype()

# Sumar Adan y Eva
Cain = Adan + Eva
Cain.showGenotype()

Abel = Adan + Eva
Abel.showGenotype()

Seth = Adan + Eva
Seth.showGenotype()


import matplotlib.pyplot as plt

# Definir los genotipos
adan_cromosomas = Adan.getGenotype()  
eva_cromosomas = Eva.getGenotype()  
cain_cromosomas = Cain.getGenotype()  
abel_cromosomas = Abel.getGenotype()
seth_cromosomas = Seth.getGenotype()

# Función para generar el genotipo con espacios cada 2 pares de caracteres
def format_genotype(cromosomas):
    return [cromosomas[i:i+2] for i in range(0, len(cromosomas), 2)]

# Formatear los cromosomas
adan_genotype = format_genotype(adan_cromosomas)
eva_genotype = format_genotype(eva_cromosomas)
cain_genotype = format_genotype(cain_cromosomas)
abel_genotype = format_genotype(abel_cromosomas)
seth_genotype = format_genotype(seth_cromosomas)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 5))

# Configuración de la tabla de cromosomas
columns = 23  # Número de pares de cromosomas
rows = 5  # Para Adán, Eva, Cain, Abel, Seth

# Datos de los cromosomas
genotypes = [adan_genotype, eva_genotype, cain_genotype, abel_genotype, seth_genotype]
colors = ['red', 'blue', 'mixed', 'mixed', 'mixed']  # Colores según los genotipos

# Crear una matriz de texto para la tabla
table_data = []
for genotype in genotypes:
    table_data.append(genotype)

# Crear la tabla con las celdas
table = ax.table(cellText=table_data, loc='center', cellLoc='center', colLabels=[f'Par {i+1}' for i in range(columns)])

# Personalizar la tabla
for i, row in table.get_celld().items():
    row_idx, col_idx = i
    if row_idx == 0:  # Skip header
        continue

    # Asignar color dependiendo de quién heredó el cromosoma
    if row_idx == 1:  # Adán
        row.set_fontsize(14)
        row.set_text_props(color='white')
        row.set_facecolor('red')  # Fondo rojo para Adán
    elif row_idx == 2:  # Eva
        row.set_fontsize(14)
        row.set_text_props(color='white')
        row.set_facecolor('blue')  # Fondo azul para Eva
    elif row_idx == 3:  # Cain
        # Alternar entre Adán y Eva
        pair = cain_genotype[col_idx]
        if col_idx % 2 == 0:  # Par de Eva
            row.set_fontsize(14)
            row.set_text_props(color='white')
            row.set_facecolor('blue')  # Fondo azul para Eva
        else:  # Par de Adán
            row.set_fontsize(14)
            row.set_text_props(color='white')
            row.set_facecolor('red')  # Fondo rojo para Adán
    elif row_idx == 4:  # Abel
        # Alternar entre Adán y Eva
        pair = abel_genotype[col_idx]
        if col_idx % 2 == 0:  # Par de Eva
            row.set_fontsize(14)
            row.set_text_props(color='white')
            row.set_facecolor('blue')  # Fondo azul para Eva
        else:  # Par de Adán
            row.set_fontsize(14)
            row.set_text_props(color='white')
            row.set_facecolor('red')  # Fondo rojo para Adán
    elif row_idx == 5:  # Seth
        # Alternar entre Adán y Eva
        pair = seth_genotype[col_idx]
        if col_idx % 2 == 0:  # Par de Eva
            row.set_fontsize(14)
            row.set_text_props(color='white')
            row.set_facecolor('blue')  # Fondo azul para Eva
        else:  # Par de Adán
            row.set_fontsize(14)
            row.set_text_props(color='white')
            row.set_facecolor('red')  # Fondo rojo para Adán

# Ajustar el área del gráfico
ax.axis('off')  # Eliminar los ejes

# Título
ax.set_title('Genotipos de Adán, Eva, Cain, Abel y Seth', fontsize=16)

# Mostrar la imagen
plt.show()
