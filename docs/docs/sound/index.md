# Sound

The `wolpie.sound` package provides simple utilities for playing sound files.

[📚 Full API Reference](../api/sound.md){ .md-button }

## Functions

### `play_sound`

This function is based on the work done by [playsound](https://pypi.org/project/playsound/). I didn't like the way it was structured, so I rewrote it to fit my needs. Currently, it only supports Windows, but I plan to add support for other platforms in the future.

I required a lightweight way to play sound files so that I could use it in my [ding context manager](#ding).

### `ding`

A context manager that plays a sound when the block of code inside it is done executing. By default, it plays a "ding" sound included with Wolpie, but you can specify your own.
