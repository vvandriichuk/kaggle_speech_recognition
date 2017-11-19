# -*- coding: utf-8 -*-
import unittest

from data_loader import load_train_data, get_silence, sampling


class TestDataLoader(unittest.TestCase):
    def test_load_data(self):
        train_df, valid_df = load_train_data('../../data/train/audio/*/**.wav', '../../data/train/validation_list.txt')
        self.assertTrue(train_df.shape[0] == 57929)
        self.assertTrue(valid_df.shape[0] == 6798)
        df = train_df.groupby('label').apply(sampling(7))
        print(df[df['label'] == 'silence'])

    def test_get_silence(self):
        train_df, valid_df = load_train_data('../../data/train/audio/*/**.wav', '../../data/train/validation_list.txt')
        get_silence(train_df)


if __name__ == '__main__':
    unittest.main()
