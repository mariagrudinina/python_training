Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <email>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | lastname  | email              |
  | firstname1 | lastname1 | email1@example.com |
  | firstname2 | lastname2 | email2@example.com |


Scenario: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname> and <email>
  When I edit the contact from the list
  Then the new contact list is equal to the old list with updated contact

  Examples:
  | firstname     | lastname    | email               |
  | firstname 1.1 | lastname1.1 | email11@example.com |
  | firstname 2.1 | lastname2.1 | email21@example.com |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

