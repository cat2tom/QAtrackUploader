import requests

import datetime

import json

import os.path


def get_latest_mri_qa_data(mri_qa_file):
    
    
    """
    Read the mri qa txt file and get the latest resutls as a list. 
    
    Input: 
    
    mri_qa_file[str]: qa result file name. 
    
    output:
    
    latest_qa_data[list]: lastest mri qa data. 
    
    
    """
    
    latest_qa_data=[]
    
    with open(mri_qa_file) as file:
          
          
        # read lines into list 
        lines = [line.split(',') for line in file.readlines()]
        
        # get the last line and assume it is latest QA data.         
        
        last_line=lines[-1]
        
        last_line=[line.strip() for line in last_line]
        
        latest_qa_data=last_line
        
    return(latest_qa_data)
    

def read_mri_daily_qa_file(mri_daily_qa_file):
    
    '''
    
    Read mri daily QA file into a nested dict. 
    
    Input: 
    
    mri_daily_qa_file: mri_daily_qa_file
    
    Output: 
    
    mri_daiy_qa_dict: dict containing daily qa results. 
    
    '''
    qa_results_dict={}

    qa_data_dict={} 
    
    latest_qa_data=get_latest_mri_qa_data(mri_daily_qa_file)
    
    last_line=latest_qa_data


    
    qatime=last_line[0]
    snr=float(last_line[1])
    uniformity=float(last_line[2])
    contrast=float(last_line[3])  
    ghosting=float(last_line[4])
    d45=float(last_line[5])
    d135=float(last_line[6])
    signal=float(last_line[7])
    
    laser_x=float(last_line[8])
    laser_y=float(last_line[9])
    laser_z=float(last_line[10])
    
    
    qa_data_dict={
        'mri_snr': {'value': snr}, 
        'mri_uniformity': {'value': uniformity}, 
        'mri_contrast':{'value':contrast},
        'mri_ghosting':{'value':ghosting},
        'mri_distance45':{'value':d45},
        'mri_distance135':{'value':d135},
        'mri_signal':{'value':signal},
        'mri_laser_x':{'value':laser_x},
        'mri_laser_y':{'value':laser_y},
        'mri_laser_z':{'value':laser_z},
        'staff_name':{'value':'Therapist/Radiographer'}
        }

    qa_results_dict['tests']=qa_data_dict
    qa_results_dict['qatime']=qatime

        
    return(qa_results_dict)

def read_one_mri_monthly_qa_file(mri_monthly_qa_file):
    
    """
    Read one monthly QA file. 
    
    Input: 
    
    mri_monthly_qa_file: one monthly QA file.
    
    output: 
    
    qa_data_dict[dict]: dict containing qa results. 
    
    """
    
   
    qa_data_dict={}
    
    latest_qa_data_se=get_latest_mri_qa_data(mri_monthly_qa_file)
    
    last_line=latest_qa_data_se


    
     
    qatime=last_line[0]   
    snr=float(last_line[1])
    uniformity=float(last_line[2])
    ghosting=float(last_line[3])
    diameter=float(last_line[4])
    signal=float(last_line[5])   
    
    qa_data_dict['snr']=snr
    
    qa_data_dict['uniformity']=uniformity
    
    qa_data_dict['ghosting']=ghosting
    
    qa_data_dict['diameter']=diameter
    
    qa_data_dict['signal']=signal

    qa_data_dict['qatime']=qatime


    return (qa_data_dict)
    
   
       
         
def read_mri_monthly_qa_files(se_qa_file,ge_qa_file,ute_qa_file,dixon_qa_file):
    
    """
    
    Read mothQA files into a dict. 
    
    Input: 
    
    se_qa_file: qa file name for se 
    ge_qa_file: qa file name for ge
    ute_qa_file: qa file name for ute
    dixon_qa_file:qa file name for dixon
    
    output: 
    
    qa_data_dict[dict]: qa_data_dict['tests'] contains qa test resutls{'qa_result_name':value}
                        qa_data_dict['qatime']:containing qa time. 
    
    """
    
    # se
    
    qa_results_dict={}

    qa_data_dict_se=read_one_mri_monthly_qa_file(se_qa_file)

    qatime=qa_data_dict_se['qatime']
    
   
    mri_snr_se=qa_data_dict_se['snr']
    mri_uniformity_se=qa_data_dict_se['uniformity']
    mri_ghosting_se=qa_data_dict_se['ghosting']
    mri_diameter_se=qa_data_dict_se['diameter']
    mri_signal_se=qa_data_dict_se['signal']
    
    # ge
    
    qa_data_dict_ge=read_one_mri_monthly_qa_file(ge_qa_file)
      
    
    mri_snr_ge=qa_data_dict_ge['snr']
    mri_uniformity_ge=qa_data_dict_ge['uniformity']
    mri_ghosting_ge=qa_data_dict_ge['ghosting']
    mri_diameter_ge=qa_data_dict_ge['diameter']
    mri_signal_ge=qa_data_dict_ge['signal']   
    
   # ute 
   
    qa_data_dict_ute=read_one_mri_monthly_qa_file(ute_qa_file)
         
       
    mri_snr_ute=qa_data_dict_ute['snr']
    mri_uniformity_ute=qa_data_dict_ute['uniformity']
    mri_ghosting_ute=qa_data_dict_ute['ghosting']
    mri_diameter_ute=qa_data_dict_ute['diameter']
    mri_signal_ute=qa_data_dict_ute['signal']     
    
    # dixon
    
    qa_data_dict_dixon=read_one_mri_monthly_qa_file(dixon_qa_file)
           
         
    mri_snr_dixon=qa_data_dict_dixon['snr']
    mri_uniformity_dixon=qa_data_dict_dixon['uniformity']
    mri_ghosting_dixon=qa_data_dict_dixon['ghosting']
    mri_diameter_dixon=qa_data_dict_dixon['diameter']
    mri_signal_dixon=qa_data_dict_dixon['signal']   
    
   
    
    # combined monthly data required by QAtrack. 
    
    qa_results_dict_monthly={
        'mri_snr_se': {'value': mri_snr_se}, 
        'mri_uniformity_se': {'value':  mri_uniformity_se},
        'mri_ghosting_se': {'value': mri_ghosting_se},
        'mri_diameter_se': {'value': mri_diameter_se},
        'mri_signal_se': {'value': mri_signal_se},
        
        'mri_snr_ge': {'value':mri_snr_ge}, 
        'mri_uniformity_ge': {'value':mri_uniformity_ge },
        'mri_ghosting_ge': {'value': mri_ghosting_ge},
        'mri_diameter_ge': {'value': mri_diameter_ge},
        'mri_signal_ge': {'value': mri_signal_ge},
        
        'mri_snr_ute': {'value': mri_snr_ute }, 
        'mri_uniformity_ute': {'value':  mri_uniformity_ute},
        'mri_ghosting_ute': {'value': mri_ghosting_ute},
        'mri_diameter_ute': {'value':mri_diameter_ute},
        'mri_signal_ute': {'value': mri_signal_ute},
        
        'mri_snr_dixon': {'value': mri_snr_dixon}, 
        'mri_uniformity_dixon': {'value': mri_uniformity_dixon},
        'mri_ghosting_dixon': {'value': mri_ghosting_dixon},
        'mri_diameter_dixon': {'value': mri_diameter_dixon},
        'mri_signal_dixon': {'value': mri_signal_dixon},
        'staff_name':{'value':'Physicist'}
        }

    
    qa_results_dict['tests']=qa_results_dict_monthly
    qa_results_dict['qatime']=qatime

           
    return (qa_results_dict)
    
    
  
    

def get_user_key():

    '''
    QAtrack uses user_key as field to ensure the uniqueness of each test resutls uploaded to QAtrack database. 
    Return a unique user key using current time for each qa resutls uploading via API.
    
    ouput:
    user_key[str]: unqiue user_key string.

    '''
    

    user_key_dict={}
    now = datetime.datetime.now()
    date_string=now.strftime("%Y%m%d.%H%M%S")
    #date_int = int(date_string)

    daily_string=now.strftime("%Y_%m_%d")
    monthly_string=now.strftime("%Y_%m")
    yearly_string=now.strftime("%Y")
    
    currenttime=date_string


    user_key_dict['currenttime']=currenttime
    user_key_dict['daily']=str(daily_string)
    user_key_dict['monthly']=str(monthly_string)
    user_key_dict['yearly']=str(yearly_string)

    return(user_key_dict)

def get_work_time(work_duration_minutes=30):
    '''
    Create the QA work start and end time which are form fields for each test and required when you upload the QA results through API.

    Input: 
    work_duration_minutes: times required for performing QA tests. 

    output:
    
    work_started[str]: work started time
    work_completed[str]: work finished time.

    '''
    now = datetime.datetime.now()

    time_change = datetime.timedelta(minutes=work_duration_minutes)
    new_time = now+ time_change

    work_started = now.strftime("%Y-%m-%d %H:%M:%S")
    work_completed=new_time.strftime("%Y-%m-%d %H:%M:%S")

    return (work_started,work_completed)



def upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json,upload_fequency='qatime'):

    '''
    Upload the qa resutls data to Qatrack via QA test API url. 

    Input: 

    root_api_url[str]: the root api url for QAtrack like: https://qatrack_server_ipaddress:port/api.

    unit_test_collection_instance_url[str]: instance api url corresponding the QA test in QAtrack. 

    qatrack_user_token[str]: token associated with a QAtrack user + password

    qa_results_json[dict]:  qa_data_dict[dict]: qa_data_dict['tests'] contains contaiing the QA resutls data 
                            like {'test_name1': {'value':test_result_value},{'test_name2':'test_resutls_string'}}
                            qa_data_dict['qatime']:containing qa time.  
    upload_frequency[enum]: five values of string: 'qatime', 'daily', 'monthly', 'yearly' and 'currenttime'. This parameters ensures that the results uploaded are unique and 
    not repeated uploading.

    Output: 

    response[str]: response code indicating the status of the post operation.
   
    '''
    
    # prepared the QA  test results 

    
    (work_started,work_completed)=get_work_time()

    data = {
    'unit_test_collection': unit_test_collection_instance_url,
    'day': 0, # optional day=0, for TestLists, required for Test List Cycles (where 0 <= day < # of test lists in cycle)
    'in_progress': False,  # optional, default is False
    'include_for_scheduling': True,
    'work_started': work_started,
    'work_completed': work_completed,  # optional
    'comment': "Performed and uploaded by MRI Auto QA tool.",  # optional
    'attachments': []  # optional
           }
           
    data['tests']=qa_results_json['tests']

    # change upload frequency and ensure uniqueness of results. 

    user_key_dict=get_user_key()

    if upload_fequency=='qatime':

       
        data['user_key']=qa_results_json['qatime']

   
    if upload_fequency=='daily':

       
        data['user_key']=user_key_dict['daily']

           
    if upload_fequency=='monthly':

        data['user_key']=user_key_dict['monthly']

    if upload_fequency=='yearly':

        data['user_key']=user_key_dict['yearly']

    if upload_fequency=='currenttime':

        data['user_key']=user_key_dict['currenttime']

    
    
    # uploaded to QAtrack for this QA test. 

    headers = {"Authorization": "Token %s" % qatrack_user_token}

    # important to add verify=False for the security link such as https://. 

    resp = requests.post(root_api_url + "/qa/testlistinstances/", json=data, headers=headers, verify=False) 

    return resp

def upload_jsonfile2QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_json_file):
    
    """
    Read a json file cotain qa resutls for a and upload it to QA track for a certain test. 
    
     Input: 

    root_api_url[str]: the root api url for QAtrack like: https://qatrack_server_ipaddress:port/api.

    unit_test_collection_instance_url[str]: instance api url corresponding the QA test in QAtrack. 

    qatrack_user_token[str]: token associated with a QAtrack user + password

    qa_json_file[str]: a json file containing qa results. 

    Output: 

    response[str]: response code indicating the status of the post operation.
       
    
    """
    
    if os.path.isfile(qa_json_file):
        
        file_obj=open(qa_json_file)
        
        data_dict=json.load(file_obj)
           
        #qa_results_json=json.dumps(data_dict)
     
        qa_results_json=data_dict
        
               
        resp=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json)
        
                              
        return resp
        
        
        
    else:
        
        print('json file could be found.')
        
        return 
        
     
     

if __name__=='__main__':

    '''
    
    A quick unit test. 
    
    '''
   

    # prepare the input data.

    root_api_url="http://10.33.72.210:8080/api"

    monthly_url='http://10.33.72.210:8080/api/qc/unittestcollections/192/'

    daily_url='http://10.33.72.210:8080/api/qc/unittestcollections/179/'

    #unit_test_collection_instance_url=monthly_url

    unit_test_collection_instance_url=daily_url

    qatrack_user_token="aef1edcbfcf713069a2a1b6f1650b77d2d85bd4f"

    qa_results_json={
        'mri_snr': {'value': 1}, # comment is optional
        'mri_uniformity': {'value': 1},  # value is mandatory, skipped is optional
        'mri_contrast':{'value':1},
        'mri_ghosting':{'value':1},
        'mri_distance45':{'value':1},
        'mri_distance135':{'value':1},
        'mri_signal':{'value':1},
        'mri_laser_x':{'value':1},
        'mri_laser_y':{'value':1},
        'mri_laser_z':{'value':1},
        'staff_name':{'value':'Therapist/Radiographer'}
        }

    qa_results_json_monthly={
        'mri_snr_se': {'value': 1}, 
        'mri_uniformity_se': {'value': 1},
        'mri_ghosting_se': {'value': 1},
        'mri_diameter_se': {'value': 1},
        'mri_signal_se': {'value': 1},
        'mri_snr_ge': {'value': 1}, 
        'mri_uniformity_ge': {'value': 1},
        'mri_ghosting_ge': {'value': 1},
        'mri_diameter_ge': {'value': 1},
        'mri_signal_ge': {'value': 1},
        'mri_snr_ute': {'value': 1}, 
        'mri_uniformity_ute': {'value': 1},
        'mri_ghosting_ute': {'value': 1},
        'mri_diameter_ute': {'value': 1},
        'mri_signal_ute': {'value': 1},
        'mri_snr_dixon': {'value': 1}, 
        'mri_uniformity_dixon': {'value': 1},
        'mri_ghosting_dixon': {'value': 1},
        'mri_diameter_dixon': {'value': 1},
        'mri_signal_dixon': {'value': 1},
        'staff_name':{'value':'Physicist'}
        }



    # # test upload_unittest_results_to_QAtrack

    #resp=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json)

    #print(resp)
    
    #unit_test_collection_instance_url=monthly_url
    
    #resp=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json_monthly)
  
    #print(resp)    
    
    # # test upload_jsonfile2QAtrack
    
    unit_test_collection_instance_url=monthly_url
    
    qa_json_file='test22.json'
    
    #resp=upload_jsonfile2QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_json_file)
    
    #print(resp)
    
    # # test 
    
    
    
    mri_daily_qa_file="tmp.txt"  
    
    
    qa_data_dict=read_mri_daily_qa_file(mri_daily_qa_file)
    
    #print(qa_data_dict)
    
        
    se_qa_file='monthlyTmpSE.txt'
    
    ge_qa_file='monthlyTmpGE.txt'
    
    ute_qa_file='monthlyTmpUTE.txt'
    
    dixon_qa_file='monthlyTmpDIXON.txt'
    
    
    mri_daily_qa_data=read_mri_daily_qa_file(mri_daily_qa_file)
    
    #print(mri_daily_qa_data)
    
    latest_qa_data=get_latest_mri_qa_data(se_qa_file)
    
    #print(latest_qa_data)
    
    one_mothly_qa_data=read_one_mri_monthly_qa_file(se_qa_file)
    
    #print(one_mothly_qa_data)
    

    # test upload_unittest_results_to_QAtrack for monthly.
    
    monthly_qa_data_dict=read_mri_monthly_qa_files(se_qa_file,ge_qa_file,ute_qa_file,dixon_qa_file)
    
    qa_results_json=monthly_qa_data_dict

    unit_test_collection_instance_url=monthly_url

    resp=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json,upload_fequency='currenttime')

    print(resp.json())

    # test upload_unittest_results_to_QAtrack for daily

    mri_daily_qa_data=read_mri_daily_qa_file(mri_daily_qa_file)

    #print(mri_daily_qa_data)

    qa_results_json=mri_daily_qa_data

    unit_test_collection_instance_url=daily_url

    #resp=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json)

    #print(resp.json())
    
    
