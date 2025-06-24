import itertools
import collections
import matplotlib.pyplot as plt

resennas = [
    {"usuario": "Ana", "puntaje": 5, "comentario": "Excelente producto, muy recomendado"},
    {"usuario": "Carlos", "puntaje": 4, "comentario": "Muy buena calidad, cumple lo esperado"},
    {"usuario": "María", "puntaje": 3, "comentario": "Buen producto pero el envío tardó mucho"},
    {"usuario": "Juan", "puntaje": 5, "comentario": "Superó mis expectativas, lo recomiendo"},
    {"usuario": "Lucía", "puntaje": 2, "comentario": "No era lo que esperaba, calidad regular"},
    {"usuario": "Pedro", "puntaje": 5, "comentario": "Excelente relación calidad-precio"},
    {"usuario": "Sofía", "puntaje": 1, "comentario": "Producto defectuoso, no funcionaba"},
    {"usuario": "Diego", "puntaje": 4, "comentario": "Buen producto, entrega rápida"},
    {"usuario": "Elena", "puntaje": 5, "comentario": "Perfecto, justo lo que necesitaba"},
    {"usuario": "Javier", "puntaje": 3, "comentario": "Aceptable pero hay mejores opciones"},
    {"usuario": "Laura", "puntaje": 5, "comentario": "Increíble producto, muy satisfecha"},
    {"usuario": "Miguel", "puntaje": 2, "comentario": "No cumple con lo prometido"},
    {"usuario": "Isabel", "puntaje": 4, "comentario": "Buena compra, lo usaré nuevamente"},
    {"usuario": "Ricardo", "puntaje": 5, "comentario": "Excelente servicio y producto"},
    {"usuario": "Carmen", "puntaje": 1, "comentario": "Pésima experiencia, no lo recomiendo"},
    {"usuario": "Fernando", "puntaje": 3, "comentario": "Regular, podría ser mejor"},
    {"usuario": "Patricia", "puntaje": 5, "comentario": "Maravilloso, vale cada centavo"},
    {"usuario": "Alejandro", "puntaje": 4, "comentario": "Muy buen producto, pequeñas mejoras posibles"},
    {"usuario": "Rosa", "puntaje": 2, "comentario": "No me convenció, esperaba más calidad"},
    {"usuario": "Manuel", "puntaje": 5, "comentario": "Fantástico, superó mis expectativas"},
    {"usuario": "Teresa", "puntaje": 3, "comentario": "Bueno pero el precio es algo elevado"},
    {"usuario": "Francisco", "puntaje": 4, "comentario": "Cumple con su función, buena compra"},
    {"usuario": "Antonia", "puntaje": 5, "comentario": "Inmejorable, lo recomiendo 100%"},
    {"usuario": "José", "puntaje": 1, "comentario": "Decepcionado, no compraría nuevamente"},
    {"usuario": "Dolores", "puntaje": 4, "comentario": "Satisfecha con la compra"},
    {"usuario": "Pablo", "puntaje": 5, "comentario": "Excelente en todos los aspectos"},
    {"usuario": "Silvia", "puntaje": 2, "comentario": "No vale lo que cuesta"},
    {"usuario": "Alberto", "puntaje": 3, "comentario": "Normal, nada especial"},
    {"usuario": "Raquel", "puntaje": 5, "comentario": "Impresionante, mejor de lo esperado"},
    {"usuario": "Arturo", "puntaje": 4, "comentario": "Buen producto, buen servicio"},
    {"usuario": "Olga", "puntaje": 1, "comentario": "Horrible, no funcional"},
    {"usuario": "Guillermo", "puntaje": 5, "comentario": "Perfecto, exactamente como en la descripción"},
    {"usuario": "Beatriz", "puntaje": 3, "comentario": "Regular, no destacable"},
    {"usuario": "Sergio", "puntaje": 4, "comentario": "Buena relación calidad-precio"},
    {"usuario": "Nuria", "puntaje": 2, "comentario": "No lo recomiendo, mala calidad"},
    {"usuario": "Héctor", "puntaje": 5, "comentario": "Increíble, lo mejor que he comprado"},
    {"usuario": "Victoria", "puntaje": 3, "comentario": "Aceptable pero con reservas"},
    {"usuario": "Óscar", "puntaje": 4, "comentario": "Contento con la compra"},
    {"usuario": "Claudia", "puntaje": 5, "comentario": "Excelente, super recomendado"},
    {"usuario": "Emilio", "puntaje": 1, "comentario": "Pésimo, no cumple su función"},
    {"usuario": "Alicia", "puntaje": 4, "comentario": "Muy bien, cumple lo prometido"},
    {"usuario": "Roberto", "puntaje": 3, "comentario": "Ni bueno ni malo, normal"},
    {"usuario": "Eva", "puntaje": 5, "comentario": "Maravilloso producto, muy feliz"},
    {"usuario": "Jorge", "puntaje": 2, "comentario": "No satisface, calidad mediocre"},
    {"usuario": "Luisa", "puntaje": 4, "comentario": "Buen producto, buen servicio postventa"},
    {"usuario": "Andrés", "puntaje": 5, "comentario": "Excepcional, vale cada peso"},
    {"usuario": "Marta", "puntaje": 3, "comentario": "Está bien, pero esperaba más"},
    {"usuario": "Felipe", "puntaje": 4, "comentario": "Recomendable, buena compra"},
    {"usuario": "Cristina", "puntaje": 5, "comentario": "Perfecto, no tengo quejas"},
    {"usuario": "Víctor", "puntaje": 1, "comentario": "Basura, no lo compren"},
    {"usuario": "Adriana", "puntaje": 5, "comentario": "Increíble calidad, superó todas mis expectativas"},
    {"usuario": "Bernardo", "puntaje": 4, "comentario": "Muy buen producto, solo un pequeño detalle podría mejorar"},
    {"usuario": "Celeste", "puntaje": 3, "comentario": "Funciona bien pero la atención al cliente fue regular"},
    {"usuario": "Daniel", "puntaje": 5, "comentario": "Absolutamente perfecto, lo compraría nuevamente"},
    {"usuario": "Estela", "puntaje": 2, "comentario": "No duró mucho tiempo, calidad inferior a lo esperado"},
    {"usuario": "Federico", "puntaje": 5, "comentario": "Excelente inversión, totalmente satisfecho"},
    {"usuario": "Gloria", "puntaje": 1, "comentario": "Defectuoso desde el primer día, muy decepcionada"},
    {"usuario": "Hugo", "puntaje": 4, "comentario": "Buen rendimiento, entrega puntual"},
    {"usuario": "Irene", "puntaje": 5, "comentario": "Me encantó, cumple exactamente con lo prometido"},
    {"usuario": "Jacobo", "puntaje": 3, "comentario": "Es aceptable, aunque el precio es algo alto"},
    {"usuario": "Karla", "puntaje": 5, "comentario": "Simplemente maravilloso, super recomendado"},
    {"usuario": "Lorenzo", "puntaje": 2, "comentario": "No es lo que aparece en la descripción"},
    {"usuario": "Mónica", "puntaje": 4, "comentario": "Buena relación calidad-precio, lo usaré otra vez"},
    {"usuario": "Néstor", "puntaje": 5, "comentario": "Impresionante, mejor de lo que imaginaba"},
    {"usuario": "Olivia", "puntaje": 1, "comentario": "Pésima calidad, no sirve para lo que necesitaba"},
    {"usuario": "Paco", "puntaje": 3, "comentario": "Regular, hace su función pero sin destacar"},
    {"usuario": "Queca", "puntaje": 5, "comentario": "Vale cada centavo, excelente adquisición"},
    {"usuario": "Ramón", "puntaje": 4, "comentario": "Muy satisfecho, cumple perfectamente"},
    {"usuario": "Sara", "puntaje": 2, "comentario": "No cumplió mis expectativas, no lo recomiendo"},
    {"usuario": "Tomás", "puntaje": 5, "comentario": "Fantástico producto, atención excelente"},
    {"usuario": "Úrsula", "puntaje": 3, "comentario": "Bueno en general, aunque podría mejorar"},
    {"usuario": "Vanesa", "puntaje": 4, "comentario": "Contentísima con mi compra, buenísima calidad"},
    {"usuario": "Walter", "puntaje": 5, "comentario": "Perfecto estado, llegó antes de lo esperado"},
    {"usuario": "Ximena", "puntaje": 1, "comentario": "Horrible experiencia, producto no funcional"},
    {"usuario": "Yolanda", "puntaje": 4, "comentario": "Muy conforme, superó mis expectativas"},
    {"usuario": "Zacarías", "puntaje": 3, "comentario": "Normal, ni bueno ni malo"},
    {"usuario": "Amalia", "puntaje": 5, "comentario": "Inmejorable calidad, servicio impecable"},
    {"usuario": "Bruno", "puntaje": 2, "comentario": "No vale la pena, hay mejores opciones"},
    {"usuario": "Camila", "puntaje": 4, "comentario": "Muy buena compra, estoy satisfecha"},
    {"usuario": "Damián", "puntaje": 5, "comentario": "Excelente en todos los sentidos"},
    {"usuario": "Elisa", "puntaje": 3, "comentario": "Cumple su función básica, nada más"},
    {"usuario": "Fabián", "puntaje": 1, "comentario": "Pésimo servicio postventa, producto regular"},
    {"usuario": "Gabriela", "puntaje": 5, "comentario": "Increíble, mejor compra del año"},
    {"usuario": "Hernán", "puntaje": 4, "comentario": "Buen producto, entrega rápida"},
    {"usuario": "Ingrid", "puntaje": 2, "comentario": "No recomiendo, mala experiencia"},
    {"usuario": "Julio", "puntaje": 5, "comentario": "Perfecto estado, excelente calidad"},
    {"usuario": "Karen", "puntaje": 3, "comentario": "Regular, esperaba algo mejor"},
    {"usuario": "Leonardo", "puntaje": 4, "comentario": "Muy contento con la compra"},
    {"usuario": "Mireya", "puntaje": 5, "comentario": "Superó ampliamente mis expectativas"},
    {"usuario": "Norberto", "puntaje": 1, "comentario": "Decepcionante, no funciona bien"},
    {"usuario": "Octavio", "puntaje": 4, "comentario": "Buen producto, buen servicio"},
    {"usuario": "Paulina", "puntaje": 5, "comentario": "Excelente en todo sentido"},
    {"usuario": "Quirino", "puntaje": 3, "comentario": "Aceptable, pero no destacable"},
    {"usuario": "Rosario", "puntaje": 2, "comentario": "No cumplió con lo prometido"},
    {"usuario": "Salvador", "puntaje": 4, "comentario": "Muy conforme con la compra"},
    {"usuario": "Tania", "puntaje": 5, "comentario": "Perfecto, exactamente lo que buscaba"},
    {"usuario": "Ulises", "puntaje": 1, "comentario": "Mala calidad, no recomiendo"},
    {"usuario": "Verónica", "puntaje": 4, "comentario": "Buena relación calidad-precio"},
    {"usuario": "Wilfredo", "puntaje": 5, "comentario": "Excelente producto, muy duradero"}
]

# 1. Contador de palabras clave
palabras = []
for r in resennas:
    palabras.extend([p.lower().strip(".,¡!¿?") for p in r["comentario"].split() if len(p) > 3])
    
conteo_palabras = collections.Counter(palabras)
print("\nPalabras más frecuentes:")
print(conteo_palabras.most_common(5))

# 2. Agrupación por puntaje
grupos_resennas = collections.defaultdict(list)
for r in resennas:
    grupos_resennas[r["puntaje"]].append(r["comentario"])

print("\nReseñas agrupadas por puntaje:")
for puntaje, comentarios in sorted(grupos_resennas.items()):
    print(f"\nPuntaje {puntaje} ({len(comentarios)} reseñas):")
    print("Ejemplo:", comentarios[0][:50] + "...")

# 3. Combinaciones de palabras clave
print("\nCombinaciones de palabras clave:")
combinaciones = list(itertools.combinations([p[0] for p in conteo_palabras.most_common(5)], 2))
for combo in combinaciones[:5]:  # Mostrar solo las primeras 5
    print(f"{combo[0]} + {combo[1]}")

# 4. Respuestas automáticas
respuestas = ["Gracias por tu comentario", "Nos alegra que te haya gustado", "Esperamos verte de nuevo"]
print("\nPermutaciones de respuestas automáticas:")
for respuesta in itertools.permutations(respuestas, 2):
    print(" → ".join(respuesta))

# 5. Gráfico de barras mejorado
plt.figure(figsize=(10, 6))  # Corregido plt.Figure a plt.figure
top_palabras = conteo_palabras.most_common(5)

# Gráfico horizontal (barh) con mejor formato
plt.barh(
    [p[0] for p in top_palabras],
    [p[1] for p in top_palabras],
    color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
)

# Añadir etiquetas de valor
for i, (palabra, freq) in enumerate(top_palabras):
    plt.text(freq + 0.5, i, str(freq), va='center')

plt.xlabel("Frecuencia", fontweight='bold')
plt.ylabel("Palabras", fontweight='bold')
plt.title("Top 5 Palabras Más Frecuentes en Reseñas", pad=20, fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()