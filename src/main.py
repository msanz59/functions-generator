import dearpygui.dearpygui as dpg
from etc.variables import Variables as vars
dpg.create_context()

import gui.themes as themes

with dpg.window(label="Example Window", tag="main_window", width=800, height=600, no_resize=True, no_move=True, no_collapse=True, no_title_bar=True):
    dpg.add_text("Bienvenido al generador de funciones:", color=(255, 255, 100))
    dpg.add_separator()
    dpg.add_text("Elija el lenguaje de su preferencia:")
    dpg.add_combo(["Python", "JavaScript", "C++", "Java", "Rust"], 
                  default_value="Python", callback=lambda s, a: vars.set_language(a))
    dpg.add_separator()
    dpg.add_text("Introduzazca los parámetros de la función: ({'param1': 'value1', 'param2': 'value2'} o deje {} para ninguno)")
    dpg.add_input_text(label="Parámetros", default_value="{}", width=400, 
                       callback=lambda s, a: vars.set_function_parameters(a))
    dpg.add_separator()

    dpg.add_text("Introduzca el output de la función: (deje vacío para ninguno)")
    dpg.add_input_text(label="Output", default_value="", width=400, 
                       callback=lambda s, a: vars.set_function_output(a))
    
    dpg.add_separator()


    dpg.add_text("Introduzca el enfoque del codigo generado:")
    dpg.add_radio_button(["Simplicidad de codigo", "Optimización [O(x)]"], 
                         callback=lambda s, a: vars.set_focus_mode(a))
    
    dpg.add_separator()

    dpg.add_button(label="Generar Función", width=200, height=50,indent=300 ,  
                   callback=lambda: print("Función generada con los parámetros seleccionados."))
    

    
with dpg.window(label="Opciones del programa", tag="options_window", width=800, height=200, no_resize=True, no_move=True):
    dpg.add_text("Seleccione el tema de la aplicación:")
    dpg.add_radio_button(["Global", "Dark"], 
                         callback=lambda s, a: vars.set_theme(a))

dpg.create_viewport(title="Functions Generator", width=800, height=800, resizable=False)
dpg.setup_dearpygui()

# Posicionar las ventanas
dpg.set_item_pos("main_window", [0, 0])
dpg.set_item_pos("options_window", [0, 600])

# Aplicar el tema global
dpg.bind_theme(themes.global_theme)

dpg.set_primary_window("main_window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()