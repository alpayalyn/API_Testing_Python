# Created by alpay at 14.01.2022
Feature: # GitHub API Validation
  # Enter feature description here

  Scenario: # Session Management Check
    Given I have github auth credentials
    When I hit getRepo API of Github
    Then status code of response should be <statuscode>
    |statuscode |
    |200    |