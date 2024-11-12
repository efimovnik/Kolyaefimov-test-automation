Feature: Main page form submission

  Scenario: Successful form submission
    Given I open the main page
    When I fill the form with name "Test", email "test@test.com", message "Test message", and request type "Личный"
    And I submit the form
    Then I should see the success message "Спасибо! Ваш запрос уже получен.Я свяжусь с вами по указанному email в течение 3 дней или ранее, если я смогу что-то предложить в ответ."
