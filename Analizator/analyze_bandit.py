import zipfile
import os
import shutil

from apps.codeAnalyzer.models import Problems


def unzip_directory(path):
    shutil.rmtree('media/source_code/')
    with zipfile.ZipFile(path) as f:
        f.extractall('media/source_code/')

    for root, dirs, files in os.walk("media/source_code"):
        if 'venv' in dirs:
            for d in dirs:
                if 'venv' in d:
                    shutil.rmtree(os.path.join(root, d))


def analyze_code(filename):
    command = "bandit -r .\media\source_code\  -o templates/bandit_report.html -f html"

    pipe = os.popen(command)
    text_cmd = pipe.read()

    project = Problems.objects.filter(project=filename).first()
    if project is not None:
        Problems.objects.filter(project=filename).all().delete()
    for root, dirs, files in os.walk("media/source_code"):

        for file in files:
            if file.endswith('.py'):

                file_path = os.path.join(root, file)

                command = "bandit " + "" + file_path

                pipe = os.popen(command)
                text_cmd = pipe.read()
                issue = ""
                location = ""
                confidence = ""
                flag = False
                for line in text_cmd.splitlines():
                    if 'Location' in line:
                        location = line.split()[1]

                    if 'Issue' in line:
                        issue = line

                    if 'Confidence' in line:
                        confidence = line.split()[3]

                    if location != "" and issue != "" and confidence != "":
                        problem = Problems(project=filename, location=location, error=issue, level=confidence)
                        problem.save()
                        issue = ""
                        location = ""
                        confidence = ""


