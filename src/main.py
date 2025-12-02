import ctypes
myappid = 'mycompany.myproduct.subproduct.'  
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
from dotenv import set_key
import dearpygui.dearpygui as dpg
from etc.variables import Variables as vars
import os
import threading
from AI_Calls.gemini import generate_function
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
        vars.check()
        window_height = 600
    else:
        dpg.show_item("options_window")
        vars.check()
        window_height = 800
    dpg.set_viewport_height(window_height)

def apply_theme(theme_name):
    theme = themes.themes.get(theme_name, themes.themes["dark"])
    dpg.bind_theme(theme)
    vars.set_theme(theme_name)

def update_after_generation(function_code):

    try:
        dpg.configure_item("generating_popup", show=False)
        dpg.set_value("output_textbox", function_code)
        dpg.show_item("output_popup")
    except Exception as e:
        print("Error on update_after_generation:", e)

def gen_in_thread():
    # Tries to run the generation in a separate thread to avoid freezing the GUI
    try:
        language = vars.language_selected
        parameters = vars.function_parameters
        output = vars.function_output
        focus_mode = vars.focus_mode
        description = vars.description_text

        function_code = generate_function(language, parameters, output, focus_mode, description)
        print("Generated Function:\n", function_code)
        update_after_generation(function_code)

    except Exception as e:
        
        print("An error occurred during function generation:", str(e))
        dpg.hide_item("generating_popup")

def gen_function():

    dpg.configure_item("generating_popup", show=True)
    thread = threading.Thread(target=gen_in_thread)
    thread.daemon = True
    thread.start()

def save_gemini_key():
    try:
        api_key = dpg.get_value("api_key_input")
        if api_key and api_key.strip():  
            set_key("src/.env", "GEMINI_API_KEY", api_key.strip())
            print("API Key saved successfully!")
            dpg.hide_item("gemini_config")
        else:
            print("Please enter a valid API key")
    except Exception as e:
        print(f"Error saving API key: {e}")



with dpg.window(label="Program", tag="main_window", width=800, height=600, no_resize=True, no_move=True, no_collapse=True, no_title_bar=True):
    dpg.add_text("Welcome to the function generator:", color=(255, 255, 100))
    dpg.add_checkbox(label="Enable advanced options", default_value=vars.checkbox_state, callback=lambda s, a: toggle_settings_window())
    dpg.add_separator()
    dpg.add_text("Choose your preferred language:")
    dpg.add_combo(["Python", "JavaScript", "C++", "Java", "Rust"], 
                  default_value=vars.language_selected if vars.language_selected else "Python", callback=lambda s, a: vars.set_language(a))
    dpg.add_separator()
    dpg.add_text("Enter the function parameters: ({'param1': 'type1', 'param2': 'type2'} or leave {} for none)")
    dpg.add_input_text(label="Parameters", default_value=str(vars.function_parameters) if vars.function_parameters else "{}", width=400, 
                       callback=lambda s, a: vars.set_function_parameters(a))
    dpg.add_separator()

    dpg.add_text("Enter the function output: (leave empty for none)")
    dpg.add_input_text(label="Output", default_value=vars.function_output if vars.function_output is not None else "", width=400, 
                       callback=lambda s, a: vars.set_function_output(a))

    
    dpg.add_separator()


    dpg.add_text("Enter the focus of the generated code:")
    dpg.add_radio_button(["Code simplicity", "Optimization [O(best possible)]"], default_value=vars.focus_mode, 
                         callback=lambda s, a: vars.set_focus_mode(a))
    
    dpg.add_separator()

    dpg.add_text("Enter a brief description of the function to be generated:")
    dpg.add_input_text(label="", default_value=vars.description_text if vars.description_text else "", width=600, height=100, multiline=True, 
                       callback=lambda s, a: vars.set_description_text(a))
    
    dpg.add_separator()

    dpg.add_button(tag="generate_function_button", label="Generate Function", width=200, height=50,indent=300 ,  
                   callback=lambda: gen_function())
    
show_settings = vars.checkbox_state
    
with dpg.window(label="Program Options", tag="options_window", width=800, height=200, no_resize=True, no_move=True, no_collapse=True, show=show_settings):
    dpg.add_text("Select the application theme:")

    with dpg.group(horizontal=True):
        dpg.add_radio_button(["aqua", "dark", "dracula", "terra"], default_value=vars.theme_selected, 
                            callback=lambda s, a: apply_theme(a))
        dpg.add_button(label="Change Gemini's API Key", width=300, height=25, callback=lambda: dpg.show_item("gemini_config"))
    
with dpg.window(label="Generating Function", tag="generating_popup", modal=True, show=False, no_resize=True, width=300, height=100, pos=[250, 200]):
    dpg.add_text("Your answer is being generated...")
    dpg.add_separator()
    dpg.add_button(label="Close", width=75, height=25, callback=lambda: dpg.hide_item("generating_popup"))

with dpg.window(label="Generated!", tag="output_popup", show=False, no_resize=True, width=600, height=400, pos=[100, 100]):
    dpg.add_text("Here is your generated function:")
    dpg.add_separator()
    dpg.add_input_text(label="", tag="output_textbox", width=550, height=300, multiline=True)
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="Copy to Clipboard", width=150, height=25, 
                       callback=lambda: dpg.set_clipboard_text(dpg.get_value("output_textbox")))
        dpg.add_button(label="Close", width=75, height=25, callback=lambda: dpg.hide_item("output_popup"))

with dpg.window(label="Gemini API Key", tag="gemini_config", show=False):
    dpg.add_text("Enter your Gemini API Key:")
    dpg.add_input_text(label="API Key", tag="api_key_input", width=400, default_value=os.getenv("GEMINI_API_KEY") if os.getenv("GEMINI_API_KEY") else "")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="Save API Key", width=120, height=30, callback=save_gemini_key)
        dpg.add_button(label="Cancel", width=80, height=30, callback=lambda: dpg.hide_item("gemini_config"))

viewport_height = 600 if not vars.checkbox_state else 800
dpg.create_viewport(title="Functions Generator", width=800, height=viewport_height, resizable=False, small_icon=small_image_dir, large_icon=large_image_dir)
dpg.setup_dearpygui()

# Position the windows
dpg.set_item_pos("main_window", [0, 0])
dpg.set_item_pos("options_window", [0, 600])

# Apply saved theme
theme_selected = vars.theme_selected
theme = themes.themes[theme_selected] 
dpg.bind_theme(theme)

dpg.set_primary_window("main_window", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# Save config on exit
vars.write_config()

