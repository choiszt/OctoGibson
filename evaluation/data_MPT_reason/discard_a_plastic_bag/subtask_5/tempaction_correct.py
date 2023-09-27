

def act(robot, env, camera):
    (straw_277, straw_278) = registry(env, 'straw-277', 'stow-278')
    MoveBot(env, robot, camera, camera)
    donothing(env)
