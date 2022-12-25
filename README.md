# SYSTEM PREPARATION
- Using preferably a Mac or Linux as an Operating System.  
- Have Python 3.x installed in your system (e.g. in MacOS `brew install python` or google "How to install python in ... "). Alternatively use https://www.tutorialsteacher.com/python/install-python
- Install latest version of `pip` following the instructions: https://pip.pypa.io/en/stable/installation/
- Install pyenv to your system following these instructions: https://github.com/pyenv/pyenv#getting-pyenv
- `pyenv install 3.9.10` to install a compatible version of python
- Create a virtualenv based on this version: `pyenv virtualenv 3.9.10 myvirtualenv`

# HOW TO INSTALL
- Install allure: `brew install allure`
- git clone https://github.com/
- Make sure that you have installed all libraries using `pip install -r requirements.txt` BUT for Selene use
`pip install git+https://github.com/yashaka/selene.git`

# BEFORE YOU EXECUTE
- Make sure that the services are up and running
- You are executing from a machine that has access to the services (consider proper configuration of firewalls, vpns, proxies etc)
- Enable in command line the virtual environment by executing `pyenv activate myvirtualenv`

## Before you execute - Chrome specific
- Make sure that the Chrome version being used for Selenium executions is the one most popular among our customers

# HOW TO EXECUTE
Execute pytest command:  

    rm -rf allure_result && ENVIRONMENT_NAME=test pytest -n 4 -s -o log_cli=true -o log_cli_level="INFO"  -m 'not (hello_world or disabled)' -k '' --alluredir=allure_result test/ && allure serve allure_result

use `--collect-only` if you want to have a collection to see if the test can be collected which does not actually execute it. This tests if pytest can find the test(s) you want

To include also Static Html Report (`pip install pytest-html`) use parameters:   
`--html=report_pytest_html/report.html --self-contained-html`

To include also Allure Report:  
`--alluredir=allure_result`

To specify the testrail based on case id:  
`-m 'testrail' -C "C37168,C37169"`

To use Report Portal:  
`--reportportal`

To run tests in parallel to multiple CPUs exploit `pip install pytest-xdist`:
`-n 4` for tests in parallel

# HOW TO EXECUTE MANUAL SCENARIOS

    ENVIRONMENT_NAME=test pytest -s -o log_cli=true -o log_cli_level="DEBUG"  -m '' -k '' --html=report_pytest_html/report.html --self-contained-html test/test_manual/

To generate pytest Json report:
`--json-report --json-report-file=report_pytest_json/2022-08-27_report.json --json-report-indent=2`


# HOW TO VIEW ALLURE REPORT Locally
Execute command: `allure serve allure_result`

# What's next?
In the project you will find various TODO files which should be included in tracking system
e.g. Jira or Instabug and be planned to be solved

# JIRA tags
qatrivial, qaminor, qamajor, qacritical: 4 levels of priority of which one should be picked up for manual testing first  
qano: No QA involvement at all for this ticket  
qahold: this has been put on hold and a comment for the reason should be found in the ticket itself or in its epic
smokefail: the ticket has failed during smoke checking
smokepass: the ticket has passed a basic superficial check
defectspending: all the scenarios have been executed for this ticket and some linked defects are pending
reopened: the ticket has some defects and have been returned to the dev team for solving those issues

## Authors
George Pligoropoulos
