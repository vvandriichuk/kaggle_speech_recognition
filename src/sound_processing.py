# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile


def scale_sound(sound):
    """
    Min Max scaling
    :param sound:
    :return:
    """
    sound = sound.astype('int64')
    if np.max(sound) - np.min(sound) <= 0:
        raise ZeroDivisionError("Bad sound file: len={}, max={}, min={}".format(len(sound), np.max(sound), np.min(sound)))

    return ((sound - np.min(sound)) / (np.max(sound) - np.min(sound))).astype(np.float32)


def read_wav_file(fname):
    _, wav = wavfile.read(fname)
    try:
        return scale_sound(wav)
    except Exception as err:
        print("Warning: sound with empty data: {}. Cause: {}".format(fname, err))
        return wav.astype(np.float32)  # TODO: this files should be removed from dataset. But for now just return unchanged.
        # raise Exception("{}: {}".format(fname, err))