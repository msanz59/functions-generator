class Variables:
    checkbox_state = False
    language_selected = ""
    theme_selected = ""
    function_parameters = {}
    function_output = None
    focus_mode = "Simplicidad de codigo"

    @staticmethod
    def check():
        Variables.checkbox_state = not Variables.checkbox_state
        print(f"Checkbox state is now: {Variables.checkbox_state}")

    @staticmethod
    def set_language(language):
        Variables.language_selected = language
        print(f"Language selected: {Variables.language_selected}")

    @staticmethod
    def set_theme(theme):
        Variables.theme_selected = theme
        print(f"Theme selected: {Variables.theme_selected}")
    @staticmethod
    def set_function_parameters(params):
        Variables.function_parameters = params
        print(f"Function parameters set to: {Variables.function_parameters}")

    @staticmethod
    def set_function_output(output):
        Variables.function_output = output
        print(f"Function output set to: {Variables.function_output}")

    @staticmethod
    def set_focus_mode(mode):
        Variables.focus_mode = mode
        print(f"Focus mode set to: {Variables.focus_mode}")