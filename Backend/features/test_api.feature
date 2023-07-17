Feature: Test API
  Scenario: make POST request to API
    Given the API URL is "https://clarity.dexcom.com/api/subject/1594950620847472640/analysis_session"
    When have valid AuthToken
    And POST request is sended
    Then response code is 200
    And analysisSessionId is not null