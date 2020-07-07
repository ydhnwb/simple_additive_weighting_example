import etc
from normalizator import Normalizator


normalizator = Normalizator()
candidates_attr = list(map(lambda data: {'id': data['id'], 'attributes': data['attributes'] }, etc.candidates))


candidates_attr_normalized = list()

def get_spesific_values(a_list, key):
    temp = []
    for d in a_list:
        temp.append(d['attributes'][key])
    return temp



for i in range(len(candidates_attr)):
    current_salary = candidates_attr[i]['attributes']['salary']
    current_gpa = candidates_attr[i]['attributes']['gpa']
    current_dependant = candidates_attr[i]['attributes']['dependant']

    salary_normalized = normalizator.normalize_salary(get_spesific_values(candidates_attr, 'salary'), current_salary)
    gpa_normalized = normalizator.normalize_gpa(get_spesific_values(candidates_attr, 'gpa'), current_gpa)
    dependant_normalized = normalizator.normalize_dependant(get_spesific_values(candidates_attr, 'dependant'), current_dependant)

    candidates_attr_normalized.append([candidates_attr[i]['id'],salary_normalized, gpa_normalized, dependant_normalized])


# Create a simple weight
# example, salary weight is 50%, gpa is 25% and dependant is 25%
role = [50, 25, 25]
results = []
accept = False
for i  in range(len(candidates_attr_normalized)):
    temp_result = 0
    for g in range(len(candidates_attr_normalized[i])):
        if g != 0:
            accept = True
            temp_result = candidates_attr_normalized[i][g] * role[g-1]
        else:
            accept = False
    
    if(accept is True):
        results.append({'id':candidates_attr_normalized[i][0], 'score':temp_result})

results = sorted(results, key = lambda i: i['score'],reverse=True) 
for x in range(len(results)):
    id = results[x]['id']
    score = results[x]['score']*10
    print(f'User id {id} score {score}%')