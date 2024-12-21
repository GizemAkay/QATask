@ignore
Feature: Utils

  Background:
    * def randomGenerator = Java.type('helpers.RandomGenerator')


  @ignore @getNumber
  Scenario: getNumber
    * def num = randomGenerator.getNumber()


  @ignore @getGender
  Scenario: getGender
    * def gender = randomGenerator.getGender()

  @ignore @getName
  Scenario: getName
    * def name = randomGenerator.getName()

