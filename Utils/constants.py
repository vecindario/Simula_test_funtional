caps = [{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '90.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'firefox',
      'browser_version': 'latest',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'ie',
      'browser_version': '11.0',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
}]

BASEURL = "https://develop.app.simula.vecindario.com/ingresar"

username_lbtest = 'qa.testing'
# accessToken:  AccessToken can be generated from automation dashboard or profile section
accessToken_lbtest = 'pTKXtmbr4JmEdVICsRIS5ZXVQxkyN6f3oy2DIs8Qx8CWcChHS9'
# gridUrl: gridUrl can be found at automation dashboard
gridUrl_lbtest = "hub.lambdatest.com/wd/hub"




######## testRails
user_testRails = 'qa.testing@vecindario.com'
pass_testRails = 'dMTJHShPgd6jPDqQNxgM'
cap_win10 = {
    "platform": "win10",
    "browserName": "chrome",
    "version": "90.0",
    # Resolution of machine
    "resolution": "1920x1080",
    "name": "LambdaTest python google search test ",
    "build": "LambdaTest python google search build",
    "network": True,
    "video": True,
    "visual": True,
    "console": True,
}