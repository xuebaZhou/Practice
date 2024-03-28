# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# import requests
# import xml.etree.ElementTree as ET
#
# # Web 服务的 URL
# url = 'http://www.webxml.com.cn/webservices/DomesticAirline.asmx'
#
# # 构建 XML 格式的请求数据
# request_data = """
# <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://WebXml.com.cn/">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <web:getDomesticAirlinesTime>
#          <!--Optional:-->
#          <startCity>北京</startCity>
#          <!--Optional:-->
#          <lastCity>上海</lastCity>
#       </web:getDomesticAirlinesTime>
#    </soapenv:Body>
# </soapenv:Envelope>
# """
#
# # 设置请求头
# headers = {
#     'Content-Type': 'text/xml; charset=utf-8',
#     'SOAPAction': 'http://WebXml.com.cn/getDomesticAirlinesTime'
# }
#
# # 发送 POST 请求
# response = requests.post(url, data=request_data, headers=headers)
#
# # 解析 XML 响应
# root = ET.fromstring(response.text)
#
# # 处理响应数据
# airline_list = root.findall('.//startCity')
# for airline in airline_list:
#     print(airline.text)
import requests

# 构建 SOAP 1.1 请求
# url = 'http://www.webxml.com.cn/webservices/DomesticAirline.asmx'
# headers = {
#     'Content-Type': 'text/xml; charset=utf-8',
#     'SOAPAction': '"http://WebXml.com.cn/getDomesticAirlinesTime"'
# }
# body = """
# <?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getDomesticAirlinesTime xmlns="http://WebXml.com.cn/">
#       <startCity>string</startCity>
#       <lastCity>string</lastCity>
#       <theDate>string</theDate>
#       <userID>string</userID>
#     </getDomesticAirlinesTime>
#   </soap:Body>
# </soap:Envelope>
# """
# response = requests.post(url, data=body, headers=headers)
# print(response.content)
#
# # 构建 SOAP 1.2 请求
# url = 'http://www.webxml.com.cn/webservices/DomesticAirline.asmx'
# headers = {
#     'Content-Type': 'application/soap+xml; charset=utf-8',
# }
# body = """
# <?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <getDomesticAirlinesTime xmlns="http://WebXml.com.cn/">
#       <startCity>string</startCity>
#       <lastCity>string</lastCity>
#       <theDate>string</theDate>
#       <userID>string</userID>
#     </getDomesticAirlinesTime>
#   </soap12:Body>
# </soap12:Envelope>
# """
# response = requests.post(url, data=body, headers=headers)
# print(response.content)




import requests
def get_weather(city_name):
    service_url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'theCityName': city_name,
    }
    try:
        response = requests.post(service_url, headers=headers, data=data)

        if response.status_code == 200:
            weather_xml = response.text
            # 在这里对 XML 数据进行解析，并提取出需要的天气信息
            # 你可以使用 ElementTree 或者 BeautifulSoup 等库来解析 XML
            # 这里以 ElementTree 为例：
            # import xml.etree.ElementTree as ET
            # root = ET.fromstring(weather_xml)
            # weather = root.find(".//Weather").text
            # return weather
            return weather_xml
        else:
            return f"无法获取天气信息。状态码: {response.status_code}"
    except Exception as e:
        return f"发生错误: {e}"
    finally:
        if 'response' in locals():
            response.close()
if __name__ == "__main__":
    city_name = input("请输入城市名称: ")
    weather = get_weather(city_name)
    if weather:
        print(f"{city_name}的天气情况：{weather}")
    else:
        print("未能获取天气信息。")
