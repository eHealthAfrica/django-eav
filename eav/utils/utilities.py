from django.conf import settings


class Utils(object):
    ENTITY_ID_TYPES = {
        'uuid': 'entity_uuid',
        'int': 'entity_id'
    }

    def get_eav_entity_id_type(self):
        key = getattr(settings, 'EAV_ENTITY_ID_TYPE', 'int')
        try:
            return self.ENTITY_ID_TYPES[key]
        except KeyError:
            print('%s not supported, kindly try uuid or int, defaulting to int' % key)
        return self.ENTITY_ID_TYPES['int']
