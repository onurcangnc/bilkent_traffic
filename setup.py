from setuptools import setup
from pathlib import Path

# Read the contents of README.md for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='bilkent_traffic',
    version='0.6',  # Increment version appropriately
    description='A Python package for sending traffic violation reports via Bilkent email',
    long_description=long_description,  # Define the long_description variable
    long_description_content_type='text/markdown',  # Ensure the format is markdown
    py_modules=['bilkent_traffic'],
    install_requires=[
        'pyfiglet',
        'pillow',
    ],
    entry_points='''
        [console_scripts]
        bilkent_traffic=bilkent_traffic:main
    ''',
    author="Onurcan Genç",
    author_email="onurcan.genc@ug.bilkent.edu.tr",
    url="https://github.com/yourusername/bilkent_traffic",  # Update with your GitHub repo URL
    license='MIT',
)
