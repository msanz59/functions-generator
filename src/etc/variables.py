import json

class Variables:
    checkbox_state = False
    language_selected = ""
    theme_selected = "dark"
    function_parameters = "{}"
    function_output = None
    focus_mode = "Code simplicity"
    description_text = ""

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
    @staticmethod
    def set_description_text(text):
        Variables.description_text = text
        print(f"Description text set to: {Variables.description_text}")

    def read_config():
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                jsonconfig = json.load(f)
                Variables.checkbox_state = jsonconfig.get("checkbox_state", False)
                Variables.language_selected = jsonconfig.get("language_selected", "")
                Variables.theme_selected = jsonconfig.get("theme_selected", "dark")
                Variables.function_parameters = jsonconfig.get("function_parameters", {})
                Variables.function_output = jsonconfig.get("function_output", None)
                Variables.focus_mode = jsonconfig.get("focus_mode", "Code simplicity")
                Variables.description_text = jsonconfig.get("description_text", "")
                print("Configuration loaded from config.json")

        except FileNotFoundError:
            print("No configuration file found. Using default settings.")

    def write_config():
        jsonconfig = {
            "checkbox_state": Variables.checkbox_state,
            "language_selected": Variables.language_selected,
            "theme_selected": Variables.theme_selected,
            "function_parameters": Variables.function_parameters,
            "function_output": Variables.function_output,
            "focus_mode": Variables.focus_mode,
            "description_text": Variables.description_text
        }
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(jsonconfig, f, ensure_ascii=False, indent=4)
        print("Configuration saved to config.json")