## Step-by-step

**Step 1. Open a terminal in the project root.**
In VS Code, open the `python-bootcamp-team8` folder, then choose Terminal → New Terminal. Check you're in the right place by running this (`dir` on Windows CMD):
```
ls
```
You should see `tests`, `members`, `shared`.

**Step 2. Create a virtual environment and install pytest.** Type this in that terminal:

Windows (PowerShell):
```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install pytest
```
If PowerShell blocks the activate script, run `Set-ExecutionPolicy -Scope Process Bypass` first, then activate again.

macOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```
`.venv/` is already in `.gitignore`, so it won't be committed.


**Step 3. Run the tests.** Type this in the same terminal, from the project root:
For example: 
```
python -m pytest -v tests/test_w1.py --member hoanghaiviet100_creator --variant 1
```
Use `--variant <i>` if your `translate.py` implements <i> problem arcoding to the member list. For example:  Variants 2, 3 and 4 expect `insertion_sort`, `transpose` and `primes_up_to`.

**Step 4. Check the result.** You should see:
```
tests/test_w1.py::test_w1_1_summary PASSED
tests/test_w1.py::test_w1_2_word_count PASSED
tests/test_w1.py::test_w1_3_thesis PASSED
tests/test_w1.py::test_w1_4_translate PASSED
tests/test_w1.py::test_w1_5_by_day PASSED
5 passed
```

## Optional: the CI lint check

The CI runs `ruff check`, and it reports one style issue in `text_tools.py`: the imports need a blank-line fix. To clean it up:
```
python -m pip install ruff
python -m ruff check members/hoanghaiviet100_creator --fix
```