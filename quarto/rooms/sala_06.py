from helpers import text, hyperlink

def revisar(respuesta):
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == 27.75:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_07.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    revisar(None)
    revisar(27.75)
    revisar(False)
