

def load_scene(filename: str) -> dict[str, list[str]]:
    """Loads the script of a scene from file and returns the speeches of each character.

    It is assumed that the file contains speeches, where each speech:
    - starts with a line containing only the uppercase name of the speaking character
    - followed by the lines of the speech
    - ended by an empty line

    Args:
        filename (str): Path to a textfile containing the script of a scene.

    Returns:
        A dict where the keys are the character names and the values are lists
        containing speeches said by the character in the scene.
        Each speech may contain multiple lines.

    Raises:
        FileNotFoundError: The file was not found.
    """
    return {}  # TODO
