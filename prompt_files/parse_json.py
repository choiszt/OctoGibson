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

def all_SG_parse_json(path):
    SG = []
    OBJ = []
    OBJ_INFO = []
    OBS = []
    with open(path) as f:
        data = json.load(f)
    for k in data.keys():
        parsed_data = data[k]
        if type(parsed_data)==str:
            TASK=parsed_data
            continue
        for ks in parsed_data.keys(): #each object in data
            if ks == 'scene_graph':
                all_relations=[]
                with open(path[:-10]+"psg_relation.json","r")as f:
                    all_psg=json.load(f)
                for key in all_psg.keys():
                    for relation in all_psg[key]:
                        if relation not in all_relations:
                            all_relations.append(relation)
                
                for s in all_relations:
                    if s not in SG:
                        SG.append(tuple(s))
            elif ks == 'inventory':
                INV = parsed_data[ks]
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
    # obs_str = ''
    # for i in OBS:
    #     s = '(' + i[0] + ', ' + str(i[1])+ ')'
    #     obs_str += s    

    EVLM_obj=path.split("/")[-3]
    with open("./prompt_files/for_jingkang/val_34task_object.json","r")as f:
        all_obj=json.load(f)
    for ele in all_obj[EVLM_obj]:
        obs_str+=f"({ele}),"
    final_SG=list(set(SG)).copy()
    for (obj1,prep,obj2) in list(set(SG)):
        if (obj2,prep,obj1) in final_SG:
            final_SG.remove((obj1,prep,obj2))


    return [final_SG, obs_str, str(INV), str(TASK)]

def parse_json(path):
    SG = []
    OBJ = []
    OBJ_INFO = []
    OBS = []
    with open(path) as f:
        data = json.load(f)
    for k in data.keys():
        parsed_data = data[k]
        if type(parsed_data)==str:
            TASK=parsed_data
            continue
        for ks in parsed_data.keys(): #each object in data
            if ks == 'scene_graph':
                sg = parsed_data[ks]
                for s in sg:
                    if s not in SG:
                        SG.append(tuple(s))
            elif ks == 'inventory':
                INV = parsed_data[ks]
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
    # obs_str = ''
    # for i in OBS:
    #     s = '(' + i[0] + ', ' + str(i[1])+ ')'
    #     obs_str += s    

    final_SG=list(set(SG)).copy()
    for (obj1,prep,obj2) in list(set(SG)):
        if (obj2,prep,obj1) in final_SG:
            final_SG.remove((obj1,prep,obj2))


    return [final_SG, obs_str, str(INV), str(TASK)]

if __name__=="__main__":
    parse_json("/shared/liushuai/OmniGibson/data/subtask_1/task.json")

