def params_function(param1):
    body = {
        param1 : "1"

    }
    return body

def headers_function(term1, term2):
    body = {
        "variable1": term1,
        "variable2": term2
    }
    return body

def headers_content():
    headers = {
      "headers": {
          "x-forwarded-proto": "http",
          "x-forwarded-port": "443",
          "host": "postman-echo.com",
          "x-amzn-trace-id": "Root=1-61e5a340-697633e467c740c50a149e7c",
          "content-type": "application/json",
          "user-agent": "PostmanRuntime/7.28.0",
          "accept": "*/*",
          "variable1": "term1",
          "variable2": "term2",
          "postman-token": "0daceda3-8ccc-49b9-b3b9-bf2e90e24c29",
          "accept-encoding": "gzip, deflate, br",
          "cookie": "sails.sid=s%3Ap1MDxspIWyG1wSOeY5Nl8-kJKEYp6GBL.9CdkTL4AR%2B625K6T6eIdpSLP6FhKGIFlWeZjLtjpxos"
      }
    }
    return headers
