import json

def locate(companies, arg):
  filtered = filter(lambda company: company.state == arg, companies.items())
  print('filtered', dict(filtered))
  # mapped = map(lambda : expression)


# def find_before():
#   lambda company_data, arg: company_names,
# def find_after(): 
#   lambda,
# def find_companies_between_size(): 
#   lambda,
# def find_type(): 
#   lambda
