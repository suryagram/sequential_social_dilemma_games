import tensorflow as tf

from ray.rllib.models.preprocessors import Preprocessor


class MultiInputPreprocessor(Preprocessor):
    def _init_shape(self, obs_space, options):
        pass

    def transform(self, observation):
        pass
