import dearpygui.dearpygui as dpg

# Nota: Este archivo se importa DESPUÉS de crear el contexto en main
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (80, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (80, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (100, 120, 140, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 120, 140, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (120, 140, 160, 255))

with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (50, 50, 50, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (60, 60, 60, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (80, 80, 80, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (80, 80, 80, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (100, 100, 100, 255))

with dpg.theme() as dracula_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (40, 42, 54, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (68, 71, 90, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (98, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (98, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (120, 122, 140, 255))
    


# Dict to hold themes for easy access
themes = {
    "global": global_theme,
    "dark": dark_theme,
    "dracula": dracula_theme
}