

def act(robot, env, camera):
    paper_bag_277 = registry(env, 'paper_box_277')
    MoveBot(env, robot, (paper_bag_277 - 277), camera)
    donothing(env)
