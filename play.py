

def load_play(directory: str) -> dict[str, list[str]]:
    """Loads the scenes of a play from the given directory.

    Args:
        directory (str): Path to the directory which contains the scenes.

    Returns:
        A dict where the keys are the scene names (filename without ext.), values are
        lists containing the names of the speaking characters.

    Raises:
        FileNotFoundError: The directory was not found.
    """
    return {}  # TODO


def get_speech_count(play: dict[str, list[str]]) -> int:
    """Counts the total number of speeches in all scenes of a play.

    Args:
        play (dict[str, list[str]]): Scene names and character names.

    Returns:
        int: The total number of speeches.
    """
    return 0  # TODO
