

def load_play(directory: str) -> dict[str, dict]:
    """Loads the scenes of a play from the given directory.

    Args:
        directory (str): Path to the directory which contains the scenes.

    Returns:
        A dict where the keys are the scene names (filename without ext.), values are
        dicts containing character names and speeches.

    Raises:
        FileNotFoundError: The directory was not found.
    """
    return {}  # TODO


def get_speech_count(play: dict[str, dict]) -> int:
    """Counts the total number of speeches in all scenes of a play.

    Args:
        play (dict[str, dict]): Names and speeches of a scene.

    Returns:
        int: The total number of speeches.
    """
    return 0  # TODO
