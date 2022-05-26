import requests
from Utils.constants import *

class testRial():

    def updateCase(self, case, state, comentario):
        url = 'https://vecindarioqa.testrail.io/index.php?/api/v2/add_result/' + case
        myobj= { "status_id": state, 'comment': comentario}
        requests.post(url, json=myobj, auth=(user_testRails,pass_testRails))

    def getCase(self,  case):
        url = 'http://vecindarioqa.testrail.io/index.php?/api/v2/get_test/' + case
        return requests.get(url, auth=(user_testRails,pass_testRails)).text

    def getResultsCase(self, case):
        url = 'http://vecindarioqa.testrail.io/index.php?/api/v2/get_results/' + case
        return requests.get(url, auth=(user_testRails, pass_testRails)).text


