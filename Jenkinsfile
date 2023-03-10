#!/usr/bin/groovy

//We are using declarative pipeline syntax and not the scripted pipeline as described here: https://stackoverflow.com/questions/42050626/jenkins-pipeline-agent-vs-node
properties([
        //https://stackoverflow.com/questions/35370810/how-do-i-use-jenkins-pipeline-properties-step
        parameters([
                //note here that the default will be the element you have as a first choice in the array
                choice(name: 'environment_name', choices: ['test', 'dev', 'staging', 'production'],
                        description: 'Choose the environment you want to execute the automated scenarios'),

                string(name: 'branch_name', defaultValue: 'main',
                        description: 'branch name which is going to be used to git clone the project'),

                string(name: 'tag_filtering', defaultValue: '(not disabled) and smoke',
                        description: 'define which scenarios to run based on their tags (custom markers). Leave empty for all. This will be the value for the -m parameter of pytest'),

                string(name: 'name_filtering', defaultValue: '',
                        description: 'will this string expression will be contained as part of filename/classname/methodname/functionname? If yes the test will be included. Leave empty for all. This will be the value for the -k parameter of pytest'),

                string(name: 'scope_filtering', defaultValue: 'test/',
                        description: 'do NOT leave empty. Choose folder or file. You may also specify tests within a class like so: test_mod.py::TestClass::test_method or inside a method like so: test_mod.py::test_func'),
        ]),

        pipelineTriggers([
                //explained here: https://stackoverflow.com/questions/44113834/trigger-hourly-build-from-scripted-jenkinsfile
                //recall that ANY change you do here you will need to execute the job once manually for the new cron parameter to be updated immediately, otherwise you need to wait for the job that was originally scheduled
                //minutes, hours, day of month, month, day of week  //H is any first available (here minute) of the hour according to resources

                //cron('H 23 * * 0-4') //this works only with the DEFAULT parameters //https://en.wikipedia.org/wiki/Cron#CRON_expression

                //leave spaces where you want them around the parameters. They'll be trimmed
                //sample line: */2 * * * * %environmentName=STAGE;SomeOtherVariable=Pluto
                //you may repeat multiple line configuration if you want
                //RP-1060, RP-1103

//Uncomment 4 lines below to start scheduling
//                parameterizedCron('''
//          H 8 * * 1-5 %environmentName=PROD
//          H 8 * * 1-5 %environmentName=STAGE
//        ''')
                //here this means every day at some minute the jenkins will decide according to resources after 8:00am any day of the month, any month but only MON-FRI
        ]),
])

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps{
                echo 'Checkout project'
                checkout([$class                           : 'GitSCM',
                          branches                         : [[name: "${branch_name}"]],
                          doGenerateSubmoduleConfigurations: false,
        //                  extensions                       : scm.extensions + [[$class: 'LocalBranch'], [$class: 'WipeWorkspace']],
                          extensions                       : scm.extensions + [[$class: 'LocalBranch']], //removing the WipeWorkspace to allow for Allure to generate its Trend Graph by keeping history
                          submoduleCfg                     : [],
        //                   userRemoteConfigs                : [[credentialsId: 'jenkins', url: 'git@github.com:pligor/qa_scenarios.git']]
                          userRemoteConfigs                : [[url: 'git@github.com:pligor/qa_scenarios.git']]
                ])
            }
        }

        stage('Build') {
            steps {
                echo "============================================"
                echo "Building project with current build url being: ${BUILD_URL}"
                echo "with parameters:"
                echo "environment_name: ${environment_name}"
                echo "branch_name: ${branch_name}"
                echo "tag_filtering: ${tag_filtering}"
                echo "name_filtering: ${name_filtering}"
                echo "scope_filtering: ${scope_filtering}"
                echo "============================================"

                sh '''#!/bin/bash
                    source ~/.bashrc && pyenv activate myenv && python -m pip install -r requirements.txt && source deactivate'''
                echo "all requirements should have been pip installed"

                // we can append ` || true` to the script to prevent it from failing: https://stackoverflow.com/a/25745593/720484
                sh 'rm -f allure_result/* || true'
                echo "emptied directory of previous Allure Results without destroying the history folder"
            }
        }

        stage('Run scenarios') {
            steps {
                echo "============================================"
                echo 'Automation scenarios execution is starting'
                echo "============================================"

                //-s -o log_cli=true -o log_cli_level='INFO'  <-- we have omitted this part of pytest as in general,
                //we will not be staring the console of the jenkins quite often, rather the report
                sh """#!/bin/bash
                source ~/.bashrc && pyenv activate myenv && \
                ENVIRONMENT_NAME=${environment_name} \
                pytest \
                --html=report_pytest_html/report.html --self-contained-html \
                --json-report --json-report-file=report_pytest_json/report.json --json-report-indent=2 \
                --alluredir=allure_pytest_export \
                -m '${tag_filtering}' -k '${name_filtering}' '${scope_filtering}' && \
                source deactivate"""
                // extra parameters if you wish to send a slack message at the end of the executions
                // --slack_hook="https://hooks.slack.com/services/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" \
                // --slack_channel='some-slack-channel' --slack_report_link='${BUILD_URL}'
            }
        }
    }
    post {
        always {
            //this block is executed after the pipeline finishes regardless of whether it succeeded or failed
            echo "============================================"
            echo 'Publishing pytest-html report'
            echo "============================================"

            publishHTML(target: [
                    keepAll    : true,
                    reportDir  : 'report_pytest_html',
                    reportFiles: 'report.html',
                    reportName : 'Static HTML Report'
            ])

            // here we are certain that at least the simple html report is generated

            echo "============================================"
            echo 'Publishing Allure report'
            echo "============================================"

            sh 'allure generate allure_pytest_export/ --clean -o allure_html_generate/'

            publishHTML(target: [
                    keepAll    : true,
                    reportDir  : 'allure_html_generate',
                    reportFiles: 'index.html',
                    reportName : 'Allure Report'
            ])

            echo "========================================================="
            echo 'Publishing Allure report combined in a single html file'
            echo "========================================================="

            sh '''#!/bin/bash
            source ~/.bashrc && pyenv activate myenv && \
            allure-combine allure_html_generate/ && \
            source deactivate'''
            sh 'mkdir -p report_allure/'
            sh 'mv allure_html_generate/complete.html report_allure/report_allure.html'

            publishHTML(target: [
                    keepAll    : true,
                    reportDir  : 'report_allure',
                    reportFiles: 'report_allure.html',
                    reportName : 'Allure Packed Single Html'
            ])

            echo "============================================"
            echo 'Preserving the Allure history of executions'
            echo "============================================"

            //https://stackoverflow.com/a/50499775/720484
            sh 'cp -rf allure_html_generate/history allure_pytest_export/'
            // therefore we will NOT be erasing the allure_pytest_export
        }
    }
}
