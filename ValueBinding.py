from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('Que tan gay    ', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=10).bind_value(demo, 'PORCENTAJE')
    ui.toggle({1: '10%', 2: '20%', 3: '30%',4: "40%",5: '50%', 6: '60%', 7: '70%',8: "80%",9: '90%', 10: '100%'}).bind_value(demo, 'PORCENTAJE')
    ui.number().bind_value(demo, 'PORCENTAJE')

ui.run()