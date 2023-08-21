from prompt_files.action_list import *
from prompt_files.action_utils import *
import omnigibson as og
def act(bot, env):
    camera=og.sim.viewer_camera 
    fridge_xyejdx_0=registry(env,obj="fridge_xyejdx_0")
    MoveBot(env,env.robots[0],fridge_xyejdx_0,camera)
    open(fridge_xyejdx_0)
    action=np.zeros(11)
    fridge_xyejdx_0=env.scene.object_registry("name","fridge_xyejdx_0")
    stove_rgpphy_0=env.scene.object_registry("name","stove_rgpphy_0")
    # picture_yrgaal_0=env.scene.object_registry("name","picture_yrgaal_0")
    sofa_xhxdqf_0=env.scene.object_registry("name","sofa_xhxdqf_0")
    bacon_154=env.scene.object_registry("name","bacon_154")
    breakfast_table_skczfi_0=env.scene.object_registry("name","breakfast_table_skczfi_0")
    donothing(env)
    EasyGrasp(env.robots[0],bacon_154)
    # FlyingCapture(camera,1)
    EasyDrop(env.robots[0],bacon_154,breakfast_table_skczfi_0)



    donothing(env, action)