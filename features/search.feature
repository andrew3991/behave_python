# Created by QA3 at 03.10.2018
Feature: Auth to app account
  # Enter feature description here
  @slow
  Scenario: Phone auth
    Given I open start activity
    When I enter number 9114585525
    Then Button is active