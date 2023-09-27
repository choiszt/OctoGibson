def act(robot,env,camera):
    # Subtask 2: Take out the chocolates from the fridge
    chocolates = registry(env,"chocolates_177")
    EasyGrasp(robot, chocolates)
    donothing(env)

