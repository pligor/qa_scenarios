@web @mobile @security @NVDEVEL-2167 @NVDEVEL-2508
Feature: Improve email verification flow for all apps - Use verifications to protect our basic resources
  Parking: Do not allow a mobile phone verification without a verified email.

  Reports: We do not allow a report submission without a verified mobile phone number.

  Do not allow more than 10 verify requests per month per user per medium (mobile or email).

  Q0: Before implementing such security measures do we know what to measure to see if we are hurting the product ? It is important to NOT lose legitimate customers just because they did mistakes, or are very not tech-savvy, but lose only those who are malicious, but how to ensure that ?
  Q1: The "how many times is a user allowed to verify a mobile phone number" accounts both the attempts or only the actual verifications ? Namely if I merely visit the form to set a mobile phone number but for some reason I needed to abandon the process and retry later when I can, then the user should be allowed to do this, no ? Only if he actually attempts to put an OTP 4-digit code, then this should be counted as an attempt, no ?

  @prio_critical @smoke @CKA9FBRuijCvmjfyUmubDqj
  Scenario: Verify that using a user who has not verified his/her email address but is attempting to verify his/her mobile phone number, this will yield a corresponding error message that will explain to the user of what actions he/she needs to take in order to proceed with the verification of the mobile phone number

  @prio_critical @smoke @C2QeNg6kHXv36iBh6xTHTjG
  Scenario: Verify that a user who has verified his/her email address when attempting to verify his/her mobile phone number, this will be successful given that the phone number is valid and the 4 digit code that the user received as OTP was used properly
    Swift Parking

  @prio_critical @CHf2Vv2zrDAHf3JmJySKYqv
  Scenario: Verify that a user who has logged in using any Social Network, who has not yet verified his phone number, he is allowed to verify his a phone number
    Facebook

  @prio_critical @CYFqx4iXMiapj4DK9Pnrbqx
  Scenario: Verify that a user who has not verified his phone number when attempting either from the Report button of the Home screen or from the plus-icon button of MyCity screen, he will receive an error message explaining to him that first his phone number needs to be verified before submitting any report


  @prio_critical @CJSLGRfcEZqpNsbLFDfbxDu
  Scenario: Verify that a user who has already verified his phone number, even if he updated his email and currently is pending for verification, he will still be allowed to send as many Reports as he wishes to
    Q3: Is this scenario true ?

  @prio_critical @Cn47xbPm6z76TkmZ7U68ABa
  Scenario: Verify that for a single user, who has already executed 10 requests for verification of any email addresses, executing an 11th request for verification of an email address, within a month should NOT be allowed, and the user should receive an error message explaining to him when the next attempt to verify an email address can happen


  @prio_critical @CkoVxwZwUzejeXYxYtzrGTv
  Scenario: Verify that for a single user, executing 10 requests for verification of some phone number, within a month should be allowed


  @prio_critical @CGec4kQ9PdGFxgE9YiBgZEP
  Scenario: Verify that for a single user, who has executed 9 requests for verification of some email addresses, plus 9 requests for verification of some phone numbers, then attempting to execute a 10th request for the verification of an email address should be allowed


  @prio_critical @CMVPNTHYnTfoiMx5euThM5m
  Scenario: Verify that for a single user, who has executed 10 requests for verification of some email addresses, plus 9 requests for verification of some phone numbers, should NOT be allowed to execute a verification of an email address but should be allowed to execute a verification of some phone number


  @prio_critical @CNurYxNDJ7twurrjJSe4xLw
  Scenario: Verify that for a single user, who has executed 10 requests for verification of some email addresses, plus 10 requests for verification of some phone numbers, should NOT be allowed to execute a verification of an email address NOR he should be allowed to execute a verification of any phone number, for within the month


  @prio_critical @CWcJDX2uSmDuiDP4RHh7Ghb
  Scenario: Verify that for a single user, who has executed 10 requests for verification of some email addresses, plus 10 requests for verification of some phone numbers, if the period of the One Month has passed, then the user will be allowed to execute a verification both for some email address and for some phone number
    Q4: When we are expressing the period of a Month for the restrictions in the description of this ticket, are we referring to 30 days in the past or is this calendar based ?

  @prio_major @CZmsEEvXvoTDUbr4JwkKnX8
  Scenario: Verify that a user who had verify his/her email address, but has changed his/her email address, and thus this is deemed as no longer valid, if he has not yet verified his phone number, he will NOT be allowed to verify it until the new/updated email is also verified
    MyAthensPass

  @prio_major @CCnC6uTsiEroqMpr76ajuLH
  Scenario: Verify that a user who had verify his/her email address, but has changed his/her email address, and thus this is deemed as no longer valid, if he had already verified his phone number, then he will NOT be forced to verify his phone number once more
    Q2: Is this scenario true ?

  @prio_major @CK2scSDgMNDx2n226dQsbFL
  Scenario: Verify that a user who has logged in using any Social Network, who has already verified his phone number, he is allowed to verify a second phone number given, which will replace the first one
    Apple id

  @prio_major @CeRVPh9ov5rLZEDGYF7oRdy
  Scenario: Verify that a user who has logged in using any Social Network, who has already verified his phone number, then this user is allowed to create/file as many Reports as he wishes to
    Google

  @prio_major @CKfw7DeDhgUVhDVX6mDyajW
  Scenario: Verify that for a single user, executing 10 requests for verification of some email addresses, within a month should be allowed


  @prio_major @C9vrbqcssJxZAUcX5gnAos5
  Scenario: Verify that for a single user, who has already executed 10 requests for verification of any phone numbers, executing an 11th request for verification of a phone number, within a month should NOT be allowed, and the user should receive an error message explaining to him when the next attempt to verify his phone number can happen


  @prio_minor @Cma2yZ865MmhSEoQspNhNAS
  Scenario: Verify that a user who has logged in using any Social Network, who has not yet verified his phone number, then this user is NOT allowed to create/file any Report
    Facebook

  @prio_minor @regression @Cdn5sTWjQf4C6rYFVqjzGdM
  Scenario: Verify that a user who has already verified his phone number, if he attempts to reverify the exact same phone numbers, an informative message should explain to the user that he cannot re-verify the same phone number or he will not be able to proceed with the verification of the phone number at all (the submit button will be disabled)


