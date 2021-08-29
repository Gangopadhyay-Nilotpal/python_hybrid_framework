pytest -s -v -m "sanity" pak_testCases/

rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html pak_testCase/ --browser chrome