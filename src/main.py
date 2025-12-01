import dearpygui.dearpygui as dpg
from etc.variables import Variables as vars
dpg.create_context()

import gui.themes as themes

# Load configuration on start
vars.read_config()

def apply_theme(theme_name):
    theme = themes.themes.get(theme_name, themes.themes["global"])
    dpg.bind_theme(theme)
    vars.set_theme(theme_name)

with dpg.window(label="Program", tag="main_window", width=800, height=600, no_resize=True, no_move=True, no_collapse=True, no_title_bar=True):
    dpg.add_text("Welcome to the function generator:", color=(255, 255, 100))
    dpg.add_separator()
    dpg.add_text("Choose your preferred language:")
    dpg.add_combo(["Python", "JavaScript", "C++", "Java", "Rust"], 
                  default_value="Python", callback=lambda s, a: vars.set_language(a))
    dpg.add_separator()
    dpg.add_text("Enter the function parameters: ({'param1': 'value1', 'param2': 'value2'} or leave {} for none)")
    dpg.add_input_text(label="Parameters", default_value="{}", width=400, 
                       callback=lambda s, a: vars.set_function_parameters(a))
    dpg.add_separator()

    dpg.add_text("Enter the function output: (leave empty for none)")
    dpg.add_input_text(label="Output", default_value="", width=400, 
                       callback=lambda s, a: vars.set_function_output(a))
    
    dpg.add_separator()


    dpg.add_text("Enter the focus of the generated code:")
    dpg.add_radio_button(["Code simplicity", "Optimization [O(x)]"], 
                         callback=lambda s, a: vars.set_focus_mode(a))
    
    dpg.add_separator()

    dpg.add_button(label="Generate Function", width=200, height=50,indent=300 ,  
                   callback=lambda: print("Function generated with the selected parameters."))
    

    
with dpg.window(label="Program Options", tag="options_window", width=800, height=200, no_resize=True, no_move=True):
    dpg.add_text("Select the application theme:")
    dpg.add_radio_button(["global", "dark"], 
                         callback=lambda s, a: apply_theme(a))

dpg.create_viewport(title="Functions Generator", width=800, height=800, resizable=False)
dpg.setup_dearpygui()

# Posicionar las ventanas
dpg.set_item_pos("main_window", [0, 0])
dpg.set_item_pos("options_window", [0, 600])

# Aplicar el tema global
theme_selected = vars.theme_selected
theme = themes.themes[theme_selected] 
dpg.bind_theme(theme)

dpg.set_primary_window("main_window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# Save config on exit
vars.write_config()