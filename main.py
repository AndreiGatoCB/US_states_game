import turtle
import pandas

pantalla = turtle.Screen()
pantalla.title("A.C.A.B. US States Game")
image = "blank_states_img.gif"
pantalla.addshape(image)
turtle.shape(image)

datos = pandas.read_csv("50_states.csv")
all_states = datos.state.to_list()
estados_acertados = []

while len(estados_acertados) < 50:
    answer_state = pantalla.textinput(title=f"{len(estados_acertados)}/50 estados correctos. ",
                                      prompt="Ingresa otro estado").title()
    if answer_state == "Exit":
        missing_states = [estado for estado in all_states if estado not in estados_acertados]
        nuevos_datos = pandas.DataFrame(missing_states)
        nuevos_datos.to_csv('estados_faltantes.csv')

        break
    if answer_state in all_states:
        estados_acertados.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        datos_estado = datos[datos.state == answer_state]
        t.goto(int(datos_estado.x), int(datos_estado.y))
        t.write(answer_state)
