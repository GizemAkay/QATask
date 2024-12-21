Feature: PetStoreCRUD

  Background:
    * def getNumber = call read('classpath:features/Utils.feature@getNumber')
    * def getName = call read('classpath:features/Utils.feature@getName')
    * url baseUrl
    * path '/pet'
    * def name = getName.name
    * def id = getNumber.num
    * def newPetRequest = read('classpath:requests/petStore/petStore.json')


  @PetStorePostHappyPath
  Scenario Outline: PetStorePostHappyPath
    # Set columns for fields' values
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * request newPetRequest
    * print newPetRequest
    * method post
    * status 200
    * print response
    * match response.id == newPetRequest.id
    * match response.name == newPetRequest.name


    Examples:
      | id     | name   | categoryId | categoryName | dogPhoto                       | tagId  | tagName     | status
      | id     | name   | 1          | kitten       | https://media.istockphoto.com  |  10    | abc         | "available"
      | id     | name   | ""         |    ""        | ""                             |   ""   | ""          |  ""
      | id     | name   | 2          | Dogs         | https://media.istockphoto.com  |  11    | abc         | 'pending'
      | id     | name   |null        |  null        | null                           |  null  | null        |  null
      | id     | name   | 3          | Dogs         | https://media.istockphoto.com  |  12    | abc         | 'sold'



  @PetStorePostErrorPath
  Scenario Outline: PetStorePostErrorPath
    # Set columns for fields' values
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * print newPetRequest
    * request newPetRequest
    * method post
    * status <statusCode>


    Examples:
      | id                                                                | name   | categoryId                                                        | categoryName | dogPhoto                            | tagId | tagName     | status        |  statusCode|
      | "abc"                                                             | name   | 4                                                                 | Dogs         | https://media.istockphoto.com       | 12    | puppy       | 'pending'     |   400      |
      | id                                                                | name   | 12345678910111213141516171819201234567891011121314151617181920164 | Dogs         | https://media.istockphoto.com       | 12    | puppy       | 'test'        |   400      |
      | id                                                                | name   | "abc"                                                             | Dogs         | https://media.istockphoto.com       | null  | puppy       | 'pending'     |   400      |
      | 12345678910111213141516171819201234567891011121314151617181920164 | name   | 5                                                                 | Dogs         | https://media.istockphoto.com       | null  | 123         | 'available'   |   400      |


  Scenario Outline: PetStorePostErrorPath
    # Set columns for fields' values
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * if (newPetRequest.id == null) karate.remove('newPetRequest', 'id')
    * print newPetRequest
    * request newPetRequest
    * method post
    * status <statusCode>

    Examples:
      | id        | name   | categoryId   | categoryName | dogPhoto                            | tagId | tagName     | status        |  statusCode|
      | null      | name   | 6           | Dogs         | https://media.istockphoto.com       | 12    | puppy       | 'available'   |   500      |



  @PetStorePostSendingOnlyRequired
  Scenario Outline: PetStorePostSendingOnlyRequired
    # Still Happy Path
    # Set columns for fields' values
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * if (newPetRequest.id == null) karate.remove('newPetRequest', 'id')
    * if (newPetRequest.name == null) karate.remove('newPetRequest', 'name')
    * if (newPetRequest.categoryId == null && newPetRequest.categoryName == null) karate.remove('newPetRequest', 'category')
    * if (newPetRequest.dogPhoto == null) karate.remove('newPetRequest', 'photoUrls')
    * if (newPetRequest.tagId == null && newPetRequest.tagName == null) karate.remove('newPetRequest', 'tags')
    * if (newPetRequest.status == null) karate.remove('newPetRequest', 'status')
    * request newPetRequest
    * print newPetRequest
    * method post
    * status 200
    * print response
    * match response.id == newPetRequest.id
    * match response.name == newPetRequest.name
    * def newResponse = response


    Examples:
      | id     | name   | categoryId | categoryName | dogPhoto  | tagId  | tagName     | status
      | id     | name   |null        |  null        | null      |  null  | null        |  null


  @PetStoreGet
  Scenario: PetStoreGet
    * def  PetStorePostSendingOnlyRequired = call read('classpath:features/PetStore/petStore.feature@PetStorePostSendingOnlyRequired')
    * path PetStorePostSendingOnlyRequired.newResponse.id
    * method get
    * status 200
    * match response.id == PetStorePostSendingOnlyRequired.newResponse.id

  Scenario: PetStoreGet
    # error path
    * path '100123'
    * method get
    * status 404
    * match response == "Pet not found"


  @PetStorePut
  Scenario Outline: PetStorePutHappyPath
    * def PetStorePostSendingOnlyRequired = call read('classpath:features/PetStore/petStore.feature@PetStorePostSendingOnlyRequired')
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * print newPetRequest.id
    * request newPetRequest
    * method put
    * status 200
    * match response.id == newPetRequest.id
    * match response.name == newPetRequest.name
    * def newResponse = response.id



    Examples:
      | id                                                 | name   | categoryId | categoryName | dogPhoto                       | tagId  | tagName     | status
      | PetStorePostSendingOnlyRequired.newResponse.id     | name   | ""         |    ""        | ""                             |   ""   | ""          |  ""
      | PetStorePostSendingOnlyRequired.newResponse.id     | name   | 7          | kitten       | https://media.istockphoto.com  |  10    | abc         | "available"



  @PetStorePutSendingOnlyRequired
  Scenario Outline: PetStorePutSendingOnlyRequired
    * def  PetStorePostSendingOnlyRequired = call read('classpath:features/PetStore/petStore.feature@PetStorePostSendingOnlyRequired')
    # Still Happy Path
    # Set columns for fields' values
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * if (newPetRequest.id == null) karate.remove('newPetRequest', 'id')
    * if (newPetRequest.name == null) karate.remove('newPetRequest', 'name')
    * if (newPetRequest.categoryId == null && newPetRequest.categoryName == null) karate.remove('newPetRequest', 'category')
    * if (newPetRequest.dogPhoto == null) karate.remove('newPetRequest', 'photoUrls')
    * if (newPetRequest.tagId == null && newPetRequest.tagName == null) karate.remove('newPetRequest', 'tags')
    * if (newPetRequest.status == null) karate.remove('newPetRequest', 'status')
    * request newPetRequest
    * print newPetRequest
    * method put
    * status 200
    * print response
    * match response.id == PetStorePostSendingOnlyRequired.newResponse.id


    Examples:
      | id                                                 | name   | categoryId | categoryName | dogPhoto  | tagId  | tagName     | status
      | PetStorePostSendingOnlyRequired.newResponse.id     | name   |null        |  null        | null      |  null  | null        |  null



  @PetStorePutErrorPath
  Scenario Outline: PetStorePutErrorPath
    * def  PetStorePostHappyPath = callonce read('classpath:features/PetStore/petStore.feature@PetStorePostSendingOnlyRequired')
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * print newPetRequest
    * request newPetRequest
    * method post
    * status <statusCode>


    Examples:
      | id                                                                | name   | categoryId                                                        | categoryName | dogPhoto                            | tagId | tagName     | status        |  statusCode|
      | "abc"                                                             | name   | 8                                                                 | Dogs         | https://media.istockphoto.com       | 12    | puppy       | 'pending'     |   400      |
      | id                                                                | name   | 12345678910111213141516171819201234567891011121314151617181920164 | Dogs         | https://media.istockphoto.com       | 12    | puppy       | 'test'        |   400      |
      | id                                                                | name   | "abc"                                                             | Dogs         | https://media.istockphoto.com       | null  | puppy       | 'pending'     |   400      |
      | 12345678910111213141516171819201234567891011121314151617181920164 | name   | 9                                                                 | Dogs         | https://media.istockphoto.com       | null  | 123         | 'available'   |   400      |



  Scenario Outline: PetStorePutErrorPath
    * def  PetStorePostHappyPath = callonce read('classpath:features/PetStore/petStore.feature@PetStorePostSendingOnlyRequired')
    * set newPetRequest.id = <id>
    * set newPetRequest.name = <name>
    * set newPetRequest.category = { id: <categoryId>, name: <categoryName> }
    * set newPetRequest.photoUrls = [<dogPhoto>]
    * set newPetRequest.tags = [{ id: <tagId>, name: <tagName> }]
    * set newPetRequest.status = <status>
    * if (newPetRequest.id == null) karate.remove('newPetRequest', 'id')
    * print newPetRequest
    * request newPetRequest
    * method post
    * status <statusCode>


    Examples:
      | id    | name   | categoryId   |   categoryName   | dogPhoto                           | tagId | tagName     | status        |statusCode|
      | null  | name   | 10           | 'Dogs'           | https://media.istockphoto.com      | 12    | puppy       | 'available'   | 500   |


  @PetStoreDelete
  Scenario: PetStoreDelete
    * def  PetStorePostSendingOnlyRequired = call read('classpath:features/PetStore/petStore.feature@PetStorePostSendingOnlyRequired')
    * path PetStorePostSendingOnlyRequired.newResponse.id
    * method delete
    * status 200
    * match response == "Pet deleted"