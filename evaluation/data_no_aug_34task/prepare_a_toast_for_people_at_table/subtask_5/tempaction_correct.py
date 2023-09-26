

def act(robot, env, camera):
    toast = registry(env, 'toaster_85')
    MoveBot(env, toast, camera)
    donothing(env)
