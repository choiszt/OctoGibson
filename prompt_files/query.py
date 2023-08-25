import re
import time
import os

# from javascript import require
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import sys;sys.path.append("/shared/liushuai/OmniGibson")
import prompt_files.env_utils_gpt as u
import openai

class Query:
    def __init__(
        self,
        model_name="gpt-4",
        temperature=0,
        request_timout=120,
        openai_api_key=None,
    ):
        # os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["OPENAI_API_KEY"] = "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"

        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            request_timeout=request_timout,
        ) # API KEY

        self.history_info = {}
        self.record_history()

    def render_system_message(self):
        system_template = u.load_prompt("prompt_template")

        response_format = u.load_prompt("response_template")
        system_message_prompt = SystemMessagePromptTemplate.from_template(
            system_template
        )
        system_message = system_message_prompt.format(response_format=response_format)  ### programs and response_format are variables in system template.
        assert isinstance(system_message, SystemMessage)
        return system_message
    
    def render_human_message(
        self, inventory="", object="", scene_graph="", task="" 
    ):

        message = ""    

        if object:
            message += f"Observed Objects: {object}\n"
        else:
            message += f"Observed Objects: None\n"
        if scene_graph:
            message += f"Observed Relations: {scene_graph}\n"
        else:
            message += f"Observed Relations: None\n"

        if inventory:
            message += f"Inventory: {inventory}\n"
        else:
            message += f"Inventory: None\n"

        message += f"Task Goal: {task}\n"
        
        if len(self.history_info['subtask']) > 0:
            message += f"Original Subtasks: {self.history_info['subtask']}\n"
        else:
            message += f"Original Subtasks: None\n"

        if len(self.history_info['code']) > 0:
            message += f"Previous Action Code: {self.history_info['code']}\n"
            if len(self.history_info['error']) > 0:
                message += f"Execution Error: {self.history_info['error']}\n"
            else:
                message += f"Execution Error: No error\n"  
        elif len(self.history_info['code']) == 0: 
            message += f"Previous Action Code: No code\n"
            message += f"Execution error: No error\n"  
        
        message += "Now, please output Explain, Subtasks (revise if necessary), Code that completing the next subtask, and Target States, according to the instruction above. Remember you can only use the functions provided above and pay attention to the response format."
            
        return HumanMessage(content=message)
    
    def process_ai_message(self, message):
        assert isinstance(message, AIMessage)

        processed_message = message.content
        # with open('./answer.txt', 'w') as f:
        #     f.write(processed_message)
        retry = 3
        error = None
        classes = ["Explain:", "Subtasks:", "Code:", "Target States:"]
        idxs = []
        for c in classes:
            m = processed_message.find(c)
            idxs.append(m)
        if -1 in idxs:
            raise Exception('Invalid response format!')
        while retry > 0:
            # try:
            explain = processed_message[:idxs[1]]
            subtask = processed_message[idxs[1]:idxs[2]]
            code = processed_message[idxs[2]:idxs[3]]
            target = processed_message[idxs[3]:]
            explain = explain.split('Explain: \n')[1].split('\n\n')[0]
            subtask = subtask.split('Subtasks:\n')[1].split('\n\n')[0]
            exec_code = code.split('```python\n')[1].split('```')[0]
            inv = target.split('Inventory: ')[1]
            inv = inv.split('Object')[0].split('\n')[0]
            obj_states_2 = []
            obj_states_3 = []
            objects = target.split('Information:\n')[1]
            objects = objects.split('\n')
            for obj in objects:
                obj = obj.split(') ')[-1]
                obj_list = obj.split(', ')
                if len(obj_list) == 3:
                    obj_states_2.append(obj_list)
                elif len(obj_list) == 4: 
                    obj_states_3.append(obj_list)
            return {
                "explain": explain,
                "subtask": subtask,
                "code": exec_code,
                "inventory": inv,
                "obj_2": obj_states_2, 
                "obj_3": obj_states_3,
            }
            # except Exception as e:
            #     retry -= 1
            #     error = e
            #     time.sleep(1)
        return f"Error parsing response (before program execution): {error}"
    
    def record_history(self, subtask="", code="", error=""):
        self.history_info['subtask'] = subtask
        self.history_info['code'] = code
        self.history_info['error'] = error

if __name__ == '__main__':
    with open('response.txt', 'r') as f:
        response = f.read()
        q = Query()
        system = q.render_system_message()
        human = q.render_human_message(object="(fridge_xyejdx_0, [('openable', 0), ('heatable', 0), ('freezable', 0)], 2.12)(stove_rgpphy_0, [('togglable', 0), ('heatable', 0), ('freezable', 0)], 1.59)(griddle_157, [('togglable', 0), ('heatable', 0), ('freezable', 0)], 1.68)(bacon_1234, ('cookable, heatable, burnable'), 2.12)",
                                       scene_graph="(pot_plant_udqjui_0,ontop,bottom_cabinet_jrhgeu_1)(trash_can_zotrbg_0,nextto,fridge_xyejdx_0)(bacon_1234, inside fridge_xyejdx_0)(fridge_xyejdx_0,nextto,shelf_owvfik_0)(pot_plant_udqjui_2,ontop,floors_xzlkei_0)(stove_rgpphy_0,under,range_hood_iqbpie_0)(stove_rgpphy_0,nextto,shelf_owvfik_0)(stove_rgpphy_0,nextto,door_lvgliq_1)(griddle_157,under,range_hood_iqbpie_0)(griddle_157,nextto,stove_rgpphy_0)",
                                       task='cook the bacon')
        print('111')
        answer = q.llm([system, human])
        
        print(answer.content)
        # with open('./response.txt', 'w') as f:
        #     f.write(answer.content)
        info = q.process_ai_message(answer)
        
        print(info['explain'])
        print(info['code'])
        print(info['subtask'])
        print(info['inventory'])
        print(info['obj_2'])
        print(info['obj_3'])