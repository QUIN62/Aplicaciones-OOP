from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('CLIC', on_click=lambda: ui.notify('GAY'))
with ui.row():
    ui.checkbox('CAJITA', on_change=show)
    ui.switch('CAMBIO', on_change=show)
ui.radio(['PIM', 'PAM', 'PUM'], value='PAM', on_change=show).props('incline')
with ui.row():
    ui.input('ESCRIBE TU NOMBRE', on_change=show)
    ui.select(['UP', 'DOWN'], value='UP', on_change=show)
ui.link('MAS INFO...', '/documentation').classes('mt-8')

ui.run()