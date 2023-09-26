def act(robot,env,camera):
    # Subtask 1: Grasp The Bucket
    bucket_275 = registry(env,"bucket_285")
    EasyGrasp(roboy, bucket_275)
    donothing(env)

