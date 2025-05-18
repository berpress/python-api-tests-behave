Feature: User registration

  Scenario: Successful registration with valid credentials
    Given I have a valid registration body
    When I send a register request
    Then the response status code should be 201
    Then the response should match RegisterResponse model