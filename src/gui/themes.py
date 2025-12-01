import dearpygui.dearpygui as dpg

# Nota: Este archivo se importa DESPUÉS de crear el contexto en main
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (80, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (80, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (100, 120, 140, 255))

with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (50, 50, 50, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (60, 60, 60, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (80, 80, 80, 255))