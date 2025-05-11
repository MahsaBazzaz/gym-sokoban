from .sokoban_env import SokobanEnv
from .sokoban_env_fixed_targets import FixedTargetsSokobanEnv
from .sokoban_env_pull import PushAndPullSokobanEnv
from .sokoban_env_two_player import TwoPlayerSokobanEnv
from .boxoban_env import BoxobanEnv


class SokobanEnv_Sturgeon0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (8, 8))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 2)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])

        super(SokobanEnv_Sturgeon0, self).__init__(**kwargs)
class SokobanEnv1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv1, self).__init__(**kwargs)


class SokobanEnv2(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['num_boxes'] = kwargs.get('num_boxes', 5)
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 40)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv2, self).__init__(**kwargs)


class SokobanEnv_Small0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 2)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv_Small0, self).__init__(**kwargs)


class SokobanEnv_Small1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv_Small1, self).__init__(**kwargs)


class SokobanEnv_Large0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 300)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 43)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv_Large0, self).__init__(**kwargs)


class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 300)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 4)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 43)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv_Large1, self).__init__(**kwargs)


class SokobanEnv_Large1(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 300)
        kwargs['num_boxes'] = kwargs.get('num_boxes',5)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 43)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv_Large1, self).__init__(**kwargs)


class SokobanEnv_Huge0(SokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 13))
        kwargs['max_steps'] = kwargs.get('max_steps', 300)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 5)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(SokobanEnv_Huge0, self).__init__(**kwargs)


class FixedTargets_Env_v0(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (10, 10))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(FixedTargets_Env_v0, self).__init__(**kwargs)


class FixedTargets_Env_v1(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (10, 10))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 4)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(FixedTargets_Env_v1, self).__init__(**kwargs)


class FixedTargets_Env_v2(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 2)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(FixedTargets_Env_v2, self).__init__(**kwargs)


class FixedTargets_Env_v3(FixedTargetsSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(FixedTargets_Env_v3, self).__init__(**kwargs)


class PushAndPull_Env_v0(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (10, 10))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(PushAndPull_Env_v0, self).__init__(**kwargs)


class PushAndPull_Env_v1(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (10, 10))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 4)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(PushAndPull_Env_v1, self).__init__(**kwargs)


class PushAndPull_Env_v2(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 2)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(PushAndPull_Env_v2, self).__init__(**kwargs)


class PushAndPull_Env_v3(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 150)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(PushAndPull_Env_v3, self).__init__(**kwargs)


class PushAndPull_Env_v4(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 300)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 4)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(PushAndPull_Env_v4, self).__init__(**kwargs)


class PushAndPull_Env_v5(PushAndPullSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 300)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 5)
        kwargs['num_gen_steps'] = kwargs.get('num_gen_steps', 50)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(PushAndPull_Env_v5, self).__init__(**kwargs)


class TwoPlayer_Env0(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 2)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(TwoPlayer_Env0, self).__init__(**kwargs)


class TwoPlayer_Env1(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (7, 7))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(TwoPlayer_Env1, self).__init__(**kwargs)


class TwoPlayer_Env2(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (10, 10))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(TwoPlayer_Env2, self).__init__(**kwargs)


class TwoPlayer_Env3(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (10, 10))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 4)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(TwoPlayer_Env3, self).__init__(**kwargs)


class TwoPlayer_Env4(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 3)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(TwoPlayer_Env4, self).__init__(**kwargs)



class TwoPlayer_Env5(TwoPlayerSokobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['dim_room'] = kwargs.get('dim_room', (13, 11))
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['num_boxes'] = kwargs.get('num_boxes', 4)
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(TwoPlayer_Env5, self).__init__(**kwargs)

class Boxban_Env0(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['difficulty'] = kwargs.get('difficulty', 'unfiltered')
        kwargs['split'] = kwargs.get('split', 'train')
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(Boxban_Env0, self).__init__(**kwargs)

class Boxban_Env0_val(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['difficulty'] = kwargs.get('difficulty', 'unfiltered')
        kwargs['split'] = kwargs.get('split', 'valid')
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(Boxban_Env0_val, self).__init__(**kwargs)

class Boxban_Env0_test(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['difficulty'] = kwargs.get('difficulty', 'unfiltered')
        kwargs['split'] = kwargs.get('split', 'test')
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(Boxban_Env0_test, self).__init__(**kwargs)

class Boxban_Env1(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['difficulty'] = kwargs.get('difficulty', 'medium')
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(Boxban_Env1, self).__init__(**kwargs)

class Boxban_Env1_val(BoxobanEnv):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'],
        'render_modes': ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw']
    }
    def __init__(self, **kwargs):
        kwargs['max_steps'] = kwargs.get('max_steps', 200)
        kwargs['difficulty'] = kwargs.get('difficulty', 'medium')
        kwargs['split'] = kwargs.get('split', 'valid')
        kwargs['render_mode'] = kwargs.get('render_mode', 'rgb_array')
        kwargs['render_modes'] = kwargs.get('render_mode', ['human', 'rgb_array', 'tiny_human', 'tiny_rgb_array', 'raw'])
        super(Boxban_Env1_val, self).__init__(**kwargs)
