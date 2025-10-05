# CREDS: https://pypi.org/project/playsound/

import abc
import logging
import warnings
from contextlib import contextmanager
from pathlib import Path
from platform import system
from typing import Generator

logger = logging.getLogger(__name__)
DEFAULT_DING_FILE = Path(__file__).resolve().parent / "ding.mp3"
SUPPORTED_PLATFORMS = ["Windows"]


class PlaySoundError(Exception):
    pass


class PlaySoundInterface(abc.ABC):
    @abc.abstractmethod
    def _play_sound(
        self,
        sound: str | Path,
        block: bool = True,
    ) -> None:
        """A function that will play `*.mp3` and `*.wav` sound files.

        .. warning::
            This function is only officially supported on Windows.

        Example usage:

        .. code-block:: python

            from wolpie import play_sound
            # or from wolpie.sound import play_sound

            play_sound("path/to/sound/file.mp3")

        .. tip::
            If you want sound files, consider https://pixabay.com/sound-effects/search

        :param str | Path sound: The sound file to play.
        :param bool block: If True, the function will block until the sound has finished playing.
        :raises PlaySoundError: If there was an error playing the sound.
        """
        ...


class WinPlaySound(PlaySoundInterface):
    def _play_sound(
        self,
        sound: str | Path,
        block: bool = True,
    ) -> None:
        _sound = Path(sound)
        if not _sound.exists():
            _err = f"Sound file does not exist: {sound}"
            raise PlaySoundError(_err)
        if _sound.suffix.lower() not in {".mp3", ".wav"}:
            _err = f"Unsupported sound file format: {sound}. Only .mp3 and .wav are supported."
            raise PlaySoundError(_err)

        sound = '"' + str(_sound) + '"'

        from ctypes import create_unicode_buffer, windll, wintypes

        windll.winmm.mciSendStringW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.UINT, wintypes.HANDLE]
        windll.winmm.mciGetErrorStringW.argtypes = [wintypes.DWORD, wintypes.LPWSTR, wintypes.UINT]

        def win_command(*command):
            buf_len = 600
            buf = create_unicode_buffer(buf_len)
            command = " ".join(command)
            winmm = windll.winmm
            error_code = int(winmm.mciSendStringW(command, buf, buf_len - 1, 0))
            if error_code:
                error_buffer = create_unicode_buffer(buf_len)
                winmm.mciGetErrorStringW(error_code, error_buffer, buf_len)
                exception_message = (
                    f"\n    Error {error_code} for command:\n        {command[0]}\n    {error_buffer.value}"
                )
                logger.error(exception_message)
                raise PlaySoundError(exception_message)

        try:
            win_command(f"open {sound}")
            win_command("play {}{}".format(sound, " wait" if block else ""))
        finally:
            try:
                win_command(f"close {sound}")
            except PlaySoundError:
                logger.warning("Failed to close the file: {}".format(sound))
                # If it fails, there's nothing more that can be done...
                pass


class NotImplementedPlaySound(PlaySoundInterface):
    def _play_sound(
        self,
        sound: str | Path,
        block: bool = True,
    ) -> None:
        _err = f"play_sound is not implemented for {current_system}. Could not play sound: {sound} with block={block}"
        logger.warning(_err)


match current_system := system():
    case "Windows":
        play_sound = WinPlaySound()._play_sound
    case _:
        warnings.warn(
            message=(
                f"Platform {current_system} is not officially supported. Supported platforms: {SUPPORTED_PLATFORMS}."
                "Playing sounds may not work as expected."
            ),
            stacklevel=2,
        )
        play_sound = NotImplementedPlaySound()._play_sound


@contextmanager
def ding(
    sound: str | Path = DEFAULT_DING_FILE,
) -> Generator[None, None, None]:
    """A context manager that plays a "ding" sound when the block of code inside the context manager finishes executing.

    If if fails to play the "ding", it won't raise any errors. After all.. the whole idea of this context
    manager is to notify you when a long running function is done. Imagine you wait 2 hours
    just for the nice sound file to fail. And you have to start from scratch. No thanks.

    .. warning::
        This function is only officially supported on Windows.

    Uses :func:`play_sound` under the hood.

    Example usage:

    .. code-block:: python

        from wolpie import ding
        import time

        # plays the default "ding" sound after the block finishes
        with ding():
            time.sleep(10)  # Simulate some long running function

        # or if you have a cooler ding:
        with ding("path/to/cooler/ding.mp3"):
            time.sleep(10)  # Simulate some long running function

    .. tip::
        If you want sound files, consider https://pixabay.com/sound-effects/search

    :param str | Path sound: The sound file to play. Defaults to a built-in "ding" sound.
    :yield Generator[None, None, None]: Yields nothing.
    """
    try:
        yield
    finally:
        try:
            play_sound(sound, block=True)
        except Exception as e:
            logger.warning(f"Failed to play sound {sound}: {e}")
