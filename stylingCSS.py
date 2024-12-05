from nicegui import ui

ui.icon('thumb_up', color='#b0304b').classes('text-6xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Angel').style('color: #b0304b; font-weight: bold ;    font-family: "Georgia"; font-size: 24px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()