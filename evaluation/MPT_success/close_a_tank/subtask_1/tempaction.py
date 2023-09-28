def act(robot,env,camera):
    # Subtask 1: Move the agent to thebowl(tak)
    bowl_195 = registry(env,"bowl-195")
    MoveBot(env, robot, bowl_195, camera)

