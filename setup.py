from distutils.core import setup
setup(
  name = 'sicboDice',         # How you named your package folder (MyLib)
  packages = ['sicboDice'],   # Chose the same as "name"
  version = '1.0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This function will determine the results of shuffling the dice that will be used in the Sicbo game.',   # Give a short description about your library
  author = 'Deza Farras Tsany',                   # Type in your name
  author_email = 'deza.ftsany@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/defartsa23/shuffle-dice-sicbo',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/defartsa23/shuffle-dice-sicbo/archive/refs/heads/main.zip',    # I explain this later on
  project_urls={
        'Documentation': 'https://github.com/defartsa23/shuffle-dice-sicbo',
        'Source': 'https://github.com/defartsa23/shuffle-dice-sicbo',
        'Tracker': 'https://github.com/defartsa23/shuffle-dice-sicbo/issues',
    },
  keywords = ['SICBO', 'DICE', 'SHUFFLE'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)