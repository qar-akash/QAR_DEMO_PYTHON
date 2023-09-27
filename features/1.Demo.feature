@register
Feature: This feature is used to test the demo functionalities.

  @scenario_1 @regression
  Scenario: Test and verify that user is able to redirect to register page
    Given Open the application with mentioned URL
    When Click on the SignUp button and redirect to the register page

  @scenario_2 @regression
  Scenario: Test and verify that user is able to redirect to subscription page
    Given Open the application with mentioned URL
    When Click on the SignUp button and redirect to the register page
    And Enter Email address and click on submit button
    Then verify that user is able to navigate to subscription page