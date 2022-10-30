import PySimpleGUI as sg

# criando layout
def janela_inicio():
  sg.theme('Dark Blue 3')
  linha = [
    # Checkbox = n1 image/  # Input = n2 image/
    [sg.Checkbox(''), sg.Input('')]
  ]
  layout = [
    [sg.Frame('Tarefas', layout=linha, key='container')],
    [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
  ]
  
  return sg.Window('Todo List', layout=layout, finalize=True)

# criando janela
janela = janela_inicio()

# criando as regras da janela
while True:
  event, values = janela.read()
  if event == sg.WIN_CLOSED:
    break
  # Nova Tarefa - criando nova linha
  elif event == 'Nova Tarefa':
    janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
  # Criando Reset
  elif event == 'Resetar':
    janela.close()
    janela = janela_inicio()
  