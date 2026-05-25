import configparser

config = configparser.ConfigParser()
config.read("f.ini")

# print all sections
print(config.sections())

for section in config.sections():
    print(f'[{section}]')

    # for option in config.options(section):
    #     print('\t',option, config.get(section, option))

# get all items from a section
it = config.items('mysqld_safe')
print(it)
