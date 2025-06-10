from helpers import text, hyperlink
import statistics

def revisar(respuesta):
    mean = statistics.mean([19.5, 22.3, 12, 10.01, 32, 29.99, 20.89])
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == mean:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_05.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    revisar(None)
    revisar(statistics.mean([19.5, 22.3, 12, 10.01, 32, 29.99, 20.89]))
    revisar(False)
