from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'harpia_proj_final'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.[pxy][yma]*'))),
        # (os.path.join('share', package_name, 'models'), glob(os.path.join('models', '*.sdf'))),
        (os.path.join('share', package_name, 'params'), glob(os.path.join('params', '*.yaml'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.sdf'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "mover = harpia_proj_final.move:main",
        ],
    },
)
