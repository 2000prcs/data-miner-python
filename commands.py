
def locate(companies, arg):
  # for company in companies:
  #   print('company state', company['state'])
  # filtered = [x for x in companies if x['state'] == arg]
  filtered_companies = list(filter(lambda company: company['state'] == arg, companies))
  result_companies = list(map(lambda company: company['company_name'], filtered_companies))
  return result_companies

def find_before(companies, arg):
  filtered_companies = list(filter(lambda company: company['year_founded'] and company['year_founded'] <= int(arg), companies))
  result_companies = list(map(lambda company: company['company_name'], filtered_companies))
  return result_companies


def find_after(companies, arg): 
  filtered_companies = list(filter(lambda company: company['year_founded'] and company['year_founded'] >= int(arg), companies))
  result_companies = list(map(lambda company: company['company_name'], filtered_companies))
  return result_companies


def find_companies_between_size(companies, arg): 
  filtered_companies = list(filter(lambda company: company['full_time_employees'] == arg, companies))
  result_companies = list(map(lambda company: company['company_name'], filtered_companies))
  return result_companies


def find_type(companies, arg): 
  filtered_companies = list(filter(lambda company: company['company_category'] == arg, companies))
  result_companies = list(map(lambda company: company['company_name'], filtered_companies))
  return result_companies