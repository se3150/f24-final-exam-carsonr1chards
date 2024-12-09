Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I add "Testing the encode functionality" to the inputfield "#letters"
    And I add "3" to the inputfield "#shift-amount"
    And I click on the element "#submit"
    And I pause for 200ms
    Then I expect that element "#decoded_message p" contains the text "Whvwlqj wkh hqfrgh ixqfwlrqdolwb"


Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I add "Decode" to the inputfield "#decoder-setting"
    And I add "3" to the inputfield "#shift-amount"
    And I add "Whvwlqj wkh hqfrgh ixqfwlrqdolwb" to the inputfield "#letters"
    And I click on the element "#submit"
    And I pause for 200ms
    Then I expect that element "#decoded_message p" contains the text "Testing the encode functionality"