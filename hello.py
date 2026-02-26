import requsts

def health_check(url):
  try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      print("Service is UP")
    else:
      print("Service is DOWN")
  except Exception as e:
    print("Service is DOWN")
    print("Error.", e)

helth_check("http://localhost:8080")

