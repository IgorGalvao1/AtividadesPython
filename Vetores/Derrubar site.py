import requests
while True:
  r = requests.get('https://www.pompeia.sp.gov.br/')
  if(r.status_code == 200):
    print('Atacando site')
  else:
      print('Site fora do ar')