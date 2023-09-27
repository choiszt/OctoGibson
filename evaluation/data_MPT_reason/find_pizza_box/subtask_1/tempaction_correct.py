

def act(robot, env, camera):
    cheese_tart_box_86 = registry(env, 'cheese-tart-box-86')
    MoveBot(env, robot, cheese_tart_box_86, camera)
    donothing(env)
