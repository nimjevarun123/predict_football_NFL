import pickle
import json
import numpy as np

from flask import Flask , render_template
import config


class win_loss():
    def __init__(self,input):
        self.input=input 

    def import_files(self):

        with open(config.model_path,"rb") as m_file:
            self.bmodel = pickle.load(m_file)
    

        with open(config.json_path,'r') as in_file: 
            self.input_featues = json.load(in_file)

    def prediction(self):
        self.import_files()        

        user_input = np.zeros(len(self.input_featues['input_features']))    
        # print(user_input)

        array= np.array(self.input_featues['input_features'])


        team_string = "Team_" + "html_Team"
        Team_index = np.where(array == team_string)[0]
        user_input[Team_index] = 1

        user_input[0]  = self.input["html_wlp"]
        user_input[1]  = self.input["html_pd"]
        user_input[2]  = self.input["html_y"]
        user_input[3]  = self.input["html_fgm"]
        user_input[4]  = self.input["html_fp"]
        user_input[5]  = self.input["html_rzp"]
        user_input[6]  = self.input["html_pwp"]
        user_input[7]  = self.input["html_sp"]
        user_input[8]  = self.input["html_tp"]
        user_input[9]  = self.input["html_rp"]
        user_input[10] = self.input["html_pyp"]
        user_input[11] = self.input["html_ptg"]
        user_input[12] = self.input["html_ppg"]
        user_input[13] = self.input["html_ypg"]
        user_input[14] = self.input["html_pag"]
        user_input[15] = self.input["html_p20"]

        
        print ()
        print (user_input)
        print ()

        Match_Result = self.bmodel.predict([user_input])
        # print (Match_Result)

        if Match_Result==0:
            result = "\U0001F499LOSS"
            print(result)
        else:
            result = "\U0001F499WIN"
            print (result)

        return render_template("nfl.html",match_output= result)
            




