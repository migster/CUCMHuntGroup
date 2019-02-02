import requests

url = "https://10.10.20.2:8443/axl/"

querystring = {"":""}

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns=\"http://www.cisco.com/AXL/API/12.0\">\n    <soapenv:Header/>\n    <soapenv:Body>\n        <ns:getPhone>\n            <name>BOTUSER011</name>\n        </ns:getPhone>\n    </soapenv:Body>\n</soapenv:Envelope>"
headers = {
    'SOAPAction': "CUCM:DB ver=12.0 getPhone",
    'Content-Type': "text/xml",
    'Authorization': "Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ=",
    'cache-control': "no-cache",
    'Postman-Token': "811d29ac-af13-4582-9c1e-d8fd88aa0010"
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers, params=querystring)

print(response.text)