from helpers import text, hyperlink

def revisar(answer):
    if answer == 7680:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_03.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


if __name__ == "__main__":
    revisar(None)
    revisar((201 + 759) * 2 ** 3)
    revisar("2")
