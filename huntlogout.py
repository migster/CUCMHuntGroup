import requests

url = "https://10.10.20.2:8443/axl/"

querystring = {"":""}

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns=\"http://www.cisco.com/AXL/API/12.0\">\n    <soapenv:Header/>\n    <soapenv:Body>\n        <ns:updatePhone>\n            <uuid>{93ABE697-403C-F042-60D3-D7694DC05792}</uuid>\n            <hlogStatus>Off</hlogStatus>\n        </ns:updatePhone>\n    </soapenv:Body>\n</soapenv:Envelope>"
headers = {
    'SOAPAction': "CUCM:DB ver=12.0 updatePhone",
    'Content-Type': "text/xml",
    'Authorization': "Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ=",
    'cache-control': "no-cache",
    'Postman-Token': "410dab1b-484b-4bdd-9131-9ec37a098e60"
    }

response = requests.request("POST", url, verify=False, data=payload, headers=headers, params=querystring)

print(response.text)