import ctypes
myappid = 'mycompany.myproduct.subproduct.'  
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import dearpygui.dearpygui as dpg
from etc.variables import Variables as vars
import os
dpg.create_context()

import gui.themes as themes

base_dir = os.path.dirname(__file__)
small_image_dir = os.path.join(base_dir, "gui", "icons", "small_icon.ico")
large_image_dir = os.path.join(base_dir, "gui", "icons", "large_icon.ico")

# Load configuration on start
vars.read_config()
def toggle_settings_window():
    if dpg.is_item_shown("options_window"):
        dpg.hide_item("options_window")
        vars.set_checkbox_state(False)
        window_height = 600
    else:
        dpg.show_item("options_window")
        vars.set_checkbox_state(True)
        window_height = 800
    dpg.set_viewport_height(window_height)
def apply_theme(theme_name):
    theme = themes.themes.get(theme_name, themes.themes["global"])
    dpg.bind_theme(theme)
    vars.set_theme(theme_name)

with dpg.window(label="Program", tag="main_window", width=800, height=600, no_resize=True, no_move=True, no_collapse=True, no_title_bar=True):
    dpg.add_text("Welcome to the function generator:", color=(255, 255, 100))
    dpg.add_checkbox(label="Enable advanced options", default_value=vars.checkbox_state, callback=lambda s, a: toggle_settings_window())
    dpg.add_separator()
    dpg.add_text("Choose your preferred language:")
    dpg.add_combo(["Python", "JavaScript", "C++", "Java", "Rust"], 
                  default_value=vars.language_selected if vars.language_selected else "Python", callback=lambda s, a: vars.set_language(a))
    dpg.add_separator()
    dpg.add_text("Enter the function parameters: ({'param1': 'value1', 'param2': 'value2'} or leave {} for none)")
    dpg.add_input_text(label="Parameters", default_value=str(vars.function_parameters) if vars.function_parameters else "{}", width=400, 
                       callback=lambda s, a: vars.set_function_parameters(a))
    dpg.add_separator()

    dpg.add_text("Enter the function output: (leave empty for none)")
    dpg.add_input_text(label="Output", default_value=vars.function_output if vars.function_output is not None else "", width=400, 
                       callback=lambda s, a: vars.set_function_output(a))

    
    dpg.add_separator()


    dpg.add_text("Enter the focus of the generated code:")
    dpg.add_radio_button(["Code simplicity", "Optimization [O(x)]"], default_value=vars.focus_mode, 
                         callback=lambda s, a: vars.set_focus_mode(a))
    
    dpg.add_separator()

    dpg.add_text("Enter a brief description of the function to be generated:")
    dpg.add_input_text(label="", default_value=vars.description_text if vars.description_text else "", width=600, height=100, multiline=True, 
                       callback=lambda s, a: vars.set_description_text(a))
    
    dpg.add_separator()

    dpg.add_button(label="Generate Function", width=200, height=50,indent=300 ,  
                   callback=lambda: print("Function generated with the selected parameters."))
    

    
with dpg.window(label="Program Options", tag="options_window", width=800, height=200, no_resize=True, no_move=True, no_collapse=True, show=False):
    dpg.add_text("Select the application theme:")
    dpg.add_radio_button(["global", "dark", "dracula", "terra"], default_value=vars.theme_selected, 
                         callback=lambda s, a: apply_theme(a))

dpg.create_viewport(title="Functions Generator", width=800, height=600, resizable=False, small_icon=small_image_dir, large_icon=large_image_dir)
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