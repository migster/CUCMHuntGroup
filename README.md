This is sample code to query the Cisco CUCM AXL API for a device status (via getphone.py), and login or logout of the hunt group the device is associated with (via huntlogin.py and huntlogout.py respectively).

It should work right out of the box with the DevNet CUCM 12.0 sandbox since it it using the pre-populated devices and default credentials.  In a production environment it would not be a good idea to hardcode these into the code. I am also including a PDF of screenshots of the tests I did with postman used to generate this code. 

File descriptions: 

getphone.py: Get the device (phone) status. This is based on device name and we are looking for "BOTUSER011" which is one of the pre-populated Android devices.

huntlogin.py:  Login to the hunt group. The key identifier is the uuid gathered from the above step and setting hlogStatus to On 

huntlogout.py:  Logout of the hunt group. The key identifier is the uuid gathered from the above step and setting hlogStatus to Off


