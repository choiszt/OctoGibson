

def act(robot, env, camera):
    wicker_basket = registry(env, 'wicker_basket_276')
    MoveBot(env, robot, wicker_basket, camera)
    donothing(env)
