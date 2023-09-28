

def act(robot, env, camera):
    cupofyougri = registry(env, "'cupofysoggri_86','cupofytoppe_85'")
    EasyGrasp(robot, cupofyougri)
    donothing(env)
