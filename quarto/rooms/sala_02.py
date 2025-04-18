# types: warning, danger, success, info, primary
########################################################
# UTILIDADES
########################################################

def text(text="", type="info"):
    text_str = f'<div class="btn btn-{type}" w-100 h-100>{text}</div>'
    print(text_str)


def hyperlink(text, url, type="info"):
    text_str = f'<a href="{url}" class="btn btn-{type} w-100 h-100">{text}</a>'
    print(text_str)


########################################################
# SALONES
########################################################

def revisar(answer):
    #\frac{1.23 + 2.34}{1 + 43/2} + 3 \times 2^{1.5}
    true_answer = (1.23 + 2.34) / (1 + 43/2) + 3 * 2**1.5
    epsilon = 0.000001
    if type(answer) in [float, int] and abs(answer - true_answer) < epsilon:
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_end.html", "success")
    elif answer == None:
        text("Indica la solución asignando algún valor a la variable `respuesta`.", "info")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")


if __name__ == "__main__":
    revisar(None)
    revisar(5)
    revisar("2")
