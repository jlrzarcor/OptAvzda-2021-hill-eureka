from distutils.core import setup
setup(
  name = 'hill_cg',         # How you named your package folder (MyLib)
  packages = ['hill_cg'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Use hill climbing to solve tsp',   # Give a short description about your library
  author = 'MLC, CR, JLRZC',                   # Type in your name
  author_email = '',      # Type in your E-Mail
  keywords = ['Hill Climbing', 'TSP', 'conjugate gradiant'],  # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8'
  ],
)
