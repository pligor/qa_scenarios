#!/usr/bin/env python
# coding: utf-8

# In[2]:


from os import system


# In[5]:


from sys import argv


# In[6]:


assert len(argv) == 2, "only one parameter is allowed and should be test/test_manual/some_dir/another_dir/some_file.py"


# In[4]:


system('rm -rf allure_pytest_export/ && rm -rf allure_html_generate/')


# In[9]:


arg = argv[1] #test/test_manual/some_dir/another_dir/some_file.py

# In[10]:


from pathlib import PurePath


# In[21]:


parts = PurePath(arg).parts


# In[22]:


assert parts[0] == 'test' and parts[1] == 'test_manual', 'the dir where this is executed should be test/test_manual'


# In[13]:


relative_path = PurePath()
for part in parts[2:]: # drop test and test_manual
    relative_path /= part


# In[15]:


dir_path = relative_path.parent


# In[17]:


dir_file_path = dir_path / relative_path.stem


# In[19]:


pytest_cmd = f"pytest -s -o log_cli=true -o log_cli_level='INFO'  -m '' -k '' --html=report_pytest_html/{dir_file_path}_report.html --self-contained-html --json-report --json-report-file=report_pytest_json/{dir_file_path}_report.json --json-report-indent=2 --alluredir=allure_pytest_export test/test_manual/{dir_file_path}.py"


# In[20]:


system(pytest_cmd)


# In[ ]:


system('allure generate allure_pytest_export/ --clean -o allure_html_generate/ && allure-combine allure_html_generate/')


# In[ ]:


system(f'mkdir -p report_allure/{dir_path}')


# In[ ]:


system(f'mv allure_html_generate/complete.html report_allure/{dir_file_path}_allure.html')


# In[ ]:


system('rm -rf allure_pytest_export/ && rm -rf allure_html_generate/')

