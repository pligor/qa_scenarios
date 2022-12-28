#!/usr/bin/groovy
@Library('xm-pipeline-library') _

//We are using scripted pipeline and not declarative pipeline syntax as described here: https://stackoverflow.com/questions/42050626/jenkins-pipeline-agent-vs-node
properties([
        //https://stackoverflow.com/questions/35370810/how-do-i-use-jenkins-pipeline-properties-step
        parameters([
                //note here that the default will be the element you have as a first choice in the array
                choice(name: 'environment_name', choices: ['test', 'dev', 'staging', 'production'],
                        description: 'Choose the environment you want to execute the automated scenarios'),
                string(name: 'branch_name', defaultValue: 'master',
                        description: 'branch name which is going to be used to git clone the project'),
                string(name: 'tag_filtering', defaultValue: '(not disabled) and (smoke or watchlist)',
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

node('automation_dev') {
    //Now we have changed this from the `winqa` to make it execute in the node of the local Jenkins in my linux laptop
    stage('Checkout') {
        echo 'Checkout project from GitLab...'
        checkout([$class                           : 'GitSCM',
                  branches                         : [[name: "${branch_name}"]],
                  doGenerateSubmoduleConfigurations: false,
//                  extensions                       : scm.extensions + [[$class: 'LocalBranch'], [$class: 'WipeWorkspace']],
                  extensions                       : scm.extensions + [[$class: 'LocalBranch']], //removing the WipeWorkspace to allow for Allure to generate its Trend Graph by keeping history
                  submoduleCfg                     : [],
                  userRemoteConfigs                : [[credentialsId: 'jenkins', url: 'git@gitlab.xm.com:gpligoropoulos/api_gateway_python.git']]
        ])
    }

    stage('Build') {
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
            source /home/jenkins/venvs/api_gateway_venv/bin/activate && pip install -r requirements.txt && pip install -r test-requirements.txt'''
        echo "all requirements should have been pip installed"

        try {
            sh 'rm -f allure_result/*'
        } catch(err) { // alternatively we could append ` || true` to the script to prevent it from failing: https://stackoverflow.com/a/25745593/720484
        }
        echo "empty directory of previous Allure Results without destroying the history folder"
    }

    stage('Run scenarios') {
        echo "============================================"
        echo 'Automation scenarios are executed'
        echo "============================================"

        try {
            sh """#!/bin/bash
          source /home/jenkins/venvs/api_gateway_venv/bin/activate && \
          ENVIRONMENT_NAME=${environment_name} \
          pytest --html=report_pytest_html/report.html --self-contained-html --alluredir=allure_result -s \
          -m '${tag_filtering}' -k '${name_filtering}' -o log_cli=true -o log_cli_level=INFO '${scope_filtering}' \
          --slack_hook="https://hooks.slack.com/services/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" \
          --slack_channel='proj-usagateway-ci' --slack_report_link='${BUILD_URL}' """
        } catch(err) {
            echo "pytest error: ${err}"
            currentBuild.result = 'FAILURE'
        }
    }

    stage('Publish reports') {
        echo "============================================"
        echo 'Publishing pytest-html report'
        echo "============================================"

        publishHTML(target: [
                keepAll    : true,
                reportDir  : 'report_pytest_html',
                reportFiles: 'report.html',
                reportName : 'Static HTML Report'
        ])

        echo "============================================"
        echo 'Publishing Allure report'
        echo "============================================"

        sh '/home/jenkins/allure-2.13.8/bin/allure generate allure_result/ --clean -o report_allure/'

        publishHTML(target: [
                keepAll    : true,
                reportDir  : 'report_allure',
                reportFiles: 'index.html',
                reportName : 'Allure Report'
        ])

        //https://stackoverflow.com/a/50499775/720484
        sh 'cp -rf report_allure/history allure_result/'
    }
}
