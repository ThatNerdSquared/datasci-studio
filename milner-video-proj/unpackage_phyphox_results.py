import shutil
import subprocess
from pathlib import Path


def read_in_trials(tlabel):
    for trial in range(1, 11):
        trial_id = f"{tlabel}-t{trial}"
        subprocess.run(['unzip', f'{trial_id}.zip'])
        newfile = Path('Frequency and speed.csv')
        newfile.rename(f'{trial_id}.csv')
        shutil.rmtree('meta')

for item in [20, 25, 35, 40, 5, 10]:
    read_in_trials(item)

