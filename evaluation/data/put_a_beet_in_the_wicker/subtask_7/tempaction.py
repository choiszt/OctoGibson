def act(robot,env,camera):
    # Subtask 2: Put the beet in the wicker basket
    beet = registry(env,"beet_277")
    unfold(robot, beet)
    donothing(env)

