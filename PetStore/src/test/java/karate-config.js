function fn() {
  var env = karate.env; // get system property 'karate.env'
  karate.log('karate.env system property was:', env);
  var config = {
    env: env,
    baseUrl: 'https://petstore3.swagger.io/api/v3'
  }
  return config;
}