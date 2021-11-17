Feature: Testing herokuapp

  @scenario.1
  Scenario: Test A/B Testing
    Given User is on the webpage
    When User click A/B Testing
    Then The user is redirected to the "AbTesting"
    And Page title is A/B Test Control

  @scenario.2
  Scenario: Test Add/Remove Elements
    Given User is on the webpage
    When User clicks Add/Remove Elements
    Then the user is redirected to the "AddRemoveTesting"
    And Page title is Add/Remove Elements
    And User clicks Add Element button
    And User verifies if Delete button appeared
    And User clicks Delete Element button
    And User verifies if Delete button disappeared

  @scenario.3
  Scenario: Test Form Authentication
    Given User is on the webpage
    When User clicks Form Authentication
    Then the user is redirected to the "FormAuthentication"
    And Page title is Login Page
    And User logs in
    And Successful log in message pop up
    And User logs out
    And Successful log out message pop up

  @scenario.4
  Scenario: Test Form Authentication With Invalid Credentials
    Given User is on the webpage
    When User clicks Form Authentication
    Then the user is redirected to the "FormAuthentication"
    And Page title is Login Page
    And User logs in with invalid credentials
      | Username   | Password              |
      | tomsmith   | SuperSecretPassword!! |
      | tomsmithh  | SuperSecretPassword!  |
    And Invalid credentials message pop up

  @scenario.5
  Scenario: Test Dropdown list
    Given User is on the webpage
    When User clicks Dropdown
    Then the user is redirected to the "Dropdown"
    And Page title is Dropdown
    And User clicks at Dropdown list

  @scenario.6
  Scenario: JavaScript alerts
    Given User is on the webpage
    When User clicks JavaScript Alerts
    Then the user is redirected to the "JavaScriptAlerts"
    And Page title is JavaScript Alerts
    And User clicks JS Alert
    And User accepts popup
    And User clicks JS Confirm
    And User accept JS Confirm
    And User clicks JS Confirm
    And User dismiss JS Confirm

  @scenario.7
  Scenario: Horizontal slider
    Given User is on the webpage
    When User clicks Horizontal slider
    Then the user is redirected to the "HorizontalSlider"
    And User moves Horizontal slider to the end
    And User moves Horizontal slider to the beginning