
import os 
import sys



sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from upload_QAtrack import upload_unittest_results_to_QAtrack

from mri_qa_file import read_qa_results

from qatrack_configfile import read_qatrack_configfile,read_root_configfile


# qatrack configure location 

root_configfile='root_qatrack_config.ini'

qatrack_configfile=read_root_configfile(root_configfile)


# # get settings from config file. 

#qatrack_config_file='qatrack_config.ini'

qatrack_config_dict=read_qatrack_configfile(qatrack_configfile)

root_api_url=qatrack_config_dict['root_api_url']

monthly_url=qatrack_config_dict['monthly_url']

daily_url=qatrack_config_dict['daily_url']

unit_test_collection_instance_url=daily_url



qatrack_user_token= qatrack_config_dict['qatrack_user_token']



mri_daily_qa_file= qatrack_config_dict['mri_daily_qa_file'] 

   
se_qa_file=qatrack_config_dict['mri_monthly_se_qa_file']
   
ge_qa_file= qatrack_config_dict['mri_monthly_ge_qa_file']

ute_qa_file=qatrack_config_dict['mri_monthly_ute_qa_file']

dixon_qa_file= qatrack_config_dict['mri_monthly_dixon_qa_file']


# # send to QAtrack.

# Send daily QA. 

unit_test_collection_instance_url=daily_url


daily_qa_data_dict=read_qa_results(mri_daily_qa_file=mri_daily_qa_file)

qa_results_json=daily_qa_data_dict

#resp_daily=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json,upload_fequency='currenttime')

resp_daily=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json)

print(resp_daily)

# monthly QA

unit_test_collection_instance_url=monthly_url


monthly_qa_data_dict=read_qa_results(mri_monthly_se_file=se_qa_file,
                                        mri_monthly_ge_file=ge_qa_file,
                                        mri_monthly_ute_file=ute_qa_file,
                                        mri_monthly_dixon_file=dixon_qa_file)

qa_results_json=monthly_qa_data_dict

#resp_monthly=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json,upload_fequency='currenttime')

resp_monthly=upload_unittest_results_to_QAtrack(root_api_url, unit_test_collection_instance_url,qatrack_user_token, qa_results_json)



print(resp_monthly)



