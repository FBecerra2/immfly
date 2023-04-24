Feature: Comprobar "Position"
  Como usuario quiero comprobar que diga "Position" por default en el 
  checkbox 

  Scenario: "Postion" exitoso
    Given Ingreso a la pagina
    When hago click en el check
    Then debe decir "Postion"
