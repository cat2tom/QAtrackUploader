import configparser



def read_qatrack_configfile(qatrack_config_file):
    
    """
    
    Read config file read the setting from qatrack_config.ini and output the settings. 
    
    Input: 
    
    
    """
    
    qatrack_config_dict={}
    
    
    config=configparser.ConfigParser()
    config.read(qatrack_config_file)
    
    # urls.
    
    qatrack_config_dict['root_api_url']=config['qatrackurl']['root_api_url']
    
    qatrack_config_dict['monthly_url']=config['qatrackurl']['monthly_url']
    
    qatrack_config_dict['daily_url']=config['qatrackurl']['daily_url']
    
    # token
    qatrack_config_dict['qatrack_user_token']=config['token']['qatrack_user_token']
    
    # qa files 
    
    qatrack_config_dict['mri_daily_qa_file']=config['mriqafiles']['mri_daily_qa_file']
    
    qatrack_config_dict['mri_monthly_se_qa_file']=config['mriqafiles']['mri_monthly_se_qa_file']
    
    qatrack_config_dict['mri_monthly_ge_qa_file']=config['mriqafiles']['mri_monthly_ge_qa_file']
    
    qatrack_config_dict['mri_monthly_ute_qa_file']=config['mriqafiles']['mri_monthly_ute_qa_file']
    
    qatrack_config_dict['mri_monthly_dixon_qa_file']=config['mriqafiles']['mri_monthly_dixon_qa_file']
    
    
    return qatrack_config_dict


def read_root_configfile(root_configfile):
    
    """
    Read the root config file containing where the qatrack_configfile is. 
    
    Input: 
    
    root_configfile: a root config file for qatrack_configfile location.
    
    output: 
    
    qatrack_configfile[str]: full path to the qatrack_configfile. 
    
    """
    
    config=configparser.ConfigParser()
    config.read(root_configfile)

     
    root_configfile=config['rootconfig']['root_qatrack_configfile']
    
    return root_configfile
    
   
    
if __name__=='__main__':

    '''
    
    A quick unit test. 
    
    '''
   
    qatrack_config_file='C:\\autoMRISimQAResource\\dirsConfigFile\\qatrack_config.ini'
    
    qatrack_config_dict=read_qatrack_configfile(qatrack_config_file)    
    
    #print(qatrack_config_dict)

    root_qatrack_configfile='C:\\autoMRISimQAResource\\dirsConfigFile\\root_qatrack_config.ini'

    qatrack_configfile=read_root_configfile(root_qatrack_configfile)

    print(qatrack_configfile)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
