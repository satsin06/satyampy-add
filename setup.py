from setuptools import setup, find_packages

setup(
    name='satyampy',
    version='0.1.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'satyampy = satyampy.__main__:main'
        ]
    },
    install_requires=[],
    python_requires='>=3.6',
)
