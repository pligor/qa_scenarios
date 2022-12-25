@web @captcha @security @NVDEVEL-2509 @NVDEVEL-2522
Feature: Security Improvements - Add captcha in our public dashboard forms
  Resident permit
  Pay a Payable (Deprecate pay a fine)
  GV person in need

  @prio_critical @smoke @CWWo9sUFf9HQieoEMxNR2ks
  Scenario: Verify that for all the public forms there is a recaptcha as the last form field above the submit button


  @prio_critical @smoke @C9dGfr8Y2tCiLVaAqNsP7dR
  Scenario: Verify that filling all the fields with valid values, but letting recaptcha intact will yield a proper error message to the user to deal with the recaptcha and no entry will have been generated in the dashboard, namely the submit will not have occurred


  @prio_critical @C2cXZF5RsCWdF5sSzogWpyo
  Scenario: Verify that filling all the fields with valid values, starting the recaptcha but not completing it, will not allow the user to submit the form


  @prio_critical @CSNSWt6Ajmt7WBce24w8cka
  Scenario: Verify that filling all the fields with valid values, using the recaptcha to make it valid, waiting a little bit but not long to expire, will allow the user to submit the form and an entry will have been generated in the dashboard


  @prio_critical @CkhPeuuT2BwHNUEKTSn5LAt
  Scenario: Verify that using a proper recaptcha submitting the form and on the success screen hitting the back button of the browser, the new recaptcha will be initiated to be a new random one, instead of being the same as the previous


  @prio_major @CBymPM77dUp9LwxNm2WqAkB
  Scenario: Verify that filling all the fields with valid values, using the recaptcha to make it valid but then waiting long enough to let it expire, will yield an error message to the user that the recaptcha is not valid anymore and the user will not be able to submit the form


  @prio_major @CF8K9ZdS5tBnmwDNqceDFzP
  Scenario: Verify that filling the recaptcha with valid values, and letting it expire, afterwards the next recaptcha will NOT be the same as the former one, and repeating this multiple times still has the same effect


  @prio_major @Cdx5qi9hgPTtsPFmAAkL6F6
  Scenario: Verify that reloading the web page even if the form values are stored and retained, the recaptcha will be initiated to be a new random one every time and will not allow the user to submit the form unless the recaptcha is valid again


  @prio_major @CgVYNoEuZPu9TsyEVwtTQFc
  Scenario: Verify that having the same form opened in multiple tabs and in multiple browsers, all of these tab-windows, each one will have each unique random recaptcha and these will not be similar in any way


  @prio_minor @CNKT6EAaXKqgq5Xb2RZFmqm
  Scenario: Verify that if the user has filled a proper recaptcha in the form, and all but one of the fields of the form are valid, when attempting to submit the form, an error message for the invalid field will be shown to the user and the form will not be submitted, but the recaptcha as long as it does not have expired yet, it will remain valid and by correcting the mistake the user is allowed to submit the form


