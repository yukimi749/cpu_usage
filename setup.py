from setuptools import setup
import os
from glob import glob

package_name = 'cpu_usage'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yukimi Miyahara',
    maintainer_email='yukimi_pooh@au.com',
    description='a package for assignment',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cpu_utilization = cpu_usage.cpu_utilization:main',
            'listener = cpu_usage.listener:main',
        ],
    },
)
