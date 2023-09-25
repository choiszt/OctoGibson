

def act(robot, env, camera):
    checkoutfloor_scksdal_00 = registry(env, 'checkoutfloor_socksdal_00')
    MoveBot(env, checkoutfloor_scksdal_00, camera)
    donothing(env)
