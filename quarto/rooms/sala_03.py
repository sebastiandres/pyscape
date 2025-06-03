from helpers import text, hyperlink

def revisar(answer):
    # \frac{1.23 + 2.34}{1 + 43/2} + 3 \times 2^{1.5}
    true_answer = ( (1.23 + 2.34) / (1 + (43 / 2) ) ) + (3 * 2**1.5)
    epsilon = 0.000001
    if type(answer) in [float, int] and abs(answer - true_answer) < epsilon:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_04.html", "success")
    elif answer == answer == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    revisar(None)
    revisar(5)
    revisar("2")
