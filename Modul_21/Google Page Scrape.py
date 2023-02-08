from requests import get
from bs4 import BeautifulSoup as bs

keyword = 'best food company'
keyword = keyword.replace(' ','+')

url = f'https://www.google.com/search?q={keyword}'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'cookie': 'HSID=ABI5viokDy3nJXIHM; SSID=AolHHEAFgcNlTq6lM; APISID=jJq5jjVIUx1EANCa/AID_sCwREEkCL7df-; SAPISID=R1HMPSm2MvwAwnOp/At043Esvp9dl-HYqo; __Secure-1PAPISID=R1HMPSm2MvwAwnOp/At043Esvp9dl-HYqo; __Secure-3PAPISID=R1HMPSm2MvwAwnOp/At043Esvp9dl-HYqo; SID=TAjEylN9VEASs6i6mCo2T9oNFwrjHqGW3D-2zmwuhPaAU2rtW8vCcidOy7Xwp8vdOJZhlg.; __Secure-1PSID=TAjEylN9VEASs6i6mCo2T9oNFwrjHqGW3D-2zmwuhPaAU2rtxrMWhsgMSDW3GokqE1RViA.; __Secure-3PSID=TAjEylN9VEASs6i6mCo2T9oNFwrjHqGW3D-2zmwuhPaAU2rtqXOsWRAkRVbk57G_r2TCSw.; OTZ=6867016_32_32__32_; AEC=ARSKqsILWnBWYHJ29F6n_72XIPzr8D6tAcIJ69VZNqFuBkRujMElfbmnSg; SEARCH_SAMESITE=CgQIwpcB; NID=511=fTJiFU840V2-3aQ1PBLv_shN-FxhuRAcuwV_toOuc4R3Adyu76y3b9qv0uvVr0P5cyqH5K_bVshloTF0i1KvudxxQruS8i4sbfFoYvJMuICSCOveLAQXDDVyv8xMQf_mS1z9JPrFMhcOcCToBRkSqNS9HE3O9pcgNKSvstpkVARFspVU46eHWyEQzchVREdaSlOm9TGaTxsqymt92PPctjt9DlCAFy6xJ814SXcpNp6yR5us8iBCt3Ht6kK2BvrqwZejQwaTG9nQLvqjnXVgiz8nI6UuwouOvfnwJf_U5aIZCIOjCgdh76qJeSVTDLYA0GTLkEWVo7m64Sc8Oc5UgZNXLvJcs8Hu1w; DV=o7sf_zYudTh6gIZJMH75pPJwwmukYliAuClUv9L1HQsAAPCYhXNegFgGvgMAANBSdRuTYlCKCQEAAF0qnu00FCAWSAAAAB71NcqXBrkQBEYCwEtSPKiaEkq6gZEAAA; 1P_JAR=2023-02-07-05; SIDCC=AFvIBn_UEsPnEx0AP2kmcbBM7wS_pkIpGy-wsOKXONcreN86AXPPHVmKeErM2dk8xJ66LFjx1hU; __Secure-1PSIDCC=AFvIBn8uIqYRC52S1simOO8UrI9hy669SsRKktOGSFdxSysA3Bqlp6eEhg2sADL200TYD49WWwZa; __Secure-3PSIDCC=AFvIBn_ADazrfeX86Td1l9k4RYg7P5mZxF0ohZSrfTRxPHSmbogWQXzyEw6J13BkcW_s0WHpBd8'
}

res = get(url, headers=headers)
soup = bs(res.text, 'html.parser')
data_section = soup.findAll('div', {'class': 'yuRUbf'})

links = []
for data in data_section:
    link_data = data.find('a').get('href')
    all_data = link_data
    links.append(all_data)

print(links)
