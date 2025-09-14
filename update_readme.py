import requests
import datetime

handle = "khaoula-km"
url = f"https://codeforces.com/api/user.status?handle={handle}"

response = requests.get(url).json()

problems = set()
for submission in response['result']:
    if submission['verdict'] == 'OK':
        problem = submission['problem']
        problem_id = f"{problem.get('contestId', '')}-{problem.get('index', '')}"
        problems.add(problem_id)

problems = sorted(list(problems))

# Write README
with open("README.md", "w") as f:
    f.write("# My Codeforces Solutions\n\n")
    f.write(f"**Handle:** {handle}\n")
    f.write(f"**Total Solved Problems:** {len(problems)}\n")
    f.write(f"**Last Updated:** {datetime.datetime.now()}\n\n")
    f.write("## Problems Solved\n")
    f.write("| Contest | Problem |\n")
    f.write("|---------|---------|\n")
    for p in problems:
        contest, problem = p.split('-')
        f.write(f"| {contest} | {problem} |\n")
