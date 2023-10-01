Feature: User Registration
  Scenario: Register a new user
    Given User is in the Home Page
    When User click sign in button
    And User input email in registration field
    And User click submit button
    And User input personal information in registration field
    And User submit personal information 'with' newsletter
    Then User can see toast success in My Account page
