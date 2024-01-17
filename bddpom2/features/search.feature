Feature: Search
  # And in fisierele de steps definition file e tot given sau when sau then
  @interes
  Scenario: Check that search works when I search for an existing product
    Given I am on the home page
    When I enter "Iphone" in the search input
    And I press Search button
    Then The URL of the page is "https://demo.nopcommerce.com/login"