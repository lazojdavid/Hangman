#this proyect consist in filter a list of data, based on previous requirements
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    all_workers = list(filter(lambda worker: worker["language"] == "Python", DATA))
#   if u want use list comprehension
#    all_workers = [worker["name"] for worker in DATA if worker["language"] == "python" ]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]== "Platzi"]
    all_older = list(filter(lambda worker: worker["age"] > 18, DATA))
    all_older = list(map(lambda worker : worker["name"], all_older))
    print("--PERSONS BELLOW WRITE IN PYTHON---")
    for worker in all_workers:
        print(worker)
    print("----BELLOW WORKING IN PLATZI-----")
    for worker in all_platzi_workers:
        print(worker)
    print("--OLDER PEOPLE--")
    for worker in all_older:
        print(worker)


if __name__=="__main__":
    run()
