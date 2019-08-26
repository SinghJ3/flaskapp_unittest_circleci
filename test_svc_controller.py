import unittest
from controller.svc_controller import app, wrap_html

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_message(self):
        response = self.app.get('/')
        message = wrap_html('Hello DockerCon 2019!')
        self.assertEqual(response.data, message)

if __name__ == '__main__':
    unittest.main()


# import unittest
# import json

# from controller.svc_controller import app 
# # set our application to testing mode
# app.testing = True

# class TestSVCController(unittest.TestCase):
    
#     def test_index(self):
#         with app.test_client() as client:
#             # auth_token = 'Bearer eyJraWQiOiJaV0UwT1RNMVltWmhNVEJsWXpoaVpqVXhOVEprTnpBNFpUUXpNV0l5WkdRMk1tWTJOemM0WlEiLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiVzQwWVd6WU52ejRCS1JHMkVMRm5ZQSIsInN1YiI6ImFzaGxleV9iYW5rMSIsImNvZGUiOiIzMDUiLCJjb250YWN0aWQiOiJhc2hsZXlfYmFuazEiLCJyb2xlcyI6ImFuYWx5c3QsZGF0YUFkbWluLG1vZGVsQW5hbHlzdCxwcm9qZWN0QWRtaW4iLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJnaXZlbl9uYW1lIjoiQXNobGV5IiwiY19oYXNoIjoiMWJ2d25PdzZYWE5MZEJHc1QzNUM2USIsImF1ZCI6Im1NM2VyODFVQTJNdHJFbGZjaTFQTFF4emZhSWEiLCJhY2NvdW50bmFtZSI6ImJhbmsxIiwiYXpwIjoibU0zZXI4MVVBMk10ckVsZmNpMVBMUXh6ZmFJYSIsImF1dGhfdGltZSI6MTU2MTM3OTczOSwib3JnYW5pemF0aW9uIjoiYmFuazEiLCJhY2NvdW50c2ZkY2lkIjoiYmFuazEiLCJleHAiOjE1NjEzODI5MzEsImFwcGxpY2F0aW9uZW50aXRsZW1lbnQiOiJbe1wibmFtZVwiOlwiSW1wYWlybWVudFN0dWRpb1wiLFwic3RhcnREYXRlXCI6XCIyMDE5LTA1LTIxXCIsXCJlbmREYXRlXCI6XCIyMDE5LTA4LTIxXCIsXCJncmFjZVBlcmlvZFwiOjE1fV0iLCJmYW1pbHlfbmFtZSI6IlRhbiIsImlhdCI6MTU2MTM4MjAzMSwiZW1haWwiOiJhc2hsZXkudGFuQG1vb2R5cy5jb20ifQ.FKCgA3LUvLp_d2Y56GrrLt3s2Vrf02zn9KC9pL5mAU37Qa3SZP97TEyU1GkpIghmXaYpNRJQ8tn9Go0UZCrQMEio5o5icblsPk8Qm3_TjHkcoRuASzwOCGgLYKDDPIzqV64sdae-sk5x47pNLj0AK06jd1p5Qj6yiEKqwsH-raIYlSmRn58gJ8bCHzs7R6Fl6n2mA2ebQJ2TV_3NxO_9WwmUICMPNFieT3p8RZvJhlVIbZrc9RHogTynWnGMlsWl6d8xI6RTT8umlwqp5NjaXea3dz854G1GE3ac61VsVKMIAb8luOjn2RaTVOxmbk4LslBZuVHLW_M-tJ_opZO0qw'
#             # payload = '{"analysisId":14066,"view":{"id":4439,"viewType":"pivot","categoryName":"instrumentReference,instrumentResult","name":"Past Due Status","rowDimensions":"reportingDate,productType,company","columnDimensions":"delinquencyStatus,accruingCategory","filterDimensions":[],"valueFields":[{"name":"amortizedCost","operation":"sum"}],"allDimensions":"internalRating,primaryIndustryNAICS,moodysIndustrySector,primaryGcorrFactorNameSector,ffiecCodeScheduleRICAllowanceBalance,ffiecCodeScheduleRCAmortizedCost,scenarioIdentifier,vintageReporting,adjustmentIdentifier,accountingClassificationUSGaap,productType,assetClass,company,delinquencyStatus,longTermRatingForPD,remainingMaturity,vintage,adjustmentIdentifier,issuingAgency,cusip,propertyType,propertyStatus,assetSubClass1,assetSubClass2,ficoScoreBand,instrumentType,instrumentSubType,amortizationType,lienPosition,interestRateType,productType,purchasedCreditDeteriorated,accruingCategory,ascImpairmentEvaluation,description,lossEstimationMethod,pdSource,pdModelName,lgdSource,lgdModelName,lossRateSource,lossRateCalculationMethod,lossRateModelName,eadSource,eadModelName,prepaymentSource,prepaymentModelName,reportingDate,ascImpairmentEvaluation","allMeasures":"lossAllowanceDelta,lossRateDelta,amortizedCost,unpaidPrincipalBalance,fairValue,pdOneYear,annualizedPDLifetime,cumulativePDLifetime,lgdOneYear,lgdLifetime,lossRateOneYear,lossRateCumulativeLifetime,lossRateAnnualizedLifetime,undrawnCommitmentAmount,currentCommitmentAmount,originalNotionalAmount,ccf,onBalanceSheetReserve,offBalanceSheetReserve,netBalance,yearToMaturity,instrumentIdentifier,lossRateOneYear","allFields":"","source":"output","tenant":"moodys","description":"","tag":"Disclosures (FASB)","scopes":[{"attributeName":"scenarioIdentifier","operator":"=","values":["Summary"]},{"attributeName":"amortizedCost","operator":"!=","values":["0.0000"]},{"attributeName":"accountingClassificationUSGaap","operator":"!=","values":["Available for sale (AFS)"]}],"viewFormat":{"rowTotal":false,"columnTotal":true},"preferred":true,"analysisId":14066}}'
#             # content_type = 'application/json'
#             # headers = {"Content-Type" : content_type, 'Authorization': auth_token}
#             # json_payload = json.loads(payload)
#             result = client.get(
#                 '/home',
#                 # data = payload,
#                 # headers = headers
#             )

#             self.assertEqual(result.status_code, 400)

# if __name__ == "__main__":
#     unittest.main()