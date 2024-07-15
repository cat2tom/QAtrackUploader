import requests

import datetime

import json

import os.path

from upload_QAtrack import read_mri_daily_qa_file,read_mri_monthly_qa_files


    
    
def read_qa_results(**kwargs):
    
    '''
    Read QA resutls from file. For MRI QA, it reades from txt file outputted by Auto MRI QA program. 
    
    input: 
    
    kwargs['mri_daily_qa_file']: daily qa file 
    kwargs['mri_monthly_se_file']: monthly se file
    kwargs['mri_monthly_ge_file']: monthly ge file
    kwargs['mri_monthly_ute_file']: monthly ute file
    kwargs['mri_monthly_dixon_file']: monthly dixon file
    
    output: 
    
    qa_data[dict]: nexted dict containing QA resutls.
    
    '''
    
    qa_data_dict={}
    
       
    if 'mri_daily_qa_file' in kwargs.keys():
        
        qa_data_dict=read_mri_daily_qa_file(kwargs['mri_daily_qa_file'])
        
    if 'mri_monthly_se_file' in kwargs.keys() and 'mri_monthly_ge_file' in kwargs.keys() and \
       'mri_monthly_ute_file' in kwargs.keys() and 'mri_monthly_dixon_file' in kwargs.keys():
        
        se_qa_file=kwargs['mri_monthly_se_file']
        ge_qa_file=kwargs['mri_monthly_ge_file']
        ute_qa_file=kwargs['mri_monthly_ute_file']
        dixon_qa_file=kwargs['mri_monthly_dixon_file']
        
               
        
        qa_data_dict=read_mri_monthly_qa_files(se_qa_file,ge_qa_file,ute_qa_file,dixon_qa_file)
        
    return qa_data_dict
       
      


         
     

if __name__=='__main__':

    '''
    
    A quick unit test. 
    
    '''
   

   #  #      
    
    mri_daily_qa_file="tmp.txt"  
    
    se_qa_file='monthlyTmpSE.txt'
       
    ge_qa_file='monthlyTmpGE.txt'
    
    ute_qa_file='monthlyTmpUTE.txt'
    
    dixon_qa_file='monthlyTmpDIXON.txt'
 
    # # 
    
    qa_data_dict=read_mri_daily_qa_file(mri_daily_qa_file)
    
    #print(qa_data_dict)
    
    # # 
    
    mri_daily_qa_data=read_mri_daily_qa_file(mri_daily_qa_file)
    
    #print(mri_daily_qa_data)
    
    # # 
    
    latest_qa_data=get_latest_mri_qa_data(se_qa_file)
    
    #print(latest_qa_data)
    
    # # 
    
    one_mothly_qa_data=read_one_mri_monthly_qa_file(se_qa_file)
    
    #print(one_mothly_qa_data)
    
    # # 
    monthly_qa_data_dict=read_mri_monthly_qa_files(se_qa_file,ge_qa_file,ute_qa_file,dixon_qa_file)
    
    #print(monthly_qa_data_dict)
    
    
    # # 
    
       
    daily_qa_data_dict=read_qa_results(mri_daily_qa_file=mri_daily_qa_file)
    
    
    
    print(daily_qa_data_dict)
    
     
    
    
    monthly_qa_data_dict=read_qa_results(mri_monthly_se_file=se_qa_file,
                                         mri_monthly_ge_file=ge_qa_file,
                                         mri_monthly_ute_file=ute_qa_file,
                                         mri_monthly_dixon_file=dixon_qa_file)
    
    print(monthly_qa_data_dict)
    
    
    
    
    
    
    
    
       
   
