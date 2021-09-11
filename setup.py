from setuptools import setup

setup(name='BoatControl',
      version='0.1',
      description='A new BoatControl App with MQTT and HomeKit',
      url='https://github.com/vojj/BoatControl',
      author='vojj',
      author_email='danielw@gmx.eu',
      license='MIT',
      install_requires=[
          'paho-mqtt',
          'pydispatch',
      ],
      zip_safe=False)
