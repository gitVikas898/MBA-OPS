job_skills = {
    'database': ['postgres','MySQL','MongoDB'],
    'languages': ['Python','JavaScript'],
    'tools': ['Jupyter','Pandas','Excel']
}
print(job_skills)
job_skills.update({'cloud':['AWS','Google Cloud']})
print(job_skills)

print(job_skills.get('languages')[0])
print(job_skills.values())
job_skills.clear()
print(job_skills)