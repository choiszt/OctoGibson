def act(robot,env,camera):
    # Subtask 1: Move The Robot To The Board Where The Leaf is Located.
    board_275 = registry(env,"board_276")
    MoveBot(env, robot, board_275, camera)
    donothing(env)

