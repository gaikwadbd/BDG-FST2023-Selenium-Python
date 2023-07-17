Feature: Test Login

  Scenario: Test Successfully login
    Given main page is open
    When click on "Dexcom CLARITY for Home Users" button
    And enter correct username
    And enter correct password
    And click on login button
    Then login successfully