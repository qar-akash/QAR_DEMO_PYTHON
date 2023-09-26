@login
Feature: This feature is used to test the Login functionalities.


  @login_positive @regression
  Scenario: Test and verify that user is able to login into the application
    Given Open the application with mentioned URL
    When Login Into application with correct username and password
    Then Verify that user has been loggedIn successfully

  @logout_positive @regression
  Scenario: Test and verify that user is able to logout from the application
    Given Open the application with mentioned URL
    When Login Into application with correct username and password
    Then Verify that user has been loggedOut successfully


