from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'autonomous_tb3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'world/maze'), glob('world/maze/*')),
        (os.path.join('share', package_name, 'world/square'), glob('world/square/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tue',
    maintainer_email='tue@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'occupancy_grid_pub = autonomous_tb3.occupancy_grid_pub:main',
            'sdf_spawner = autonomous_tb3.spawn_entity:main',
            'commander = autonomous_tb3.commander:main'
        ],
    },
)
