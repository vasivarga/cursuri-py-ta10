Feature:

  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the page is "https://demo.nopcommerce.com/login"

  Scenario: Log in with unregistered email
    Given I am on the login page
    When I enter "pyta10@gmail.com" in the email input
    And I enter "123456" in the password input
    And I click the login button
    Then I should see "No customer account found" message


