Feature: Main page form submission

  Scenario Outline: Successful form submission
    Given I open the main page
    When I fill the form with name "<name>", email "<email>", message "<message>", and request type "<request_type>"
    And I submit the form
    Then I should see the success message "Спасибо! Ваш запрос уже получен.Я свяжусь с вами по указанному email в течение 3 дней или ранее, если я смогу что-то предложить в ответ."

  Examples:
    | name      | email                    | message                  | request_type          |
    | Personal  | personal@test.com        | Personal test message    | Личный                |
    | Commercial| commercial@test.com      | commercial test message  | Коммерческий          |


  Scenario Outline: Unsuccessful form submission
    Given I open the main page
    When I fill the form with name "<name>", email "<email>", message "<message>", and request type "<request_type>"
    And I submit the form
    Then I should see a "<status_code>" response for the form submission

  Examples:
    | name      | email                    | message                  | request_type          | status_code |
    |           |                          |                          |                        |400 |
    | empty email & message|               |                          |                        |400 |
    |           | empty_message@test.com   |                          |                        |400 |
    |           |                          | empty email              |                        |400 |