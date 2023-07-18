"""
This file contains the base wrapper class for OmnOmniGibson environments
Wrappers are useful for data collection and logging. Highly recommended.
"""


class BaseWrapper:
    """
    Base class for all wrappers in OmniGibson

    Args:
        env (OmniGibsonEnv): The environment to wrap.
    """

    def __init__(self, env):
        self.env = env

    @classmethod
    def class_name(cls):
        return cls.__name__

    def _warn_double_wrap(self):
        """
        Utility function that checks if we're accidentally trying to double wrap an env
        Raises:
            Exception: [Double wrapping env]
        """
        env = self.env
        while True:
            if isinstance(env, BaseWrapper):
                if env.class_name() == self.class_name():
                    raise Exception("Attempted to double wrap with Wrapper: {}".format(self.__class__.__name__))
                env = env.env
            else:
                break

    def step(self, action):
        """
        By default, run the normal environment step() function
        Args:
            action (np.array): action to take in environment
        Returns:
            4-tuple:
                - (dict) observations from the environment
                - (float) reward from the environment
                - (bool) whether the current episode is completed or not
                - (dict) misc information
        """
        return self.env.step(action)

    def reset(self):
        """
        By default, run the normal environment reset() function
        Returns:
            dict: Environment observation space after reset occurs
        """
        return self.env.reset()

    def observation_spec(self):
        """
        By default, grabs the normal environment observation_spec
        Returns:
            dict: Observations from the environment
        """
        return self.env.observation_spec()

    @property
    def unwrapped(self):
        """
        Grabs unwrapped environment
        Returns:
            env (OmniGibsonEnv): The unwrapped environment
        """
        if hasattr(self.env, "unwrapped"):
            return self.env.unwrapped
        else:
            return self.env

    # this method is a fallback option on any methods the original env might support
    def __getattr__(self, attr):
        # using getattr ensures that both __getattribute__ and __getattr__ (fallback) get called
        # (see https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute)
        orig_attr = getattr(self.env, attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                result = orig_attr(*args, **kwargs)
                # prevent wrapped_class from becoming unwrapped
                if result == self.env:
                    return self
                return result
            return hooked
        else:
            return orig_attr
