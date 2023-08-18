import re
import time
import os

# from javascript import require
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage

import communicate.env_utils as u

class Query:
    def __init__(
        self,
        model_name="gpt-3.5-turbo",
        temperature=0,
        request_timout=120,
        ckpt_dir="ckpt",
        openai_api_key=None,
    ):
        os.environ["OPENAI_API_KEY"] = openai_api_key
        
        self.ckpt_dir = ckpt_dir
        u.f_mkdir(f"{ckpt_dir}/action")

        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            request_timeout=request_timout,
        ) # API KEY

        self.history_info = {}
        self.record_history()

    def render_system_message(self):
        system_template = u.load_prompt("action_template")
        
        # TODO: specify the content in prompt

        response_format = u.load_prompt("action_response_format")
        system_message_prompt = SystemMessagePromptTemplate.from_template(
            system_template
        )
        system_message = system_message_prompt.format(
            programs=programs, response_format=response_format
        )  ### programs and response_format are variables in system template.
        assert isinstance(system_message, SystemMessage)
        return system_message
    
    def render_human_message(
        self, inventory="", object="", scene_graph="", task="" 
    ):

        message = ""    

        if object:
            message += f"Observed Objects: {object}\n"
        else:
            message += f"Objects Informaton: None\n"
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
            message += f"Original Subtasks: none\n"

        if len(self.history_info['answer']) > 0:
            message += f"Previous Action Code: {self.history_info['answer']['code']}\n"
            if len(self.history_info['error']) > 0:
                message += f"Execution Error: {self.history_info['error']}\n"
            else:
                message += f"Execution Error: No error\n"  
        elif len(self.history_info['answer']) == 0: 
            message += f"Code from the last round: No code\n"
            message += f"Execution error: No error\n"  
            
        return HumanMessage(content=message)
    
    def process_ai_message(self, message):
        # assert isinstance(message, AIMessage)

        processed_message = message
        retry = 3
        error = None
        classes = ["Explain:", "Plan:", "Code:", "Target States:"]
        idxs = []
        for c in classes:
            m = processed_message.find(c)
            idxs.append(m)
        if -1 in idxs:
            raise Exception('Invalid response format!')
        while retry > 0:
            # try:
            explain = processed_message[:idxs[1]]
            plan = processed_message[idxs[1]:idxs[2]]
            code = processed_message[idxs[2]:idxs[3]]
            target = processed_message[idxs[3]:]
            explain = explain.split('Explain:\n')[1]
            plan = plan.split('Plan:\n\n')[1]
            exec_code = code.split('Code:\n\n')[1]
            inv = target.split('Inventory: ')[1]
            inv = inv.split('Object')[0]
            obj_states_2 = []
            obj_states_3 = []
            objects = target.split('Information:')[1]
            objects = objects.split('\n')
            for obj in objects:
                obj = obj[3:]
                obj_list = obj.split(', ')
                if len(obj_list) == 2:
                    obj_states_2.append(obj_list)
                else: 
                    obj_states_3.append(obj_list)
            return {
                "explain": explain,
                "plan": plan,
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
    
    def record_history(self, answer="", error=""):
        self.history_info['response'] = answer
        self.history_info['error'] = error

if __name__ == '__main__':
    with open('response.txt', 'r') as f:
        response = f.read()
        q = Query()
        d = q.process_ai_message(response)
        print(d['explain'])
        print(d['plan'])
        print(d['code'])
        print(d['inventory'])
        print(d['obj_2'])
        print(d['obj_3'])