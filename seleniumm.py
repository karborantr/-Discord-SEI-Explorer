def get_data():
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from bs4 import BeautifulSoup
  
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--incognito')
  chrome_options.add_argument('--ignore-certificate-errors')
  
  global latest_block, supply,community_pool,block_time,chain,online_voting_power,active_validators,APR,inflation,list

  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://sei.explorers.guru/")
  page_source = driver.page_source
  soup = BeautifulSoup(page_source, "lxml")
  Supply_vars = soup.find_all("p", {"class": "chakra-text css-1mn117a"})
  latest_block = Supply_vars[0].get_text()
  supply = Supply_vars[1].get_text()
  community_pool = Supply_vars[2].get_text()
  block_time_vars = soup.find_all("p", {"class": "chakra-text css-ty28gi"})
  block_time = block_time_vars[0].get_text()
  chain = block_time_vars[1].get_text()
  active_validators_vars = soup.find_all("p", {"chakra-text css-kttl9l"})
  online_voting_power = active_validators_vars[0].get_text()
  active_validators = active_validators_vars[1].get_text()
  APR = active_validators_vars[2].get_text()
  inflation = active_validators_vars[3].get_text()
  list=[latest_block, supply,community_pool,block_time,chain,online_voting_power,active_validators,APR,inflation]
  return list
  

