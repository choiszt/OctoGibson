

def act(robot, env, camera):
    beet = registry(env, 'beet_277')
    wicker_basket = registry(env, 'wicker_basket_276')
    unfold(robot, beet, wicker_basket)
    donothing(env)
