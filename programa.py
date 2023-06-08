from tkinter import *
from tkinter import messagebox
from random import choice

# Definimos un diccionario vacío para almacenar las preguntas y respuestas
preguntas_respuestas = {}

# Función para agregar una pregunta y su respuesta al diccionario
def agregar_pregunta_respuesta(pregunta, respuesta):
    preguntas_respuestas[pregunta] = respuesta

# Función para buscar una respuesta a partir de una pregunta dada
def buscar_respuesta(pregunta):
    if pregunta in preguntas_respuestas:
        return preguntas_respuestas[pregunta]
    else:
        return "Lo siento, no tengo respuesta para esa pregunta."

# Base de datos

agregar_pregunta_respuesta("¿Cuál es la capital de España?", "Madrid")
agregar_pregunta_respuesta("¿En qué país se encuentra la Torre Eiffel?", "Francia")
agregar_pregunta_respuesta("¿Cuál es el río más largo del mundo?", "Amazonas")
agregar_pregunta_respuesta("¿Cuál es el océano más grande?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Quién escribió la obra 'Romeo y Julieta'?", "William Shakespeare")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del oro?", "Au")
agregar_pregunta_respuesta("¿Cuál es el órgano más grande del cuerpo humano?", "La piel")
agregar_pregunta_respuesta("¿Cuál es el planeta más grande del sistema solar?", "Júpiter")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta del mundo?", "Monte Everest")
agregar_pregunta_respuesta("¿Quién pintó la Mona Lisa?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más poblado del mundo?", "China")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de viento más antiguo?", "La flauta")
agregar_pregunta_respuesta("¿En qué continente se encuentra el desierto del Sahara?", "África")
agregar_pregunta_respuesta("¿Cuál es el metal líquido a temperatura ambiente?", "Mercurio")
agregar_pregunta_respuesta("¿Cuál es el idioma más hablado en el mundo?", "Chino mandarín")
agregar_pregunta_respuesta("¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez")
agregar_pregunta_respuesta("¿Cuál es el país más grande del mundo en términos de superficie?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el animal más grande del mundo?", "La ballena azul")
agregar_pregunta_respuesta("¿Quién fue el primer presidente de los Estados Unidos?", "George Washington")
agregar_pregunta_respuesta("¿Cuál es el país conocido como la 'tierra de los faraones'?", "Egipto")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como la 'Ciudad Eterna'?", "Roma")
agregar_pregunta_respuesta("¿Quién escribió '1984'?", "George Orwell")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del carbono?", "C")
agregar_pregunta_respuesta("¿Cuál es el hueso más largo del cuerpo humano?", "El fémur")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de América del Norte?", "Monte Denali")
agregar_pregunta_respuesta("¿Quién pintó 'La noche estrellada'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño del mundo?", "Ciudad del Vaticano")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor número de países?", "África")
agregar_pregunta_respuesta("¿Quién escribió 'Orgullo y prejuicio'?", "Jane Austen")
agregar_pregunta_respuesta("¿Cuál es el océano más frío?", "Océano Antártico")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de cuerda más grande?", "El contrabajo")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de México?", "América")
agregar_pregunta_respuesta("¿Cuál es el metal más ligero?", "Litio")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Brasil?", "Portugués")
agregar_pregunta_respuesta("¿Quién escribió 'Don Quijote de la Mancha'?", "Miguel de Cervantes Saavedra")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Japón?", "Yen")
agregar_pregunta_respuesta("¿Cuál es el planeta más cercano al sol?", "Mercurio")
agregar_pregunta_respuesta("¿Cuál es el desierto más grande de América del Norte?", "Desierto de Sonora")
agregar_pregunta_respuesta("¿Quién fue el famoso físico que formuló la teoría de la relatividad?", "Albert Einstein")
agregar_pregunta_respuesta("¿Cuál es el país más visitado del mundo?", "Francia")
agregar_pregunta_respuesta("¿Cuál es el elemento químico más abundante en el universo?", "Hidrógeno")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Atenas?", "Grecia")
agregar_pregunta_respuesta("¿Cuál es el período de gestación de un elefante?", "Aproximadamente 22 meses")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Australia?", "Inglés")
agregar_pregunta_respuesta("¿Cuál es el animal más rápido del mundo?", "El guepardo")
agregar_pregunta_respuesta("¿Quién pintó 'La última cena'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país con forma de bota en Europa?", "Italia")
agregar_pregunta_respuesta("¿Cuál es el continente más seco del mundo?", "Antártida")
agregar_pregunta_respuesta("¿Quién escribió 'El Gran Gatsby'?", "F. Scott Fitzgerald")
agregar_pregunta_respuesta("¿Cuál es el océano más pequeño del mundo?", "Océano Ártico")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de percusión más antiguo?", "El tambor")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Nigeria?", "África")
agregar_pregunta_respuesta("¿Cuál es el metal más resistente?", "El tungsteno")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Canadá?", "Inglés y francés")
agregar_pregunta_respuesta("¿Quién escribió 'Matar a un ruiseñor'?", "Harper Lee")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de México?", "Peso mexicano")
agregar_pregunta_respuesta("¿Cuál es el planeta más alejado del sol?", "Neptuno")
agregar_pregunta_respuesta("¿Cuál es el desierto más grande del mundo?", "El desierto del Sáhara")
agregar_pregunta_respuesta("¿Quién fue el científico que formuló la teoría de la evolución?", "Charles Darwin")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de América del Sur?", "Brasil")
agregar_pregunta_respuesta("¿Cuál es el elemento químico más pesado?", "Oganesón")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Praga?", "República Checa")
agregar_pregunta_respuesta("¿Cuál es el período de gestación de una ballena?", "Aproximadamente 11 meses")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Argentina?", "Español")
agregar_pregunta_respuesta("¿Cuál es el ave más grande del mundo?", "El avestruz")
agregar_pregunta_respuesta("¿Quién pintó 'La persistencia de la memoria'?", "Salvador Dalí")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra del sol naciente'?", "Japón")
agregar_pregunta_respuesta("¿Cuál es el continente más poblado del mundo?", "Asia")
agregar_pregunta_respuesta("¿Quién escribió 'Ulises'?", "James Joyce")
agregar_pregunta_respuesta("¿Cuál es el océano más profundo?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de viento más pequeño?", "La armónica")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Italia?", "Europa")
agregar_pregunta_respuesta("¿Cuál es el metal más caro?", "El rodio")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Alemania?", "Alemán")
agregar_pregunta_respuesta("¿Quién escribió 'El señor de los anillos'?", "J.R.R. Tolkien")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Reino Unido?", "Libra esterlina")
agregar_pregunta_respuesta("¿Cuál es el planeta más pequeño del sistema solar?", "Mercurio")
agregar_pregunta_respuesta("¿Cuál es el desierto más frío del mundo?", "Desierto de Gobi")
agregar_pregunta_respuesta("¿Quién fue el famoso físico que desarrolló la teoría de la gravedad?", "Isaac Newton")
agregar_pregunta_respuesta("¿Cuál es el país con el idioma más hablado del mundo?", "China")
agregar_pregunta_respuesta("¿Cuál es el elemento químico más común en la corteza terrestre?", "Oxígeno")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Moscú?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el período de gestación de un perro?", "Aproximadamente 9 semanas")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de España?", "Español")
agregar_pregunta_respuesta("¿Cuál es el mamífero más rápido del mundo?", "El guepardo")
agregar_pregunta_respuesta("¿Quién pintó 'Los girasoles'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra del fuego'?", "Argentina")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor número de países?", "África")
agregar_pregunta_respuesta("¿Quién escribió 'Crimen y castigo'?", "Fiódor Dostoyevski")
agregar_pregunta_respuesta("¿Cuál es el océano más cálido?", "Océano Índico")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de cuerda más pequeño?", "El violín")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Sudáfrica?", "África")
agregar_pregunta_respuesta("¿Cuál es el metal más dúctil?", "El oro")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Francia?", "Francés")
agregar_pregunta_respuesta("¿Quién escribió 'Los Miserables'?", "Victor Hugo")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de China?", "Yuan")
agregar_pregunta_respuesta("¿Cuál es el planeta más caliente del sistema solar?", "Venus")
agregar_pregunta_respuesta("¿Cuál es el desierto más húmedo del mundo?", "El desierto del Namib")
agregar_pregunta_respuesta("¿Quién fue el científico que desarrolló la teoría de la relatividad?", "Albert Einstein")
agregar_pregunta_respuesta("¿Cuál es el país con más ganadores de la Copa del Mundo de la FIFA?", "Brasil")
agregar_pregunta_respuesta("¿Cuál es la capital de Italia?", "Roma")
agregar_pregunta_respuesta("¿En qué país se encuentra el Taj Mahal?", "India")
agregar_pregunta_respuesta("¿Cuál es el río más largo de África?", "Nilo")
agregar_pregunta_respuesta("¿Cuál es el océano más salado?", "Océano Atlántico")
agregar_pregunta_respuesta("¿Quién escribió 'La Odisea'?", "Homero")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del hierro?", "Fe")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la bilis?", "El hígado")
agregar_pregunta_respuesta("¿Cuál es el planeta más cercano a la Tierra?", "Venus")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de África?", "Monte Kilimanjaro")
agregar_pregunta_respuesta("¿Quién pintó 'La noche estrellada'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de África?", "Nigeria")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de viento más antiguo?", "La flauta")
agregar_pregunta_respuesta("¿En qué continente se encuentra el desierto de Gobi?", "Asia")
agregar_pregunta_respuesta("¿Cuál es el metal líquido a temperatura ambiente?", "Mercurio")
agregar_pregunta_respuesta("¿Cuál es el idioma más hablado en el mundo?", "Chino mandarín")
agregar_pregunta_respuesta("¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de África?", "Argelia")
agregar_pregunta_respuesta("¿Cuál es el animal más grande del mundo?", "La ballena azul")
agregar_pregunta_respuesta("¿Quién fue el primer presidente de los Estados Unidos?", "George Washington")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra del sol naciente'?", "Japón")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La Ciudad Eterna'?", "Roma")
agregar_pregunta_respuesta("¿Quién escribió '1984'?", "George Orwell")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del carbono?", "C")
agregar_pregunta_respuesta("¿Cuál es el hueso más largo del cuerpo humano?", "El fémur")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de América del Norte?", "Monte Denali")
agregar_pregunta_respuesta("¿Quién pintó 'La Mona Lisa'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño del mundo?", "Ciudad del Vaticano")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor número de países?", "África")
agregar_pregunta_respuesta("¿Quién escribió 'La isla del tesoro'?", "Robert Louis Stevenson")
agregar_pregunta_respuesta("¿Cuál es el océano más grande del mundo?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de percusión más grande?", "El órgano")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Egipto?", "África")
agregar_pregunta_respuesta("¿Cuál es el metal más abundante en la corteza terrestre?", "Aluminio")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de México?", "Español")
agregar_pregunta_respuesta("¿Quién escribió 'La Divina Comedia'?", "Dante Alighieri")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Canadá?", "Dólar canadiense")
agregar_pregunta_respuesta("¿Cuál es el planeta más alejado del sol?", "Neptuno")
agregar_pregunta_respuesta("¿Cuál es el desierto más seco del mundo?", "El desierto de Atacama")
agregar_pregunta_respuesta("¿Quién fue el famoso físico que enunció las leyes del movimiento?", "Isaac Newton")
agregar_pregunta_respuesta("¿Cuál es el país con más Premios Nobel recibidos?", "Estados Unidos")
agregar_pregunta_respuesta("¿Cuál es la capital de Australia?", "Canberra")
agregar_pregunta_respuesta("¿En qué país se encuentra el Coliseo Romano?", "Italia")
agregar_pregunta_respuesta("¿Cuál es el río más largo de América del Norte?", "Río Misisipi")
agregar_pregunta_respuesta("¿Cuál es el océano más profundo del mundo?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Quién escribió 'Hamlet'?", "William Shakespeare")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del oro?", "Au")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la insulina?", "El páncreas")
agregar_pregunta_respuesta("¿Cuál es el planeta más grande del sistema solar?", "Júpiter")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Europa?", "Monte Elbrus")
agregar_pregunta_respuesta("¿Quién pintó 'La Gioconda'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de Europa?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de viento más popular?", "La guitarra")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de China?", "Asia")
agregar_pregunta_respuesta("¿Cuál es el metal más utilizado en la industria automotriz?", "Acero")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Rusia?", "Ruso")
agregar_pregunta_respuesta("¿Quién escribió 'El Principito'?", "Antoine de Saint-Exupéry")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de Europa?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el animal más pesado del mundo?", "La ballena azul")
agregar_pregunta_respuesta("¿Quién fue el primer ser humano en pisar la luna?", "Neil Armstrong")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La cuna de la civilización'?", "Irak")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La ciudad de los canales'?", "Venecia")
agregar_pregunta_respuesta("¿Quién escribió 'Orgullo y prejuicio'?", "Jane Austen")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del plomo?", "Pb")
agregar_pregunta_respuesta("¿Cuál es el hueso más pequeño del cuerpo humano?", "El estribo")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de América del Sur?", "Monte Aconcagua")
agregar_pregunta_respuesta("¿Quién pintó 'La noche estrellada'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño de América del Sur?", "Surinam")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor diversidad cultural?", "África")
agregar_pregunta_respuesta("¿Quién escribió 'Don Quijote de la Mancha'?", "Miguel de Cervantes Saavedra")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Japón?", "Yen")
agregar_pregunta_respuesta("¿Cuál es la capital de Canadá?", "Ottawa")
agregar_pregunta_respuesta("¿En qué país se encuentra la Gran Muralla China?", "China")
agregar_pregunta_respuesta("¿Cuál es el río más largo de América del Sur?", "Río Amazonas")
agregar_pregunta_respuesta("¿Cuál es el océano más frío del mundo?", "Océano Ártico")
agregar_pregunta_respuesta("¿Quién escribió 'Romeo y Julieta'?", "William Shakespeare")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico de la plata?", "Ag")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la adrenalina?", "Las glándulas suprarrenales")
agregar_pregunta_respuesta("¿Cuál es el planeta más cercano al sol?", "Mercurio")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Sudamérica?", "Monte Aconcagua")
agregar_pregunta_respuesta("¿Quién pintó 'La persistencia de la memoria'?", "Salvador Dalí")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de Sudamérica?", "Brasil")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de viento más antiguo?", "La flauta")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Australia?", "Oceanía")
agregar_pregunta_respuesta("¿Cuál es el metal más utilizado en la fabricación de aviones?", "Aluminio")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Alemania?", "Alemán")
agregar_pregunta_respuesta("¿Quién escribió 'Moby Dick'?", "Herman Melville")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de Sudamérica?", "Brasil")
agregar_pregunta_respuesta("¿Cuál es el animal más veloz del mundo?", "El guepardo")
agregar_pregunta_respuesta("¿Quién fue el inventor de la electricidad?", "Thomas Edison")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La cuna de la democracia'?", "Grecia")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La ciudad de los rascacielos'?", "Nueva York")
agregar_pregunta_respuesta("¿Quién escribió 'El Gran Gatsby'?", "F. Scott Fitzgerald")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del cobre?", "Cu")
agregar_pregunta_respuesta("¿Cuál es el hueso más pequeño del cuerpo humano?", "El estribo")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Oceanía?", "Monte Puncak Jaya")
agregar_pregunta_respuesta("¿Quién pintó 'La persistencia de la memoria'?", "Salvador Dalí")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño de Oceanía?", "Nauru")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor cantidad de idiomas?", "Asia")
agregar_pregunta_respuesta("¿Quién escribió 'Las aventuras de Tom Sawyer'?", "Mark Twain")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Reino Unido?", "Libra esterlina")
agregar_pregunta_respuesta("¿Cuál es la capital de Argentina?", "Buenos Aires")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Petra?", "Jordania")
agregar_pregunta_respuesta("¿Cuál es el río más largo de Asia?", "Río Yangtsé")
agregar_pregunta_respuesta("¿Cuál es el océano más grande del mundo?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Quién escribió '1984'?", "George Orwell")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del calcio?", "Ca")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la hormona del crecimiento?", "La glándula pituitaria")
agregar_pregunta_respuesta("¿Cuál es el planeta más pequeño del sistema solar?", "Mercurio")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Norteamérica?", "Monte Denali")
agregar_pregunta_respuesta("¿Quién pintó 'La última cena'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de Asia?", "China")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de percusión más antiguo?", "El tambor")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Brasil?", "América del Sur")
agregar_pregunta_respuesta("¿Cuál es el metal más utilizado en la industria eléctrica?", "Cobre")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Francia?", "Francés")
agregar_pregunta_respuesta("¿Quién escribió 'Los miserables'?", "Victor Hugo")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de Asia?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el animal más rápido del mundo?", "El guepardo")
agregar_pregunta_respuesta("¿Quién fue el primer ser humano en orbitar la Tierra?", "Yuri Gagarin")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra de los faraones'?", "Egipto")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La ciudad del amor'?", "París")
agregar_pregunta_respuesta("¿Quién escribió 'Orgullo y prejuicio'?", "Jane Austen")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del potasio?", "K")
agregar_pregunta_respuesta("¿Cuál es el hueso más largo del cuerpo humano?", "El fémur")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Asia?", "Monte Everest")
agregar_pregunta_respuesta("¿Quién pintó 'La noche estrellada'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño de Asia?", "Maldivas")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor número de habitantes?", "Asia")
agregar_pregunta_respuesta("¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Suiza?", "Franco suizo")
agregar_pregunta_respuesta("¿Cuál es la capital de Francia?", "París")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Machu Picchu?", "Perú")
agregar_pregunta_respuesta("¿Cuál es el río más largo de África?", "Río Nilo")
agregar_pregunta_respuesta("¿Cuál es el océano más salado del mundo?", "Océano Atlántico")
agregar_pregunta_respuesta("¿Quién escribió 'El Gran Gatsby'?", "F. Scott Fitzgerald")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del hierro?", "Fe")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la bilis?", "El hígado")
agregar_pregunta_respuesta("¿Cuál es el planeta más alejado del sol?", "Neptuno")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de África?", "Monte Kilimanjaro")
agregar_pregunta_respuesta("¿Quién pintó 'La noche estrellada'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de África?", "Nigeria")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de cuerda más antiguo?", "La lira")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de Canadá?", "América del Norte")
agregar_pregunta_respuesta("¿Cuál es el metal más utilizado en la fabricación de aviones?", "Aluminio")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de Italia?", "Italiano")
agregar_pregunta_respuesta("¿Quién escribió 'Matar a un ruiseñor'?", "Harper Lee")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de África?", "Argelia")
agregar_pregunta_respuesta("¿Cuál es el animal más grande del mundo?", "La ballena azul")
agregar_pregunta_respuesta("¿Quién fue el inventor de la bombilla eléctrica?", "Thomas Edison")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra de los vikingos'?", "Noruega")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La ciudad eterna'?", "Roma")
agregar_pregunta_respuesta("¿Quién escribió 'Crimen y castigo'?", "Fyodor Dostoyevsky")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del sodio?", "Na")
agregar_pregunta_respuesta("¿Cuál es el hueso más pequeño del cuerpo humano?", "El estribo")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de América del Norte?", "Monte Denali")
agregar_pregunta_respuesta("¿Quién pintó 'La última cena'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño de África?", "Seychelles")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor diversidad de especies?", "América del Sur")
agregar_pregunta_respuesta("¿Quién escribió 'La Odisea'?", "Homero")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de México?", "Peso mexicano")
agregar_pregunta_respuesta("¿Cuál es la capital de Italia?", "Roma")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Estambul?", "Turquía")
agregar_pregunta_respuesta("¿Cuál es el río más largo de Europa?", "Río Volga")
agregar_pregunta_respuesta("¿Cuál es el océano más profundo del mundo?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Quién escribió 'Orgullo y prejuicio'?", "Jane Austen")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del plomo?", "Pb")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la insulina?", "El páncreas")
agregar_pregunta_respuesta("¿Cuál es el planeta más grande del sistema solar?", "Júpiter")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Europa?", "Monte Elbrus")
agregar_pregunta_respuesta("¿Quién pintó 'La Mona Lisa'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de Europa?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de teclado más antiguo?", "El órgano")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de India?", "Asia")
agregar_pregunta_respuesta("¿Cuál es el metal más utilizado en la fabricación de automóviles?", "Acero")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de España?", "Español")
agregar_pregunta_respuesta("¿Quién escribió 'En busca del tiempo perdido'?", "Marcel Proust")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de Europa?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el animal más pesado del mundo?", "La ballena azul")
agregar_pregunta_respuesta("¿Quién fue el inventor del teléfono?", "Alexander Graham Bell")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra de los tulipanes'?", "Países Bajos")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La ciudad eterna'?", "Roma")
agregar_pregunta_respuesta("¿Quién escribió 'El principito'?", "Antoine de Saint-Exupéry")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del mercurio?", "Hg")
agregar_pregunta_respuesta("¿Cuál es el hueso más largo del cuerpo humano?", "El fémur")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Europa Occidental?", "Monte Blanc")
agregar_pregunta_respuesta("¿Quién pintó 'Los girasoles'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño de Europa?", "Vaticano")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor número de países?", "África")
agregar_pregunta_respuesta("¿Quién escribió 'Don Quijote de la Mancha'?", "Miguel de Cervantes Saavedra")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Japón?", "Yen")
agregar_pregunta_respuesta("¿Cuál es la capital de Italia?", "Roma")
agregar_pregunta_respuesta("¿En qué país se encuentra la ciudad de Estambul?", "Turquía")
agregar_pregunta_respuesta("¿Cuál es el río más largo de Europa?", "Río Volga")
agregar_pregunta_respuesta("¿Cuál es el océano más profundo del mundo?", "Océano Pacífico")
agregar_pregunta_respuesta("¿Quién escribió 'Orgullo y prejuicio'?", "Jane Austen")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del plomo?", "Pb")
agregar_pregunta_respuesta("¿Cuál es el órgano encargado de la producción de la insulina?", "El páncreas")
agregar_pregunta_respuesta("¿Cuál es el planeta más grande del sistema solar?", "Júpiter")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Europa?", "Monte Elbrus")
agregar_pregunta_respuesta("¿Quién pintó 'La Mona Lisa'?", "Leonardo da Vinci")
agregar_pregunta_respuesta("¿Cuál es el país más poblado de Europa?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el instrumento musical de teclado más antiguo?", "El órgano")
agregar_pregunta_respuesta("¿En qué continente se encuentra el país de India?", "Asia")
agregar_pregunta_respuesta("¿Cuál es el metal más utilizado en la fabricación de automóviles?", "Acero")
agregar_pregunta_respuesta("¿Cuál es el idioma oficial de España?", "Español")
agregar_pregunta_respuesta("¿Quién escribió 'En busca del tiempo perdido'?", "Marcel Proust")
agregar_pregunta_respuesta("¿Cuál es el país más extenso de Europa?", "Rusia")
agregar_pregunta_respuesta("¿Cuál es el animal más pesado del mundo?", "La ballena azul")
agregar_pregunta_respuesta("¿Quién fue el inventor del teléfono?", "Alexander Graham Bell")
agregar_pregunta_respuesta("¿Cuál es el país conocido como 'La tierra de los tulipanes'?", "Países Bajos")
agregar_pregunta_respuesta("¿Cuál es la ciudad conocida como 'La ciudad eterna'?", "Roma")
agregar_pregunta_respuesta("¿Quién escribió 'El principito'?", "Antoine de Saint-Exupéry")
agregar_pregunta_respuesta("¿Cuál es el símbolo químico del mercurio?", "Hg")
agregar_pregunta_respuesta("¿Cuál es el hueso más largo del cuerpo humano?", "El fémur")
agregar_pregunta_respuesta("¿Cuál es la montaña más alta de Europa Occidental?", "Monte Blanc")
agregar_pregunta_respuesta("¿Quién pintó 'Los girasoles'?", "Vincent van Gogh")
agregar_pregunta_respuesta("¿Cuál es el país más pequeño de Europa?", "Vaticano")
agregar_pregunta_respuesta("¿Cuál es el continente con mayor número de países?", "África")
agregar_pregunta_respuesta("¿Quién escribió 'Don Quijote de la Mancha'?", "Miguel de Cervantes Saavedra")
agregar_pregunta_respuesta("¿Cuál es la moneda oficial de Japón?", "Yen")

# Variable para almacenar la pregunta actual
pregunta_actual = ""

# Variable para controlar si se ha hecho clic en "Comprobar"
comprobar_clicado = False

# Función que se ejecutará cuando se haga clic en el botón "Omitir"
def boton1_clic():
    global pregunta_actual
    pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
    # Evitar seleccionar la misma pregunta actual
    while pregunta_aleatoria == pregunta_actual:
        pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
    cuadro_texto.config(text=pregunta_aleatoria)
    respuesta.set("Aquí sale la respuesta")
    cuadro_respuesta.delete(0, END)
    pregunta_actual = pregunta_aleatoria

# Función que se ejecutará cuando se haga clic en el botón "Siguiente"
def boton2_clic():
    global pregunta_actual, comprobar_clicado
    if comprobar_clicado:
        pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
        # Evitar seleccionar la misma pregunta actual
        while pregunta_aleatoria == pregunta_actual:
            pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
        cuadro_texto.config(text=pregunta_aleatoria)
        respuesta.set("Aquí sale la respuesta")
        cuadro_respuesta.delete(0, END)
        pregunta_actual = pregunta_aleatoria
        comprobar_clicado = False
        boton2.config(state=NORMAL)
    else:
        messagebox.showinfo("ON LIVE", "Primero debes hacer clic en 'Comprobar'.")

# Función que se ejecutará cuando se haga clic en el botón "Comprobar"
def boton3_clic():
    global comprobar_clicado
    pregunta_actual = cuadro_texto.cget("text")
    respuesta_correcta = buscar_respuesta(pregunta_actual)
    respuesta_usuario = cuadro_respuesta.get()
    if respuesta_usuario.lower() == respuesta_correcta.lower():
        respuesta.set("Tu respuesta es correcta")
    else:
        respuesta.set("La respuesta correcta es: " + respuesta_correcta)
    comprobar_clicado = True
    boton2.config(state=NORMAL)

# Crear la ventana principal
ventana = Tk()
ventana.title("ON LIVE")
ventana.geometry("1920x1080")
ventana.config(bg="white")

# Crear un cuadro de texto en el centro de la ventana superior
cuadro_texto = Label(ventana, width=20, bg="black", fg="medium violet red", font=("gabriola", 50), relief=FLAT)
cuadro_texto.place(x=-5, y=0, width=1920, height=100)

# Barra inferior de respuesta
respuesta = StringVar()
respuesta.set("Aquí sale la respuesta")
cuadro_respuesta = Entry(ventana, width=30, bg="medium violet red", font=("courier", 20), relief=FLAT)
cuadro_respuesta.place(x=680, y=700)
cuadro_texto_respuesta = Label(ventana, textvariable=respuesta, width=60, bg="medium violet red", fg="black", font=("gabriola", 58), relief=FLAT)
cuadro_texto_respuesta.place(x=0, y=890)

# Crear los dos botones de cambio entre preguntas
boton1 = Button(ventana, text="Omitir", command=boton1_clic, bg="black", fg="medium violet red", font=("gabriola", 20), padx=10, pady=5, relief=FLAT)
boton1.pack(side="left", padx=10)

boton2 = Button(ventana, text="Siguiente", command=boton2_clic, bg="medium violet red", fg="black", font=("gabriola", 20), padx=10, pady=5, relief=FLAT)
boton2.pack(side="right", padx=10)
boton2.config(state=NORMAL)

boton3 = Button(ventana, text="Comprobar", command=boton3_clic, bg="gray", fg="blue", font=("gabriola", 20), padx=10, pady=5, relief=FLAT)
boton3.place(x=850, y=480)

# Seleccionar una pregunta aleatoria y mostrarla en el cuadro de texto
pregunta_aleatoria = choice(list(preguntas_respuestas.keys()))
cuadro_texto.config(text=pregunta_aleatoria)
pregunta_actual = pregunta_aleatoria

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
