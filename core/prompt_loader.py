class PromptLoader:
    
    def __init__(self, prompt_directory: str):
        self._prompt_directory = prompt_directory

    def load_prompt(self, prompt_name: str) -> str:
        # Placeholder for loading a prompt from the specified directory
        print(f"Loading prompt '{prompt_name}' from directory '{self._prompt_directory}'")
        return f"Prompt content for {prompt_name}"