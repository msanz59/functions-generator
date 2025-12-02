import dearpygui.dearpygui as dpg


with dpg.theme() as aqua:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (70, 90, 110, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (80, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (100, 120, 140, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 120, 140, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (120, 140, 160, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (90, 110, 130, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (110, 130, 150, 255))
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (140, 160, 180, 255))

        dpg.add_theme_color(dpg.mvThemeCol_Header, (90, 110, 130, 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (110, 130, 150, 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (130, 150, 170, 255))
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (70, 90, 110, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (90, 110, 130, 255))

with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (50, 50, 50, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (60, 60, 60, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (80, 80, 80, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (80, 80, 80, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (100, 100, 100, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (70, 70, 70, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (90, 90, 90, 255))
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (120, 120, 120, 255))

        dpg.add_theme_color(dpg.mvThemeCol_Header, (70, 70, 70, 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (90, 90, 90, 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (110, 110, 110, 255))
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (45, 45, 45, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (70, 70, 70, 255))

with dpg.theme() as dracula_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (40, 42, 54, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (68, 71, 90, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (98, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (98, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (120, 122, 140, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (248, 248, 242, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (68, 71, 90, 255))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (88, 91, 110, 255))
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (139, 233, 253, 255))

        dpg.add_theme_color(dpg.mvThemeCol_Header, (68, 71, 90, 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (98, 100, 120, 255))
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (139, 233, 253, 255)) 
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (40, 42, 54, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (68, 71, 90, 255))

with dpg.theme() as terra_theme: 
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (139, 125, 107, 255))  
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (119, 136, 102, 255))   
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (144, 161, 127, 255)) 
        dpg.add_theme_color(dpg.mvThemeCol_Button, (144, 161, 127, 255))   
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (164, 181, 147, 255))  
        dpg.add_theme_color(dpg.mvThemeCol_Text, (40, 35, 30, 255))         
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (159, 145, 127, 255))   
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (179, 165, 147, 255))  
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (96, 108, 85, 255))   

        dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (129, 146, 112, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Header, (129, 146, 112, 255))  
        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (154, 171, 137, 255))  
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (174, 191, 157, 255))
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (149, 135, 117, 255))

# Dict to hold themes for easy access
themes = {
    "aqua": aqua,
    "dark": dark_theme,
    "dracula": dracula_theme,
    "terra": terra_theme
}