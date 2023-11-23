ESTADO = [ ('1', 'En Stock'), ('2', 'Agotado'), ]
CATEGORIAS = [
    ('0', 'Sin categoría'),
    ('1', 'Frutas'),
    ('2', 'Carnes'),
    ('3', 'Mariscos'),
    ('4', 'Postres'),
    ('5', 'Especias y Condimentos'),
    ('6', 'Productos Organicos'),
    ('7', 'Bebidas'),
    ('8', 'Aves'),
    ('9', 'Helados'),
    ('10', 'Comida Japonesa'),
]

lista_estados = {key: value for key, value in ESTADO}
lista_categorias = {key: value for key, value in CATEGORIAS}