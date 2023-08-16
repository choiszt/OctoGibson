#parse information from 1 BEV picture and 4 ego pictures
import json

def parse_json(path):
    SG = []
    OBJ = []
    OBJ_INFO = []
    OBS = []
    with open(path) as f:
        data = json.load(f)
    for k in data.keys():
        parsed_data = data[k]
        for ks in parsed_data.keys():
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
                    obs = (ks, obj_data['position_in_bot']['rho'])
                    OBS.append(obs)
                else:
                    continue    
    sg_str = ''
    for i in SG:
        s = ','.join(i)
        sg_str += '(' + s + ')'
    obj_str = ''
    for i in OBJ_INFO:
        s = '[' + i[0] + ', ' + '(' + ','.join(i[1]) + ')'  + ', ' + '(' + ','.join(i[2]) + ')' + ']'
        obj_str += s
    obs_str = ''
    for i in OBS:
        s = '(' + i[0] + ', ' + str(round(i[1], 2)) + ')'
        obs_str += s

    return [sg_str, obj_str, obs_str, str(INV), str(TASK)]
