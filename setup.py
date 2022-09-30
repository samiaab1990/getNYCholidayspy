from setuptools import setup

setup(
    name='getnycholidayspy',
    version='0.0.1',
    author='Samia B',
    author_email='samiaab1990@gmail.com',
    license='MIT',
    packages=['getNYCholidayspy'],
    scripts=['scripts/getnycholidayspy_test.py'],
    url='https://github.com/samiaab1990/getNYCholidayspy',
    description="A Python version of the getNYCholidays package. Retrieves a vector of official NYC holiday dates from the NYC Office of Payroll Administration's List of Holidays PDF. Allows to retrieve dates by filtering on holiday name, weekday and date.",
)