def text_formatting(text: str, width: int, style: str) -> str:
    return text


if __name__ == '__main__':
    LINE = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure '
            'harum suscipit aperiam aliquam ad, perferendis ex molestias '
            'reiciendis accusantium quos, tempore sunt quod veniam, eveniet '
            'et necessitatibus mollitia. Quasi, culpa.')


text_formatting(LINE, 38, 'l')
#         '''Lorem ipsum dolor sit amet,
# consectetur adipisicing elit. Iure
# harum suscipit aperiam aliquam ad,
# perferendis ex molestias reiciendis
# accusantium quos, tempore sunt quod
# veniam, eveniet et necessitatibus
# mollitia. Quasi, culpa.''', 'Left 38'

text_formatting(LINE, 30, 'c')
#         ''' Lorem ipsum dolor sit amet,
# consectetur adipisicing elit.
#  Iure harum suscipit aperiam
#   aliquam ad, perferendis ex
#      molestias reiciendis
# accusantium quos, tempore sunt
#    quod veniam, eveniet et
#    necessitatibus mollitia.
#         Quasi, culpa.''', 'Center 30'

text_formatting(LINE, 50, 'r')
 #        '''           Lorem ipsum dolor sit amet, consectetur
 #     adipisicing elit. Iure harum suscipit aperiam
 #   aliquam ad, perferendis ex molestias reiciendis
 #       accusantium quos, tempore sunt quod veniam,
 # eveniet et necessitatibus mollitia. Quasi, culpa.''', 'Right 50'

text_formatting(LINE, 45, 'j')
#         '''Lorem   ipsum  dolor  sit  amet,  consectetur
# adipisicing elit. Iure harum suscipit aperiam
# aliquam    ad,   perferendis   ex   molestias
# reiciendis  accusantium  quos,  tempore  sunt
# quod   veniam,   eveniet   et  necessitatibus
# mollitia. Quasi, culpa.''', 'Justify 45'
