Feature: First saga test
  Only for testing

  Scenario: Basic scenario
    Given some precondition
    When some action is performed
    Then some expected result should occur

  Scenario Outline: Example scenario with examples
    Given a user with <user_type>
    When they perform <action>
    Then they should see <result>

    Examples:
      | user_type | action    | result           |
      | admin     | login     | dashboard access |
      | user      | register  | welcome message  |
    Given John likes reading books 
    Given John likes cooking for his family
    Given John likes traveling twice a year

