#parse information from 1 BEV picture and 4 ego pictures
import json

def _decomposed(self): #decomposed all the object in the env at the very beginning
    OG_results=[]
    parsed_objects=self.env.task.activity_conditions.parsed_objects
    OG_dict=self.env.task.load_task_metadata()["inst_to_name"] #format in OG E.g: floor.n.01_1 -> floors_hcqtge_0
    for key in parsed_objects.keys():
        for ele in parsed_objects[key]: #E.g:bacon.n.01_1
            OG_results.append(OG_dict[ele])

    return OG_results



def parse_json(path):
    SG = []
    OBJ = []
    OBJ_INFO = []
    OBS = []
    with open(path) as f:
        data = json.load(f)
    for k in data.keys():
        parsed_data = data[k]
        for ks in parsed_data.keys(): #each object in data
            if ks == 'scene_graph':
                sg = parsed_data[ks]
                for s in sg:
                    if s not in SG:
                        SG.append(tuple(s))
            elif ks == 'inventory':
                INV = parsed_data[ks]
            elif ks == 'task':
                TASK = parsed_data[ks]
            else:
                if ks not in OBJ:
                    obj = []
                    obj.append(ks)
                    obj_data = parsed_data[ks]
                    obj.append(tuple(obj_data['ability']))
                    obj.append(tuple(obj_data['position_in_bot'])) # correct the key
                    OBJ_INFO.append(obj)
                    OBJ.append(ks)
                    obs = (ks, tuple(obj_data['ability']),obj_data['position_in_bot']['rho'])
                    OBS.append(obs)
                else:
                    continue    
    sg_str = ''
    for i in SG:
        s = ','.join(i)
        sg_str += '(' + s + ')'
    obs_str = ''
    for i in OBS:
        s = '(' + i[0] + ', ' + str(i[1])+ ", " +str(round(i[2], 2)) + ')'
        obs_str += s

    return [sg_str, obs_str, str(INV), str(TASK)]

parse_json('/shared/liushuai/OmniGibson/816_test_gpt/task1.json')